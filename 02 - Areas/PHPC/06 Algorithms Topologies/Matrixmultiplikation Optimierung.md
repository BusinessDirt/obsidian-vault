---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Blocking
  - Tiling
  - AVX2-Vektorisierung
links:
  - "[[Memory Wall & Caches]]"
  - "[[Roofline Modell & Arithmetic Intensity]]"
---
## 1. Naive Matrixmultiplikation & Das Cache-Problem

Die mathematische Definition der Matrixmultiplikation $C = A \cdot B$ für quadratische $N \times N$ Matrizen lautet:

$$C_{i,j} = \sum_{k=0}^{N-1} A_{i,k} \cdot B_{k,j}$$

### Der Naive $i-j-k$ Algorithmus

```c
for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
        for (int k = 0; k < N; k++) {
            C[i][j] += A[i][k] * B[k][j];
        }
    }
}
```

> [!WARNING] Cache Disaster bei naivem Code
> In C/C++ liegen Matrizen im **Row-Major Order** (zeilenweise) im Speicher:
> * `A[i][k]`: Greift zeilenweise zu $\rightarrow$ Gute räumliche Lokalität.
> * `B[k][j]`: Greift **spaltenweise** zu $\rightarrow$ Bei großem $N$ führt jeder Zugriff auf `B[k][j]` zu einem Cache Miss!

---

## 2. Schleifenumordnung ($i-k-j$ Permutation)

Durch vertauschen der beiden inneren Schleifen zu $i-k-j$:

```c
for (int i = 0; i < N; i++) {
    for (int k = 0; k < N; k++) {
        for (int j = 0; j < N; j++) {
            C[i][j] += A[i][k] * B[k][j]; // j läuft im innersten Loop!
        }
    }
}
```

* Sowohl `C[i][j]` als auch `B[k][j]` greifen nun **kontinuierlich zeilenweise** über den Index $j$ zu.
* Dies führt zu einer Speedup-Steigerung um den Faktor 5x bis 10x allein durch Ausnutzung räumlicher Lokalität!

---

## 3. Cache Blocking (Tiling)

Für Matrizen, die größer als der L2/L3-Cache sind, zerlegt man die Matrizen in kleine Sub-Blöcke (Tiles) der Größe $B \times B$, die vollständig in den Cache passen.

```c
for (int i0 = 0; i0 < N; i0 += BLOCK)
    for (int k0 = 0; k0 < N; k0 += BLOCK)
        for (int j0 = 0; j0 < N; j0 += BLOCK)
            // Kernel auf Block
            for (int i = i0; i < i0 + BLOCK; i++)
                for (int k = k0; k < k0 + BLOCK; k++)
                    for (int j = j0; j < j0 + BLOCK; j++)
                        C[i][j] += A[i][k] * B[k][j];
```

* Die Wiederverwendungsrate von Daten im L1-Cache steigt drastisch an.
* Die Arithmetische Intensität $I$ wächst von $O(1)$ auf $O(BLOCK)$.

---

## 4. Kombination mit SIMD & OpenMP

In der Praxis vereint man Tiling mit SIMD Vector Intrinsics (`_mm256_fmadd_pd`) und OpenMP Parallelisierung:

```c
#pragma omp parallel for collapse(2) schedule(static)
for (int i0 = 0; i0 < N; i0 += BLOCK) {
    for (int j0 = 0; j0 < N; j0 += BLOCK) {
        // Tiled Inner Loops with SIMD Autovectorization
    }
}
```
