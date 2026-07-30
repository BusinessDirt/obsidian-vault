---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Caches
links:
  - "[[Memory Wall & Caches]]"
  - "[[OpenMP - Grundlagen & Worksharing]]"
---
## 1. Das Phänomen False Sharing

**False Sharing** ist einer der tückischsten Performance-Flaschenhälse in Shared-Memory-Systemen. Es tritt auf, wenn zwei oder mehr Prozessoren auf logisch völlig unabhängige Variablen zugreifen, die zufällig auf derselben physischen **Cache Line** (64 Bytes) liegen, und mindestens ein Zugriff schreibend ist.

```
+-------------------------------------------------------------+
|                     Cache Line (64 Bytes)                   |
|  [ Thread 0 Variable A (8B) ]  [ Thread 1 Variable B (8B) ] |
+-------------------------------------------------------------+
```

### Der Mechanismus der Entstehung
1. Core 0 schreibt auf `Variable A` $\rightarrow$ Die Cache Line in Core 0 wird **Modified (M)**.
2. Das Kohärenzprotokoll (MESI) invaldiert die gesamte Cache Line in Core 1 ($\rightarrow$ Status **Invalid (I)**).
3. Core 1 möchte nun auf seine unabhängige `Variable B` schreiben $\rightarrow$ **Cache Miss**!
4. Die Cache Line muss von Core 0 zu Core 1 transferiert werden.
5. Das Hin- und Herwechseln (Ping-Pong-Effekt) der Cache Line erzeugt massive Bus-Latenzen und zerstört die Skalierbarkeit.

---

## 2. Code-Beispiel für False Sharing

Schlechtes Design (Thread-Ergebnisse in einem gemeinsamen Array):

```c
double sum[NUM_THREADS]; // Alle Elemente liegen direkt nebeneinander!

#pragma omp parallel num_threads(NUM_THREADS)
{
    int tid = omp_get_thread_num();
    for (int i = 0; i < N; i++) {
        sum[tid] += compute(i); // False Sharing Katastrophe!
    }
}
```

---

## 3. Lösungsstrategien

### 1. Thread-lokale Akkumulation (Best Practice)
Jeder Thread akkumuliert Zwischenergebnisse in einer lokalen Stack-Variable und schreibt erst am Ende einmalig in den gemeinsamen Speicher:

```c
#pragma omp parallel num_threads(NUM_THREADS)
{
    int tid = omp_get_thread_num();
    double local_sum = 0.0;
    for (int i = 0; i < N; i++) {
        local_sum += compute(i);
    }
    sum[tid] = local_sum; // Nur ein einziger Schreibzugriff am Ende
}
```

### 2. Array Padding (Speicher-Auffüllung)
Man erzwingt einen Mindestabstand zwischen Elementen, sodass jedes Array-Element in seiner eigenen Cache Line liegt:

```c
#define CACHE_LINE_SIZE 64
struct PaddedDouble {
    double value;
    char pad[CACHE_LINE_SIZE - sizeof(double)]; // 56 Bytes Padding
};

struct PaddedDouble sum[NUM_THREADS];
```

Oder in C++11 mittels `alignas`:

```cpp
struct alignas(64) AlignedDouble {
    double value;
};
```
