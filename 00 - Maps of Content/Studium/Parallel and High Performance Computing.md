---
date: 2026-07-30 11:02
tags:
  - MOC
  - PHPC
  - HPC
status: in-progress
last_updated: 2026-07-30
---

# 🖥️ PHPC - Master Map of Content

Willkommen zur zentralen Übersichtsseite für das Modul **Parallel and High Performance Computing (PHPC)**. Dieses MOC strukturiert das gesamte Vorlesungsmaterial, Praktikumsaufgaben und Prüfungsvorbereitungen in atomare Notizen.

---

## 📌 Schnellzugriff & Prüfungsfokus
- 🎯 **Hauptfokus:** OpenMP (Shared Memory) & MPI (Distributed Memory)
- 📊 **Metriken & Formeln:** Speedup, Efficiency, Amdahl/Gustafson, Roofline
- 🧪 **Prüfungsvorbereitung:** [[Klausur - Q&A Repetitorium]] | [[Klausur - Gedächtnisprotokolle]]

---

## 🔴 Phase 1: Kernkonzepte (Höchste Priorität)

### 🔹 01. Grundlagen & Hardware-Architektur
- [[Rechnerarchitektur & ILP]]
  - *Instruction-Level Parallelism, Superskalarität, Out-of-Order Execution, SIMD/Vektorisierung*
- [[Memory Wall & Caches]]
  - *Cache-Hierarchien (L1-L3), Temporal/Spatial Locality, Cache Line Size (64 Byte), Stride-1 Access*
- [[Parallele Kennzahlen & Skalierung]]
  - *Speedup $S(p)$, Effizienz $E(p)$, Strong Scaling (Amdahlsches Gesetz) vs. Weak Scaling (Gustafsonsches Gesetz)*

### 🔹 02. Shared Memory Programming (OpenMP)
- [[OpenMP - Grundlagen & Worksharing]]
  - *Fork-Join-Modell, `#pragma omp parallel`, `for`, `sections`, Variable Scoping (`shared`, `private`, `firstprivate`, `reduction`)*
- [[OpenMP - Scheduling]]
  - *`static`, `dynamic`, `guided`, `runtime` – Trade-offs zwischen Load Balancing und Overhead*
- [[OpenMP - Synchronisation]]
  - *`critical`, `atomic`, `barrier`, `single`, `master`, Deadlocks, Critical Sections*
- [[OpenMP - Tasks]]
  - *Task-basierte Ausführung, `#pragma omp task`, `taskwait`, `depend(in/out/inout)`, Rekursion (z. B. Fibonacci)*
- [[False Sharing & Array Padding]]
  - *Cache Line Invalidation Ping-Pong, Cache-Kohärenz, Vermeidung durch Pad-Structs oder thread-lokale Puffer*
- [[NUMA & First-Touch Policy]]
  - *Non-Uniform Memory Access, UMA vs. NUMA, Data Placement bei First-Touch*

### 🔹 03. Distributed Memory Programming (MPI)
- [[MPI - Grundlagen & P2P]]
  - *Ranks, Communicators (`MPI_COMM_WORLD`), Datentypen, Point-to-Point (`MPI_Send`, `MPI_Recv`)*
- [[MPI - Nicht-blockierende Kommunikation]]
  - *`MPI_Isend`, `MPI_Irecv`, `MPI_Wait`, Computation/Communication Overlap, Deadlock-Vermeidung*
- [[MPI - Kollektive Kommunikation]]
  - *`MPI_Bcast`, `MPI_Reduce`, `MPI_Allreduce`, `MPI_Scatter`, `MPI_Gather`, `MPI_Barrier`*
- [[MPI - One-Sided Communication (RMA)]]
  - *Remote Memory Access, RMA Windows (`MPI_Win_create`), `MPI_Put`, `MPI_Get`, `MPI_Accumulate`, Synchronization Epoches (`MPI_Win_fence`)*

---

## 🟡 Phase 2: Beschleuniger, Metriken & Netze (Hohe Priorität)

### 🔹 04. GPU-Programmierung & Heterogene Systeme
- [[GPU-Architektur & CUDA Grundlagen]]
  - *Streaming Multiprocessors (SM), CUDA Cores, Warps (32 Threads), Grid/Block/Thread Hierarchy, Shared vs. Global Memory*
- [[OpenMP - Offloading]]
  - *Host-Target Model, `#pragma omp target`, `teams`, `distribute`, `parallel for`, Data Mapping (`map(to/from)`)*

### 🔹 05. Performance-Analyse & Profiling
- [[Roofline Modell & Arithmetic Intensity]]
  - *Operational / Arithmetic Intensity (FLOPs/Byte), Memory-bound vs. Compute-bound Regionen*
- [[Profiling & Tracing Tools]]
  - *Hardware Performance Counter, PAPI, `perf`, IPM, Vampir, MPE, Tracing vs. Profiling*

### 🔹 06. Netzwerke & Topologien
- [[Interconnection Networks & Topologien]]
  - *Durchmesser, Bisektionsbandbreite, Latenz, Durchsatz, Topologien (Hypercube, Mesh, Torus, Fat Tree), Hockney-Modell ($T = \alpha + \beta \cdot L$)*

---

## 🟢 Phase 3: Algorithmen & Fortgeschrittene Paradigmen

### 🔹 07. PGAS & Spezielle Algorithmen
- [[PGAS & UPC]]
  - *Partitioned Global Address Space, Logisch gemeinsamer Speicher auf verteilter HW, UPC, DASH*
- [[Domain Decomposition & Parallele Algorithmen]]
  - *Gebietszerlegung, Surface-to-Volume Ratio, Stencil Computations, Sparse Matrices, FFT*
- [[Matrixmultiplikation Optimierung]]
  - *Naiv ($ijk$) vs. Loop Interchange ($ikj$), Cache Blocking / Tiling, AVX-Vektorisierung*

---

## 🎯 Phase 4: Klausurvorbereitung & Praxistests

- [[Klausur - Q&A Repetitorium]]
  - *Fragenkatalog aus den offiziellen Q&A-Folien (15.QandA.pdf)*
- [[Klausur - Gedächtnisprotokolle]]
  - *Ausgearbeitete Lösungen zu den Altklausuren (2021/22 & Folgende)*
