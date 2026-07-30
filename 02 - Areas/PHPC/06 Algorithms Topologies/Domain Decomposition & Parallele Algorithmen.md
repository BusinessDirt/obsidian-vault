---
date: 2026-04-09 11:02
tags:
  - PHPC
  - FFT
  - Sparse
  - Stencil
  - Gebietszerlegung
links: "[[MPI - Grundlagen & P2P]]"
---
## 1. Gebietszerlegung (Domain Decomposition)

Bei partiellen Differentialgleichungen (PDEs) und Gitter-basierten Simulationen zerlegt man das physikalische Rechengebiet in kleinere Teilgebiete (Subdomains), die auf verschiedene MPI-Prozesse verteilt werden.

### Zerlegungs-Topologien
* **1D-Zerlegung (Slabs / Streifen):** Einfach zu implementieren, aber hohes Verhältnis von Randfläche zu Volumen (Kommunikations-Overhead steigt bei vielen Prozessen).
* **2D-Zerlegung (Pencils / Stäbe):** Besser skalierbar für mittlere Cluster-Größen.
* **3D-Zerlegung (Cubes / Blöcke):** Minimales Oberflächen-zu-Volumen-Verhältnis $\left(\frac{O(N^2)}{O(N^3)}\right)$, beste Skalierbarkeit für Supercomputer.

---

## 2. Halo Cell Exchange (Ghost Cells)

Um Ableitungen an den Rändern der lokalen Subdomain zu berechnen, benötigt ein Prozess die Randwerte seiner Nachbarprozesse. Hierzu wird die Subdomain um eine Randschicht aus **Halo Cells (Ghost Cells)** erweitert.

```
+---+---+---+---+
| G | G | G | G | <-- Ghost Cells (vom Nachbarn empfangen)
+===+===+===+===+
| L | L | L | L | <-- Lokale Rechenzellen
| L | L | L | L |
+---+---+---+---+
```

### Der Halo-Austauschzyklus
1. **Nicht-blockierendes Senden (`MPI_Isend`)** der eigenen lokalen Randwerte an die Nachbarn.
2. **Nicht-blockierendes Empfangen (`MPI_Irecv`)** der gegenseitigen Randwerte in die Ghost Cells.
3. **Berechnung der inneren Zellen**, während die Netzwerkübertragung läuft (Latency Hiding).
4. **`MPI_Waitall`** abwarten und anschließend die Randzellen berechnen.

---

## 3. Typische Parallele Algorithmenmuster

### 1. Stencil Computations (Gitter-Iterationen)
* Wichtigste Vertreter: Jacobi-Verfahren, Gauss-Seidel-Verfahren zur Lösung von Poisson-Gleichungen.
* Jeder Punkt wird aus der Kombination seiner Nachbarpunkte des vorherigen Zeitschritts aktualisiert.

### 2. Fast Fourier Transform (FFT)
* Die parallele 3D-FFT erfordert zwei vollständige All-to-All Daten-Transpositionen (`MPI_Alltoallv`) zwischen 1D/2D-Zerlegungen, um die 1D-FFTs in allen drei Raumrichtungen nacheinander auszuführen.

### 3. Sparse Matrix Computations (SpMV)
* Dünnbesetzte Matrizen werden in komprimierten Formaten wie **CRS (Compressed Row Storage)** gespeichert.
* Die Parallelisierung erfordert unregelmäßige Datenzugriffe (Gather/Scatter) basierend auf der Graphen-Topologie der Matrix.
