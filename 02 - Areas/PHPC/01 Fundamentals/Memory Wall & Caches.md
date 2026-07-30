---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Caches
  - Locality
links:
  - "[[Matrixmultiplikation Optimierung]]"
  - "[[False Sharing & Array Padding]]"
---
## 1. Speichersysteme & Die "Memory Wall"

### Das Prozessor-Speicher-Leistungsgap
In den letzten Jahrzehnten stieg die Rechenleistung von Prozessoren (CPU Floating Point Operations per Second) historisch um ca. 50% pro Jahr, während die Zugriffs-Latenz des Hauptspeichers (DRAM) nur um ca. 7% pro Jahr sank.

Diese Diskrepanz wird als **Memory Wall** bezeichnet:
* Die CPU verbringt einen Großteil ihrer Zeit mit Warten auf Daten aus dem DRAM (Stall Cycles / Memory Stalls).
* Zugriffszeiten im Vergleich:
  * **CPU Register:** < 1 Taktzyklus (~0.3 ns)
  * **L1 Cache:** ~4 Taktzyklen (~1 ns)
  * **L2 Cache:** ~12 Taktzyklen (~3-4 ns)
  * **L3 Cache:** ~40 Taktzyklen (~10-15 ns)
  * **DRAM (Hauptspeicher):** ~200-300 Taktzyklen (~60-100 ns)

> [!WARNING] Von-Neumann-Flaschenhals
> Der Befehls- und Datentransfer über einen gemeinsamen Speicherbus begrenzt den Durchsatz moderner Von-Neumann-Architekturen. Ohne effiziente Cache-Hierarchien verkommt die schnellste CPU zu einer wartenden Einheit.

---

## 2. Das Lokalitätsprinzip (Principle of Locality)

Caches funktionieren nur deshalb so effektiv, weil reale Programme ein stark strukturiertes Zugriffsverhalten aufweisen:

### 1. Zeitliche Lokalität (Temporal Locality)
* **Prinzip:** Wird auf eine Speicheradresse zugegriffen, ist die Wahrscheinlichkeit hoch, dass auf dieselbe Adresse in naher Zukunft erneut zugegriffen wird.
* **Beispiel:** Schleifenzähler ($i$), Summenakkumulatoren, Instruktions-Code innerhalb von Schleifen.

### 2. Räumliche Lokalität (Spatial Locality)
* **Prinzip:** Wird auf eine Speicheradresse zugegriffen, ist die Wahrscheinlichkeit hoch, dass in naher Zukunft auf benachbarte Speicheradressen zugegriffen wird.
* **Beispiel:** Sequentieller Durchlauf eines Arrays im Speicher (Row-Major Order in C/C++).

> [!TIP] Cache Line Granularität
> Speicher wird nicht byteweise zwischen DRAM und Cache übertragen, sondern in Blöcken fixer Größe, den **Cache Lines** (in der Regel **64 Bytes**). Beim Zugriff auf ein einziges `double` (8 Bytes) werden stets die umliegenden 64 Bytes in den Cache geladen.

---

## 3. Cache-Architektur & Adress-Mapping

Ein Cache teilt eine Speicheradresse in drei logische Abschnitte auf: **Tag**, **Index** und **Offset**.

$$\text{Bit-Breite: } \quad \underbrace{\text{Tag}}_{\text{Identifikation}} \quad \vert \quad \underbrace{\text{Index}}_{\text{Set-Auswahl}} \quad \vert \quad \underbrace{\text{Offset}}_{\text{Byte in Cache-Line}}$$

### Mapping-Strategien

| Strategie | Funktionsweise | Vorteil | Nachteil |
| :--- | :--- | :--- | :--- |
| **Direct Mapped** | Jede Hauptspeicheradresse wird genau einem Cache-Set zugewiesen ($\text{Index} = \text{Adresse} \pmod N$). | Sehr einfache & schnelle Hardware-Implementierung. | Hohe Konflikt-Miss-Rate (Cache Thrashing). |
| **N-Way Set Associative** | Speicheradresse wird einem Set zugewiesen, das $N$ Slots (Ways) enthält. | Guter Kompromiss aus Latenz und Trefferquote. | Komplexere Such-Logik (Tag-Vergleich parallel). |
| **Fully Associative** | Cache Line kann an jeder beliebigen Stelle im Cache platziert werden. | Minimale Konflikt-Misses. | Hoher Hardware-Aufwand & höherer Energiebedarf. |

### Die 3 Cs der Cache Misses

1. **Compulsory Misses (Cold Misses):** Erstmaliger Zugriff auf einen Datenblock. Unvermeidbar.
2. **Capacity Misses:** Der Cache ist zu klein, um das gesamte Working Set des Programms aufzunehmen.
3. **Conflict Misses:** Mehrere benötigte Blöcke mappen auf dasselbe Cache-Set, obwohl im restlichen Cache noch Platz frei wäre (bei Direct Mapped / N-Way).

---

## 4. Cache-Kohärenz (Cache Coherence)

In Multi-Core-Systemen besitzt jeder Kern eigene L1/L2-Caches. Schreiben zwei Kerne auf dieselbe Adresse, müssen Cache-Inhalte abgeglichen werden.

### Das MESI-Protokoll
Jede Cache Line befindet sich in einem von vier Zuständen:

* **M - Modified:** Cache-Line ist gültig, befindet sich *nur* in diesem Cache und ist *dirty* (geändert tsb. Hauptspeicher).
* **E - Exclusive:** Cache-Line ist gültig, befindet sich *nur* in diesem Cache und ist *clean* (identisch mit Hauptspeicher).
* **S - Shared:** Cache-Line ist gültig, kann sich in *mehreren* Caches befinden und ist *clean*.
* **I - Invalid:** Cache-Line enthält keine gültigen Daten.

> [!IMPORTANT] Invaliderungs-Overhead
> Schreibt ein Core auf eine Cache Line im Zustand **Shared**, muss eine Invaliderungsnachricht über den Interconnect an alle anderen Cores gesendet werden, um deren Status auf **Invalid** zu setzen. Dies ist der primäre Auslöser für [[False Sharing & Array Padding]].
