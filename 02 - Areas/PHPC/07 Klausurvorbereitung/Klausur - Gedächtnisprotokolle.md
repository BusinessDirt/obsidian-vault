---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[Klausur - Q&A Repetitorium]]"
---
## 1. Übersicht & Aufbau der PHPC Abschlussklausur

Die Prüfung "Parallel & High Performance Computing" gliedert sich in der Regel in folgende Aufgabentypen:

1. **Theorie- & Konzeptfragen (ca. 30%):** Verständnis von Architekturen, Kohärenzprotokollen, MPI-Semantik und OpenMP-Speichermodellen.
2. **Berechnungs- & Formelaufgaben (ca. 35%):** Speedup, Amdahl/Gustafson, Roofline-Modell, Netzwerktopologie-Parameter, Cache-Tag/Index/Offset-Breite.
3. **Code-Analyse & Bugfixing (ca. 35%):** Identifikation von Data Races, False Sharing, Deadlocks in MPI, falschen Scoping-Klauseln und Fehlen von Synchronisationen.

---

## 2. Auswertung typischer Klausuraufgaben

### Aufgabenblock A: Kennzahlen & Skalierung
* **Aufgabe:** Ein Programm benötigt auf 1 Core 100 Sekunden. Der sequentielle Anteil beträgt 10%. 
  * *Frage:* Wie hoch ist der Speedup auf 8 Cores nach Amdahl?
  * *Lösung:* $S(8) = \frac{1}{0.10 + \frac{0.90}{8}} = \frac{1}{0.10 + 0.1125} = \frac{1}{0.2125} \approx 4.70$.
  * *Frage:* Wie hoch ist der maximale theoretische Speedup auf beliebig vielen Cores?
  * *Lösung:* $\lim_{p \to \infty} S(p) = \frac{1}{0.10} = 10$.

### Aufgabenblock B: OpenMP Scoping & Bugs
* **Aufgabe:** Gegeben ist folgender Code. Finde 2 schwerwiegende Fehler:

```c
int sum = 0;
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    sum += A[i];
}
```

* *Fehler 1:* **Data Race auf `sum`**: `sum` ist standardmäßig `shared`. Mehrere Threads schreiben gleichzeitig darauf.
  * *Korrektur:* `reduction(+:sum)` hinzufügen.
* *Fehler 2:* Abhängig von der OpenMP Version ist $i$ zwar in C99 `for(int i...)` privat, aber bei externem $i$ ohne Deklaration wäre $i$ shared.

---

### Aufgabenblock C: MPI P2P Deadlock
* **Aufgabe:** Warum blockiert folgender MPI-Code bei großen Nachrichtenlängen?

```c
// Process 0                      // Process 1
MPI_Send(buf0, N, MPI_DOUBLE, 1, 0, comm);  MPI_Send(buf1, N, MPI_DOUBLE, 0, 0, comm);
MPI_Recv(buf1, N, MPI_DOUBLE, 1, 0, comm);  MPI_Recv(buf0, N, MPI_DOUBLE, 0, 0, comm);
```

* *Erklärung:* Da die Pufferekapazität des Betriebssystems bei großem $N$ überschritten wird, kehrt `MPI_Send` nicht mehr vorzeitig zurück. Beide Prozesse warten blockierend auf den jeweils anderen, um die Daten einzulesen.
* *Lösung:* Ersetzen durch `MPI_Sendrecv` oder nicht-blockierende Aufrufe `MPI_Isend` / `MPI_Irecv`.

---

### Aufgabenblock D: Cache-Mapping & Bitbreiten
* **Aufgabe:** Ein System hat 32-Bit Adressen und einen 64 KB 4-Way Set-Associative Cache mit 64 Byte Cache Lines. Berechne die Bitbreiten für Tag, Index und Offset.
* *Lösung:*
  * **Offset:** $\log_2(64) = 6 \text{ Bits}$.
  * **Anzahl Cache Lines gesamt:** $\frac{64 \text{ KB}}{64 \text{ Bytes}} = 1024 \text{ Lines}$.
  * **Anzahl Sets:** $\frac{1024 \text{ Lines}}{4 \text{ Ways}} = 256 \text{ Sets}$.
  * **Index Bits:** $\log_2(256) = 8 \text{ Bits}$.
  * **Tag Bits:** $32 - (8 + 6) = 18 \text{ Bits}$.
