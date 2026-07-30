---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[MPI - One-Sided Communication (RMA)]]"
---
## 1. Das PGAS-Programmiermodell

Das **Partitioned Global Address Space (PGAS)** Modell kombiniert die einfache Programmierung des Shared-Memory-Modells mit der Performance-Kontrolle von Distributed-Memory-Architekturen.

* **Globaler Adressraum:** Ein einziger logischer Adressraum wird über alle Cluster-Knoten hinweg aufgespannt. Jeder Prozess/Thread kann direkt Variablen anderer Knoten referenzieren.
* **Partitionierung:** Der Speicher ist physisch partitioniert. Jeder Zeiger unterscheidet strikt zwischen **lokalem Speicher** (schnell) und **entferntem Speicher** (Remote Access über RDMA Netzwerk).

---

## 2. Unified Parallel C (UPC)

UPC ist eine Erweiterung der Sprache C basierend auf dem PGAS-Modell.

### Deklaration von Shared Data
```upc
#include <upc.h>

// Variable existiert genau 1-mal im globalen Adressraum auf Thread 0
shared int global_counter; 

// Array wird zyklisch elementweise auf alle UPC-Threads verteilt
shared int distributed_array[100 * THREADS]; 
```

### Zeiger-Klassifikation in UPC

| Zeigertyp | Deklarations-Syntax | Semantik |
| :--- | :--- | :--- |
| **Private Pointer to Local** | `int *p` | Standard C-Zeiger auf lokalen Speicher des Threads. |
| **Shared Pointer to Shared** | `shared int *p` | Zeiger auf ein Objekt im globalen Adressraum (kann lokal oder remote sein). |
| **Private Pointer to Shared** | `shared int *private p` | Lokaler Zeiger, der auf eine globale Adresse zeigt. |

---

## 3. Vergleich: Shared Memory vs. MPI vs. PGAS

| Eigenschaft | Shared Memory (OpenMP) | Distributed Memory (MPI) | PGAS (UPC / Chapel / Fortran Coarrays) |
| :--- | :--- | :--- | :--- |
| **Adressraum** | Global Gemeinsam | Strik Trennt per Prozess | **Global Partitioniert** |
| **Hardware** | Single Node / Multi-Core | Cluster / Distributed | Cluster / Supercomputer |
| **Kommunikation** | Implizit (Speicherkopien) | Explizit (`MPI_Send`/`Recv`) | Implizit via Remote Pointer (`*p_shared`) |
| **Performance-Kontrolle**| Schwer (NUMA-Issues) | Sehr hoch | Hoch (Dank expliziter Partitionierung) |
