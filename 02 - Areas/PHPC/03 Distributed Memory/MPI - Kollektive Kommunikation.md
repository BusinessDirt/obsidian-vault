---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[MPI - Grundlagen & P2P]]"
---
## 1. Konzepte Kollektiver Kommunikation

Kollektive Operationen beteiligen **alle Prozesse** innerhalb eines definierten Communicators (`MPI_COMM_WORLD`).

> [!IMPORTANT] Regel für Kollektive Operationen
> Alle Prozesse im Communicator müssen die kollektive Funktion aufrufen! Ein Versäumnis führt unweigerlich zum Einfrieren (Hang / Deadlock) des gesamten Programms.

---

## 2. Datenbewegungskommunikation

### 1. Broadcast (`MPI_Bcast`)
Verteilt Daten von einem Root-Prozess an alle anderen Prozesse.

```c
MPI_Bcast(void *buffer, int count, MPI_Datatype datatype, int root, MPI_Comm comm);
```

### 2. Scatter (`MPI_Scatter`)
Zerstückelt ein Array auf dem Root-Prozess in gleich große Blöcke und sendet den $i$-ten Block an Prozess $i$.

### 3. Gather (`MPI_Gather`)
Sammelt Datenblöcke aller Prozesse in Reihenfolge ihrer Ranks auf dem Root-Prozess auf.

### 4. Allgather (`MPI_Allgather`)
Sammelt die Daten aller Prozesse und stellt das vollständige Gesamtergebnis **allen** Prozessen zur Verfügung (Gather + Broadcast).

### 5. All-to-All (`MPI_Alltoall`)
Vollständige Matrix-Transposition der Daten: Prozess $i$ sendet das $j$-te Segment seines Puffers an Prozess $j$.

---

## 3. Reduktionsoperationen

Kollektive Reduktionen verknüpfen Elemente aller Prozesse mittels einer mathematischen Operation (z. B. `MPI_SUM`, `MPI_MAX`, `MPI_MIN`, `MPI_PROD`).

### `MPI_Reduce`
Reduziert die Daten aller Prozesse auf dem Root-Prozess:

```c
double local_val = calculate();
double global_sum;

MPI_Reduce(&local_val, &global_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
```

### `MPI_Allreduce`
Führt die Reduktion durch und verteilt das Gesamtergebnis an **jeden** Prozess im Communicator. (Entspricht `MPI_Reduce` gefolgt von `MPI_Bcast`).

---

## 4. Performance & Netzwerktopologie-Algorithmen

Moderne MPI-Implementierungen nutzen hochoptimierte Baum- und Ring-Topologien:

* **Binomial-Baum Broadcast:** Ein Broadcast an $N$ Prozesse benötigt nur $O(\log_2 N)$ Kommunikationsschritte statt $O(N)$ sequentieller Sends.
* **Ring-Allreduce (Baidu Ring Algorithm):** Teilt Daten in Chunks auf; optimale Netzwerkauslastung für große Datenmengen (wichtig im Deep Learning / HPC).
