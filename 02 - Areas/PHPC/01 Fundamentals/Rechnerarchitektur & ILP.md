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
Die **Instruction Set Architecture (ISA)** dient als fundamentale Abstraktionsschicht zwischen Hardware und Software. Eine gut entworfene ISA zeichnet sich durch folgende Merkmale aus:
* **Langlebigkeit:** Überdauert mehrere Hardware-Generationen.
* **Allgemeine Verwendbarkeit:** Für verschiedene Anwendungsklassen geeignet.
* **Effizienz:** Erlaubt eine leistungsfähige Implementierung in der Hardware.

### Die CPU-Leistungsgleichung (Performance Equation)
Die Ausführungszeit eines Programms wird maßgeblich durch die CPU-Leistungsgleichung bestimmt:

$$\text{CPU-Zeit} = \frac{\text{Instruktionen}}{\text{Programm}} \times \frac{\text{Taktzyklen}}{\text{Instruktion (CPI)}} \times \frac{\text{Zeit}}{\text{Taktzyklus}}$$

> [!TIP] Optimierungsansatz
> Um die Ausführungszeit zu reduzieren, muss mindestens eine der folgenden Stellschrauben optimiert werden:
> 1. Reduktion der **Befehlsanzahl** (durch effiziente Compiler/Algorithmen).
> 2. Senkung der **Cycles Per Instruction (CPI)** (durch Befehlsparallelität/Pipelining).
> 3. Verringerung der **Taktzeit** (Erhöhung der Taktfrequenz).

---

## 2. Instruction-Level Parallelism (ILP)

Instruction-Level Parallelism (ILP) umfasst Verfahren, um innerhalb eines einzelnen, sequentiellen Befehlsstroms (Instruction Stream) Parallelität auf Hardware-Ebene zu entdecken und auszunutzen. 

Historisch galt das Ziel: **Parallelität vor dem Programmierer, dem Betriebssystem und dem Compiler vollständig zu verbergen**.

### Kernmechanismen von ILP

#### 1. Pipelining
* **Funktionsweise:** Unterteilung der Ausführung eines Befehls in mehrere Teilschritte (z. B. Fetch, Decode, Execute, Writeback).
* **Auswirkung:** Mehrere Befehle befinden sich zeitgleich in unterschiedlichen Phasen der Pipeline.
* **Leistungsmetrik:** Der theoretische maximale Speedup entspricht der Anzahl der Pipeline-Stufen. Die Latenz eines einzelnen Befehls bleibt unverändert, aber der Durchsatz steigt erheblich.

#### 2. Superskalarität (Superscalarity)
* **Funktionsweise:** Die CPU kann **mehr als einen Befehl pro Taktzyklus** starten (Issue/Launch).
* **Voraussetzung:** Vorhandensein mehrerer paralleler Ausführungseinheiten (ALUs, FPUs, Load/Store-Units).

#### 3. Out-of-Order Execution (OoO)
* **Funktionsweise:** Befehle werden nicht zwingend in der sequentiellen Programmreihenfolge abgearbeitet, sondern sobald ihre Operanden verfügbar und die benötigten Rechenwerke frei sind.
* **Prozessor-Architektur:**
  * **Front End (In-Order):** Fetch & Decode inklusive Sprungvorhersage (Branch Prediction).
  * **Execution Engine (Out-of-Order):** Dynamisches Scheduling und parallele Ausführung.
  * **Back End / Commit (In-Order):** Reordering und finaler Zustandstransfer, um die funktionale Korrektheit des sequentiellen Programms zu garantieren.

#### 4. VLIW (Very Long Instruction Word / EPIC)
* **Funktionsweise:** Mehrere unabhängige Befehle werden statisch zu einem einzigen langen Befehlswort gebündelt.
* **Unterschied zu Superskalarität:** Die Analyse von Datenabhängigkeiten erfolgt **statisch durch den Compiler** zur Übersetzungszeit und nicht dynamisch durch die Hardware.

---

## 3. Abgrenzung: ILP vs. DLP vs. TLP

Die nachfolgende Übersicht grenzt die verschiedenen Formen der Parallelität ab:

| Parallelitätsmodell | Ausprägung | Steuerung / Sichtbarkeit | Haupteinsatzbereich |
| :--- | :--- | :--- | :--- |
| **ILP** (Instruction Level) | Pipelining, Superskalarität, Out-of-Order | **Hardware-gesteuert / Transparent** | Einzelne Prozessorkerne |
| **DLP** (Data Level) | SIMD, Vektoringstruktionen (AVX, SSE) | **Explizit** (Compiler-Auto-Vektorisierung / Intrinsics) | Datenparallele Schleifen |
| **TLP** (Thread Level) | SMT (Hyper-Threading), Multi-Core | **Explizit** (OpenMP, pthreads, MPI) | Multi-Threaded / Verteilte Systeme |

---

## 4. Grenzen von ILP ("ILP Wall")

> [!WARNING] Historischer Paradigmenwechsel
> Die Steigerung der Rechenleistung rein über ILP und Erhöhung der Taktfrequenz stieß in den 2000er Jahren an physikalische Grenzen (Thermal- / Power-Wall):
> * Die Suche nach zusätzlicher Parallelität im sequentiellen Befehlsstrom lieferte kaum noch Erträge.
> * Der Energieverbrauch und die Wärmeentwicklung stiegen überproportional an.
> 
> **Konsequenz:** Der Wechsel von rein verdeckter Parallelität (ILP) hin zu expliziter Thread-Parallelität (Multi-Core-Prozessoren).