---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[OpenMP - Scheduling]]"
---
## 1. Non-Uniform Memory Access (NUMA)

In modernen Multi-Socket-Servern ist der Hauptspeicher physisch auf die einzelnen Prozessorsockel (NUMA-Knoten) aufgeteilt.

* **Local Memory Access:** Greift ein CPU-Kern auf den Speicher zu, der direkt an seinen eigenen Sockel angebunden ist, sind Latenz minimal und Bandbreite maximal.
* **Remote Memory Access:** Greift ein Kern auf den Speicher eines anderen Sockels zu, müssen die Daten über den Interconnect (z.B. Intel UPI, AMD Infinity Fabric) übertragen werden. Dies erhöht die Latenz erheblich (NUMA-Faktor meist 1.5x bis 2.5x).

---

## 2. Die First-Touch Policy des Betriebssystems

Linux allokiert Speicherseiten (Pages, typischerweise 4 KB) nach der **First-Touch Policy**:

> [!IMPORTANT] Kernerkenntnis
> Ein Aufruf von `malloc()` oder `new` reserviert lediglich virtuellen Adressraum. Die physische Speicherseite wird erst in dem Moment an den NUMA-Knoten gebunden, in dem der **erste Schreibzugriff** ("First Touch") auf diese Seite erfolgt.

### Das "Single-Threaded Initialization" Anti-Pattern

```c
// Step 1: Allokation
double *A = (double*) malloc(N * sizeof(double));

// Step 2: Sequential Initialization (FEHLER!)
for (int i = 0; i < N; i++) {
    A[i] = 0.0; // Master-Thread führt First Touch aus!
} // ALL Speicherseiten liegen nun physikalisch auf NUMA Node 0!

// Step 3: Parallel Computation
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    A[i] = compute(i); // Threads auf Node 1, 2, 3 leiden unter Remote Access!
}
```

---

## 3. NUMA-Aware Code schreiben

Um die First-Touch Policy korrekt auszunutzen, muss das Array **parallel mit derselben Datenverteilung initialisiert** werden, wie es später in der Berechnung verwendet wird:

```c
double *A = (double*) malloc(N * sizeof(double));

// Correct NUMA-Aware Initialization
#pragma omp parallel for schedule(static)
for (int i = 0; i < N; i++) {
    A[i] = 0.0; // Jeder Thread führt First-Touch für seine Speicherseiten aus!
}

// Parallel Computation
#pragma omp parallel for schedule(static)
for (int i = 0; i < N; i++) {
    A[i] = compute(i); // Perfekte Speicherlokalität auf jedem NUMA-Knoten!
}
```

---

## 4. Thread Pinning & Affinity Controls

Damit Threads nicht vom Betriebssystem während der Laufzeit auf andere NUMA-Knoten verschoben werden, bindet man sie fest an Cores (**Thread Affinity / Pinning**):

Umgebungsvariablen in OpenMP:
* `export OMP_PLACES=cores` (definiert die Ausführungseinheiten).
* `export OMP_PROC_BIND=spread` (verteilt Threads gleichmäßig auf NUMA-Knoten für maximale Bandbreite) oder `close` (hält Threads nahe beieinander für L3-Cache-Sharing).
