---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Overhead-Tradeoffs
links: "[[OpenMP - Grundlagen & Worksharing]]"
---
## 1. Schleifen-Scheduling in OpenMP

Beim Parallelisieren von Schleifen mittels `#pragma omp for` bestimmt die `schedule`-Klausel, wie Schleifeniterationen (Chunks) den verfügbaren Threads zugewiesen werden.

Syntax: `#pragma omp parallel for schedule(kind [, chunk_size])`

---

## 2. Die Scheduling-Strategien im Detail

### 1. `static` (Statisches Scheduling)
* **Funktionsweise:** Die Iterationsmenge wird vor Ausführung der Schleife in Chunks der Größe `chunk_size` zerlegt und im Round-Robin-Verfahren fest den Threads zugeteilt. (Standard-Chunksize: $N / p$).
* **Vorteile:** Minimaler Laufzeit-Overhead, sehr gute Cache-Lokalität.
* **Nachteile:** Anfällig für Load Imbalance (Lastungleichheit), wenn Iterationen unterschiedlich lange dauern.

### 2. `dynamic` (Dynamisches Scheduling)
* **Funktionsweise:** Chunks der Größe `chunk_size` (Default: 1) werden in eine gemeinsame Queue gelegt. Sobald ein Thread einen Chunk abgearbeitet hat, fordert er dynamisch den nächsten an.
* **Vorteile:** Exzellente Lastverteilung bei stark schwankenden Ausführungszeiten pro Iteration.
* **Nachteile:** Hoher Overhead durch Synchronisation auf die Task-Queue; schlechtere Cache-Lokalität.

### 3. `guided` (Geführtes Scheduling)
* **Funktionsweise:** Ähnlich wie `dynamic`, jedoch schrumpft die Chunk-Größe exponentiell mit dem Fortschritt der Schleife bis zur Untergrenze `chunk_size`.
* **Vorteile:** Große Chunks am Anfang reduzieren den Queue-Overhead; kleine Chunks am Ende sorgen für Lastausgleich.

### 4. `auto` & `runtime`
* **`auto`:** Die Entscheidung wird dem Compiler / der Runtime überlassen.
* **`runtime`:** Die Strategie wird zur Laufzeit über die Umgebungsvariable `OMP_SCHEDULE` gesteuert (z. B. `export OMP_SCHEDULE="guided,16"`).

---

## 3. Vergleichende Übersicht

| Schedule-Typ | Overhead | Lastausgleich (Load Balancing) | Cache-Lokalität | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **`static`** | **Sehr gering** | Schlecht (bei variabler Last) | **Exzellent** | Gleichförmige Berechnungen (z. B. Vektoraddition) |
| **`dynamic`** | Hoch | **Sehr gut** | Mäßig | Unregelmäßige Workloads (z. B. Mandelbrot-Menge) |
| **`guided`** | Mittel | **Gut** | Gut | Variierende Schleifen mit vielen Iterationen |

> [!TIP] Performance-Rule-of-Thumb
> Beginne stets mit `schedule(static)`. Zeigt das Profiling erhebliche Thread-Wartezeiten am Ende der Schleife (Load Imbalance), teste `guided` oder `dynamic` mit angepasster Chunksize.
