---
date: 2026-04-09 11:02
tags:
  - PHPC
  - FLOP
  - Linpack
links: "[[Roofline Modell & Arithmetic Intensity]]"
---
## 1. Grundlagen der Performance-Analyse

Bei der Performance-Analyse unterscheidet man zwei grundlegende Messmethoden:

### 1. Profiling (Statistische Abtastung / Summenwerte)
* **Funktionsweise:** Das Programm wird periodisch unterbrochen (Sampling) oder Zähler werden an Funktionsgrenzen aggregiert.
* **Ergebnis:** Summenübersicht (z. B. "Funktion `matrix_mult()` verbrauchte 78% der Gesamtzeit").
* **Vorteil:** Sehr geringer Overhead.

### 2. Tracing (Chronologische Ereignisprotokollierung)
* **Funktionsweise:** Jedes Ereignis (Funktionseintritt, Senden einer MPI-Nachricht, Lock-Erwerb) wird mit einem hochpräzisen Zeitstempel in einer Trace-Datei protokolliert.
* **Ergebnis:** Detaillierte Zeitstrahl-Visualisierung (Timeline Graph).
* **Vorteil:** Verhaltens- und Abhängigkeitsanalyse zwischen Prozessen/Threads.

---

## 2. Hardware Performance Counter & PAPI

Moderne CPUs besitzen im Prozessor integrierte Hardware-Zähler (**Performance Monitor Units / PMUs**).

**PAPI (Performance Application Programming Interface)** bietet eine standardisierte C/Fortran-Schnittstelle zum Auslesen dieser Zähler:
* `PAPI_TOT_CYC`: Gesamte Taktzyklen.
* `PAPI_FP_OPS`: Anzahl an Fließkommaoperationen.
* `PAPI_L3_TCM`: Level 3 Cache Misses.

---

## 3. Die HPC Toolsuite im Vergleich

| Tool | Typ | Anwendungsbereich | Besonderheiten |
| :--- | :--- | :--- | :--- |
| **`gprof`** | Profiler | Single-Core CPU | Klassischer Compiler-basierter Profiler (`-pg`). |
| **`perf`** | Profiler | Linux CPU System | Linux Kernel-integriertes PMU Sampling Tool. |
| **Intel VTune** | Profiler | CPU & Shared Memory | Detaillierte Microarchitecture- & NUMA-Analyse. |
| **Score-P** | Profiler & Tracer | MPI, OpenMP, CUDA | Standardisiertes Measurement Infrastructure Framework. |
| **Vampir** | Tracing Viewer | MPI / Large Cluster | Kommerzielle, hochskalierbare Visualisierung von Traces. |
| **NVIDIA Nsight** | Profiler & Tracer | GPU / CUDA | Nsight Systems (System-Trace), Nsight Compute (Kernel-Details). |
