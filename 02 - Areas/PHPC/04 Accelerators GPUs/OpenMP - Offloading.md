---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Host-Target-Modell
  - Data-Mapping
links: "[[GPU-Architektur & CUDA Grundlagen]]"
---
## 1. Das OpenMP Target Offloading Modell

Seit OpenMP 4.0 unterstützt der Standard das Offloading von Berechnungen auf heterogene Beschleuniger (z. B. NVIDIA / AMD GPUs) mittels Direktiven.

Dies erlaubt die Entwicklung von portablem GPU-Code ohne herstellerspezifische Sprachen wie CUDA oder HIP.

---

## 2. Kernel Offloading Direktiven

### Das `#pragma omp target` Konstrukt
Überträgt den umschlossenen Codeblock zur Ausführung an das Zielgerät (Target Device / GPU):

```c
#pragma omp target
{
    // Code läuft auf der GPU!
}
```

### Die Hierarchie zur Ausnutzung von GPU-Parallelität
Um die tausenden Cores einer GPU voll auszulasten, kombiniert man vier Hierarchiestufen:

```c
#pragma omp target teams distribute parallel for
for (int i = 0; i < N; i++) {
    C[i] = A[i] + B[i];
}
```

* **`target`:** Erzeugt die Datenumgebung und startet die GPU-Ausführung.
* **`teams`:** Erzeugt eine Gruppe von Thread-Teams (entspricht CUDA **Thread Blocks**).
* **`distribute`:** Verteilt die Schleifeniterationen auf die verschachtelten Teams.
* **`parallel for`:** Parallelisiert die Iterationen innerhalb jedes Teams auf die Threads (entspricht CUDA **Threads**).

---

## 3. Data Mapping & Speicherverwaltung

Da Host (CPU) und Target (GPU) meist getrennte physische Hauptspeicher besitzen, müssen Daten explizit gemappt werden.

### Data Mapping Clauses
* `map(to: var)`: Kopiert den Wert der Variable vor der Region vom Host zur GPU.
* `map(from: var)`: Kopiert das Ergebnis nach Beendigung der Region von der GPU zum Host.
* `map(tofrom: var)`: Kombiniert `to` und `from` (Standard für benutzte Arrays).
* `map(alloc: var)`: Reserviert nur Speicher auf der GPU ohne Datenübertragung.

```c
#pragma omp target map(to: A[0:N], B[0:N]) map(from: C[0:N])
#pragma omp teams distribute parallel for
for (int i = 0; i < N; i++) {
    C[i] = A[i] + B[i];
}
```

---

## 4. Structured vs. Unstructured Data Environments

Um wiederholten unnötigen Datentransfer in Schleifen zu vermeiden:

### Structured Data Region (`#pragma omp target data`)
```c
#pragma omp target data map(to: A[0:N], B[0:N]) map(from: C[0:N])
{
    for (int iter = 0; iter < 1000; iter++) {
        #pragma omp target teams distribute parallel for
        for (int i = 0; i < N; i++) {
            C[i] += A[i] * B[i];
        }
    }
} // Daten werden ERST HIER zur CPU zurückkopiert!
```
