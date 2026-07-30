---
date: 2026-04-09 11:02
tags:
  - PHPC
  - MOC
---
### 🗺️ Lern-Roadmap

#### 🔴 PHASE 1: Höchste Priorität (Kernkonzepte & Hauptprogrammiermodelle)

>[!info]
>Diese Themen bilden das Fundament und stellen gewöhnlich den größten Teil der Klausurfragen dar.

1. **Shared Memory Programming mit OpenMP**
    - **Grundlagen & Direktiven:** `#pragma omp parallel`, `for`, `sections`, Variable Scoping (`private`, `shared`, `firstprivate`, `reduction`).
    - **Worksharing & Scheduling:** `static`, `dynamic`, `guided`, `runtime` (Wann nutzt man welches?).  
    - **Synchronisation:** `critical`, `atomic`, `barrier`, `single`, `master`.
    - **Task-basierte Ausführung:** `#pragma omp task`, `taskwait`, Task-Abhängigkeiten (`depend`).
    - **Performance & Pitfalls:**
        - **False Sharing** & **Array Padding** (Ursachen, Cache-Line-Ebene, Vermeidung). 
        - **NUMA-Architekturen** & **First-Touch-Policy** (Thread-Affinität / Data Placement).
2. **Distributed Memory Programming mit MPI (Message Passing Interface)**
    - **MPI-Grundlagen:** Ranks, Kommunikatoren (`MPI_COMM_WORLD`), Datentypen, Nachrichtenstruktur.
    - **Point-to-Point (P2P) Kommunikation:**
        - Blockierend (`MPI_Send`, `MPI_Recv`) vs. Nicht-blockierend (`MPI_Isend`, `MPI_Irecv`, `MPI_Wait`). 
        - Deadlock-Szenarien und Vermeidung. 
        - Überlappung von Kommunikation und Berechnung (Communication/Computation Overlap).
    - **Kollektive Kommunikation:** `MPI_Bcast`, `MPI_Reduce`, `MPI_Allreduce`, `MPI_Scatter`, `MPI_Gather`, `MPI_Barrier`.
    - **Einseitige Kommunikation (RMA / One-Sided):** `MPI_Win_create`, `MPI_Put`, `MPI_Get`, `MPI_Accumulate`, Synchronisations-Epochen (`MPI_Win_fence`).
3. **Rechnerarchitektur & Speicherhierarchie**
    - **CPU-Mikroarchitektur & ILP:** Instruction-Level Parallelism, Pipelining, Superskalarität, Out-of-Order Execution (OoO), SIMD/Vektorisierung. 
    - **Caches & Memory Wall:** Cache-Hierarchien (L1, L2, L3), Temporal & Spatial Locality, Cache Line Size (typisch 64 Bytes).

#### 🟡 PHASE 2: Hohe Priorität (Skalierung, Metriken & Beschleuniger)

4. **Konzepte der Parallelisierung & Skalierungsgesetze**
    - **Kennzahlen:** Speedup S(p), Effizienz E(p).
    - **Skalierung:**
        - **Strong Scaling:** Feste Problemgröße, steigende Prozessoranzahl → Limitiert durch den sequentiellen Anteil (**Amdahlsches Gesetz**).
        - **Weak Scaling:** Skalierende Problemgröße mit der Prozessoranzahl → **Gustafsonsches Gesetz**.
5. **GPU-Programmierung & Heterogene Systeme**
    - **CUDA-Architektur & Terminology:** Grid, Block, Thread, Warp (32 Threads), Executing Threads in Lockstep.
    - **Speicherhierarchie bei GPUs:** Registers, Shared Memory, Global Memory.
    - **OpenMP Offloading:** Pragmas für Accelerators (`#pragma omp target`, `map(to/from)`).
6. **Leistungsanalyse & Metriken**
    - **Arithmetic / Computational Intensity:** FLOPs pro Byte Hauptspeicherzugriff.
    - **Roofline-Modell:** Speicherbandbreiten-Limitierung vs. Compute-Limitierung.
    - **Profiling-Tools:** Grundlagen zu Vampir, IPM, PAPI.
#### 🟢 PHASE 3: Mittlere Priorität (Netzwerke, PGAS & Spezialthemen)

7. **Interconnection Networks & Netzwerktopologien**
    - **Netzwerkeigenschaften:** Durchmesser (Diameter), Bisektionsbandbreite (Bisection Bandwidth), Latenz, Durchsatz.
    - **Topologien:** Hypercube (Metriken wie Durchmesser log2​N), Mesh, Torus, Fat Tree. 
    - **Kommunikationsmodelle:** Hockney-Modell (T=α+β⋅L), LogP. 
8. **PGAS (Partitioned Global Address Space)**
    - **Konzept:** Logisch gemeinsamer Adressraum auf verteiltem Speicher. 
    - **Sprachen & Bibliotheken:** Unified Parallel C (UPC), DASH.
    - Vergleich zwischen PGAS, MPI und OpenMP (Vor- und Nachteile bzgl. Produktivität und Kontrolle).
9. **Parallele Algorithmen & Anwendungen**
    - **Domain Decomposition:** Gebietszerlegung, Oberflächen-zu-Volumen-Verhältnis (_Surface-to-Volume Ratio_) zur Minimierung des Kommunikationsaufwands.
    - **Anwendungsfälle:** Parallele Matrixmultiplikation, Fast Fourier Transform (FFT), Paralleles Sortieren, Sparse Matrices.