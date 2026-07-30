---
date: 2026-04-09 11:02
tags:
  - PHPC
links: "[[PGAS & UPC]]"
---
## 1. Remote Memory Access (RMA) Konzept

MPI-2 führte das Konzept der **One-Sided Communication (Remote Memory Access / RMA)** ein. Im Gegensatz zur klassischen Point-to-Point-Kommunikation trennt RMA die Datenübertragung von der Prozess-Synchronisation.

Ein Prozess (Origin) kann direkt im Speicher eines entfernten Prozesses (Target) lesen oder schreiben, **ohne dass der Target-Prozess aktiv eine MPI-Funktion aufrufen muss**.

---

## 2. Speicherfenster (Memory Windows)

Bevor ein Prozess entfernten Zugriff erlaubt, muss er einen ausgewählten Speicherbereich als **Window** exportieren:

```c
MPI_Win win;
double *baseptr;

// Allokiert lokalen Speicher und macht ihn als Fenster für andere nutzbar
MPI_Win_allocate(size * sizeof(double), sizeof(double), MPI_INFO_NULL, 
                 MPI_COMM_WORLD, &baseptr, &win);

// ... Zugriffe ...

MPI_Win_free(&win);
```

---

## 3. One-Sided Datenzugriffs-Primitiven

* **`MPI_Put`:** Schreibt Daten aus dem lokalen Puffer direkt in das Window des Target-Prozesses.
* **`MPI_Get`:** Liest Daten aus dem Window des Target-Prozesses in den lokalen Puffer.
* **`MPI_Accumulate`:** Atomare Aktualisierung (z. B. Hinzuaddieren) von Daten im Target-Window.

---

## 4. Synchronisationsmodi in RMA

Da der Zielprozess an der Übertragung nicht beteiligt ist, erzwingen Synchronisations-Epochen die Speicher-Konsistenz:

### Active Target Synchronization (Fence)
Alle Prozesse treten gemeinsam in eine Zugriffsphase ein und beenden diese kollektiv:

```c
MPI_Win_fence(0, win); // Start der Epoch
if (rank == 0) {
    MPI_Put(local_buf, 10, MPI_DOUBLE, 1, 0, 10, MPI_DOUBLE, win);
}
MPI_Win_fence(0, win); // Ende der Epoch (Garantiert Fertigstellung des Put)
```

### Passive Target Synchronization (Lock / Unlock)
Erlaubt den Zugriff ohne jegliche Beteiligung des Zielprozesses (Echtes One-Sided):

```c
MPI_Win_lock(MPI_LOCK_EXCLUSIVE, target_rank, 0, win);
MPI_Put(buf, count, MPI_INT, target_rank, offset, count, MPI_INT, win);
MPI_Win_unlock(target_rank, win);
```
