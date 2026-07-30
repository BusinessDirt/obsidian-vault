---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[Klausur - Gedächtnisprotokolle]]"
---
## 1. Kompaktes Q&A Repetitorium für die Prüfung

### Q1: Was ist der Unterschied zwischen ILP, DLP und TLP?
* **Antwort:**
  * **ILP (Instruction Level Parallelism):** Hardware-gesteuerte verdeckte Parallelität im Befehlsstrom eines Prozessors (Pipelining, Out-of-Order).
  * **DLP (Data Level Parallelism):** Identische Operation wird explizit auf Vektoren angewendet (SIMD, AVX, GPU Warps).
  * **TLP (Thread Level Parallelism):** Explizit vom Programmierer definierte unabhängige Threads (OpenMP, MPI, pthreads).

### Q2: Warum führt die First-Touch Policy bei naiver Allokation zu NUMA-Problemen?
* **Antwort:** Speicherseiten werden physisch auf dem NUMA-Knoten derjenigen CPU platziert, die den allerersten Schreibzugriff ausführt. Initialisiert der Master-Thread ein Array sequentiell allein, liegen alle Seiten auf Sockel 0. Parallele Zugriffe anderer Sockel erleiden dann dauerhafte Remote-Access Latenzen.

### Q3: Wodurch unterscheidet sich `#pragma omp critical` von `#pragma omp atomic`?
* **Antwort:** `critical` erzeugt eine allgemeine Software-Sperre (Mutex) für ganze Codeblöcke mit hohem Overhead. `atomic` nutzt spezialisierte Hardware-Instruktionen der CPU für einzelne Speicheradressen und ist um Größenordnungen schneller.

### Q4: Wann tritt False Sharing auf und wie vermeidet man es?
* **Antwort:** Wenn verschiedene Cores schreibend auf unterschiedliche Variablen zugreifen, die zufällig in derselben 64-Byte Cache Line liegen. Dies erzeugt MESI-Cache-Line Ping-Pong. Vermeidung durch thread-lokale Akkumulation in Stack-Variablen oder Array Padding.

### Q5: Was besagt die Arithmetische Intensität im Roofline Modell?
* **Antwort:** Das Verhältnis von ausgeführten Fließkommaoperationen (FLOPs) zu übertragenen Hauptspeicher-Bytes ($\text{FLOP/Byte}$). Liegt $I$ unter dem Ridge Point $I^*$, ist die Anwendung Memory-Bound.

### Q6: Was unterscheidet `MPI_Bcast` von `MPI_Scatter`?
* **Antwort:** `MPI_Bcast` schickt denselben Gesamtdatenpuffer an alle Prozesse. `MPI_Scatter` teilt den Datenpuffer des Root-Prozesses in Stücke auf und sendet jedem Prozess ein individuelles Teilsegment.

### Q7: Warum ist Wormhole-Routing bei Cluster-Interconnects schneller als Store-and-Forward?
* **Antwort:** Weil Nachrichten in kleine Flits unterteilt werden, die wie bei einem Fließband durch die Switches geleitet werden. Die Übertragungsverzögerung hängt dadurch fast nur noch von der Nachrichtengröße ab, nicht mehr von der Anzahl der Zwischenknoten (Hops).

---

## 2. Formelsammlung auf einen Blick

* **CPU-Leistungsgleichung:** $\text{CPU-Zeit} = \text{Instruktionen} \times \text{CPI} \times \text{Taktzeit}$
* **Speedup:** $S(p) = \frac{T(1)}{T(p)}$
* **Effizienz:** $E(p) = \frac{S(p)}{p}$
* **Amdahl Speedup:** $S_{\text{Amdahl}}(p) = \frac{1}{s + \frac{1-s}{p}} \le \frac{1}{s}$
* **Gustafson Speedup:** $S_{\text{Gustafson}}(p) = s' + p(1-s')$
* **Arithmetische Intensität:** $I = \frac{\text{FLOPs}}{\text{Bytes}}$
* **Roofline Limit:** $P = \min(P_{\max}, I \times B_{\max})$
* **Ridge Point:** $I^* = \frac{P_{\max}}{B_{\max}}$
* **Karp-Flatt Metric:** $e = \frac{\frac{1}{S(p)} - \frac{1}{p}}{1 - \frac{1}{p}}$
* **Hypercube Parameter:** $N = 2^n \implies D = n, \, d = n, \, \text{Bisektionsbreite} = N/2$
