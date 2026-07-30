---
date: 2026-04-09 11:02
tags:
  - PHPC
  - PAPI
  - IPM
  - Vampir
  - MPE
links: "[[Profiling & Tracing Tools]]"
---
## 1. Das Roofline Modell

Das **Roofline Modell** von Williams et al. ist ein anschauliches Performance-Modell zur Bewertung, ob ein Rechenkern (Kernel) durch die **Rechenleistung der CPU/GPU** (Compute-Bound) oder durch die **Speicherbandbreite des Hauptspeichers** (Memory-Bound) begrenzt wird.

---

## 2. Arithmetische Intensität (Arithmetic Intensity)

Die zentrale Kennzahl des Roofline Modells ist die **Arithmetische Intensität** $I$:

$$I = \frac{\text{Ausgeführte Fließkomma-Operationen (FLOP)}}{\text{Übertragene Speicher-Bytes (DRAM Bytes)}} \quad \left[ \frac{\text{FLOP}}{\text{Byte}} \right]$$

> [!TIP] Beispielrechnung
> Vektoraddition $C[i] = A[i] + B[i]$ für `double` (8 Bytes):
> * Fließkommaoperationen: 1 Addition ($1 \text{ FLOP}$)
> * Speicherzugriffe: 2 Loads ($A[i], B[i]$) + 1 Store ($C[i]$) = $3 \times 8 \text{ Bytes} = 24 \text{ Bytes}$
> * Arithmetische Intensität: $I = \frac{1 \text{ FLOP}}{24 \text{ Bytes}} \approx 0.0417 \text{ FLOP/Byte}$ (Sehr niedrig $\rightarrow$ Stramm Memory-Bound!).

---

## 3. Die Roofline-Kurve & Leistungsgrenzen

Die maximal erreichbare Performance $P$ (in GFLOP/s) wird durch folgende Funktion beschrieben:

$$P = \min \left( P_{\max}, \, I \times B_{\max} \right)$$

* $P_{\max}$: Maximale Peak-Rechenleistung der Hardware (FLOP/s).
* $B_{\max}$: Maximale Speicherbandbreite der Hardware (Bytes/s).
* $I$: Arithmetische Intensität der Anwendung (FLOP/Byte).

```
Performance P 
 (GFLOP/s) ^
           |             +----------------------- Peak Performance P_max (Compute-Bound)
           |            / 
           |           / 
           |          /  <-- Ridge Point I* = P_max / B_max
           |         /
           |        /  Memory Bandwidth Limit: P = I * B_max (Memory-Bound)
           +-------+------------------------------------> Arithmetic Intensity I (FLOP/Byte)
```

### Der Ridge Point (Knickpunkt)
Der **Ridge Point** $I^*$ markiert die minimale arithmetische Intensität, die ein Algorithmus aufweisen muss, um die theoretische Maximalleistung $P_{\max}$ der Hardware überhaupt erreichen zu können:

$$I^* = \frac{P_{\max}}{B_{\max}}$$

---

## 4. Optimierungsstrategien im Roofline Modell

1. **Memory-Bound Bereich ($I < I^*$):**
   * Ziel: Erhöhung der arithmetischen Intensität $I$.
   * Maßnahmen: **Cache Blocking / Tiling**, Register Reuse, Vermeidung von unötigen Speicherzugriffen.
2. **Compute-Bound Bereich ($I > I^*$):**
   * Ziel: Erhöhung von $P_{\max}$.
   * Maßnahmen: **SIMD / AVX-Vektorisierung**, Fused Multiply-Add (FMA), Instruction-Level Parallelism (ILP).
