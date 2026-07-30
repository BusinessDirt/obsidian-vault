---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Pipelining
  - Superskalarität
  - SIMD
links: "[[Memory Wall & Caches]]"
---
## 1. Grundlagen der Rechnerarchitektur & Leistungsgleichung

### Instruction Set Architecture (ISA)
[cite_start]Die **Instruction Set Architecture (ISA)** dient als fundamentale Abstraktionsschicht zwischen Hardware und Software[cite: 75]. Eine gut entworfene ISA zeichnet sich durch folgende Merkmale aus:
* [cite_start]**Langlebigkeit:** Überdauert mehrere Hardware-Generationen[cite: 75].
* **Allgemeine Verwendbarkeit:** Für verschiedene Anwendungsklassen geeignet.
* [cite_start]**Effizienz:** Erlaubt eine leistungsfähige Implementierung in der Hardware[cite: 75].

### Die CPU-Leistungsgleichung (Performance Equation)
[cite_start]Die Ausführungszeit eines Programms wird maßgeblich durch die CPU-Leistungsgleichung bestimmt[cite: 75, 76]:

$$\text{CPU-Zeit} = \frac{\text{Instruktionen}}{\text{Programm}} \times \frac{\text{Taktzyklen}}{\text{Instruktion (CPI)}} \times \frac{\text{Zeit}}{\text{Taktzyklus}}$$

> [!TIP] Optimierungsansatz
> Um die Ausführungszeit zu reduzieren, muss mindestens eine der folgenden Stellschrauben optimiert werden:
> 1. Reduktion der **Befehlsanzahl** (durch effiziente Compiler/Algorithmen).
> [cite_start]2. Senkung der **Cycles Per Instruction (CPI)** (durch Befehlsparallelität/Pipelining)[cite: 91].
> [cite_start]3. Verringerung der **Taktzeit** (Erhöhung der Taktfrequenz)[cite: 91].

---

## 2. Instruction-Level Parallelism (ILP)

[cite_start]Instruction-Level Parallelism (ILP) umfasst Verfahren, um innerhalb eines einzelnen, sequentiellen Befehlsstroms (Instruction Stream) Parallelität auf Hardware-Ebene zu entdecken und auszunutzen[cite: 79]. 

[cite_start]Historisch galt das Ziel: **Parallelität vor dem Programmierer, dem Betriebssystem und dem Compiler vollständig zu verbergen**[cite: 79, 95].

### Kernmechanismen von ILP

#### 1. Pipelining
* [cite_start]**Funktionsweise:** Unterteilung der Ausführung eines Befehls in mehrere Teilschritte (z. B. Fetch, Decode, Execute, Writeback)[cite: 79, 87].
* [cite_start]**Auswirkung:** Mehrere Befehle befinden sich zeitgleich in unterschiedlichen Phasen der Pipeline[cite: 95].
* [cite_start]**Leistung Metrik:** Der theoretische maximale Speedup entspricht der Anzahl der Pipeline-Stufen[cite: 87]. [cite_start]Die Latenz eines einzelnen Befehls bleibt unverändert, aber der Durchsatz steigt erheblich[cite: 87].

#### 2. Superskalarität (Superscalarity)
* [cite_start]**Funktionsweise:** Die CPU kann **mehr als einen Befehl pro Taktzyklus** starten (Issue/Launch)[cite: 97].
* [cite_start]**Voraussetzung:** Vorhandensein mehrerer paralleler Ausführungseinheiten (ALUs, FPUs, Load/Store-Units)[cite: 97].

#### 3. Out-of-Order Execution (OoO)
* **Funktionsweise:** Befehle werden nicht zwingend in der sequentiellen Programmreihenfolge abgearbeitet, sondern sobald ihre Operanden verfügbar und die benötigten Rechenwerke frei sind.
* **Prozessor-Architektur:**
  * **Front End (In-Order):** Fetch & Decode inklusive Sprungvorhersage (Branch Prediction).
  * **Execution Engine (Out-of-Order):** Dynamisches Scheduling und parallele Ausführung.
  * **Back End / Commit (In-Order):** Reordering und finaler Zustandstransfer, um die funktionale Korrektheit des sequentiellen Programms zu garantieren.

#### 4. VLIW (Very Long Instruction Word / EPIC)
* [cite_start]**Funktionsweise:** Mehrere unabhängige Befehle werden statisch zu einem einzigen langen Befehlswort gebündelt[cite: 76, 80].
* [cite_start]**Unterschied zu Superskalarität:** Die Analyse von Datenabhängigkeiten erfolgt **statisch durch den Compiler** zur Übersetzungszeit und nicht dynamisch durch die Hardware[cite: 80].

---

## 3. Abgrenzung: ILP vs. DLP vs. TLP

Die nachfolgende Übersicht grenzt die verschiedenen Formen der Parallelität ab:

| Parallelitätsmodell | Ausprägung | Steuerung / Sichtbarkeit | Haupteinsatzbereich |
| :--- | :--- | :--- | :--- |
| **ILP** (Instruction Level) | Pipelining, Superskalarität, Out-of-Order | [cite_start]**Hardware-gesteuert / Transparent** [cite: 79, 95, 97] | [cite_start]Einzelne Prozessorkerne [cite: 79] |
| **DLP** (Data Level) | [cite_start]SIMD, Vektoringstruktionen (AVX, SSE) [cite: 80, 101] | [cite_start]**Explizit** (Compiler-Auto-Vektorisierung / Intrinsics) [cite: 101] | [cite_start]Datenparallele Schleifen [cite: 80, 101] |
| **TLP** (Thread Level) | [cite_start]SMT (Hyper-Threading), Multi-Core [cite: 80] | [cite_start]**Explizit** (OpenMP, pthreads, MPI) [cite: 5, 10, 80] | [cite_start]Multi-Threaded / Verteilte Systeme [cite: 80] |

---

## 4. Grenzen von ILP ("ILP Wall")

> [!WARNING] Historischer Paradigmenwechsel
> Die Steigerung der Rechenleistung rein über ILP und Erhöhung der Taktfrequenz stieß in den 2000er Jahren an physikalische Grenzen (Thermal- / Power-Wall):
> * Die Suche nach zusätzlicher Parallelität im sequentiellen Befehlsstrom lieferte kaum noch Erträge.
> * Der Energieverbrauch und die Wärmeentwicklung stiegen überproportional an.
> 
> **Konsequenz:** Der Wechsel von rein verdeckter Parallelität (ILP) hin zu expliziter Thread-Parallelität (Multi-Core-Prozessoren).