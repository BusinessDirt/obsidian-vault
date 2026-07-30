---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Ranks
  - Communicators
  - Datentypen
links:
  - "[[MPI - Nicht-blockierende Kommunikation]]"
  - "[[MPI - Kollektive Kommunikation]]"
---
## 1. Das Distributed Memory Modell & MPI

Im Gegenteil zu Shared-Memory-Systemen besitzen Knoten in **Distributed-Memory-Architekturen** (z. B. HPC-Clustern) keinen gemeinsamen physischen Adressraum. Jeder Prozess verwaltet ausschließlich seinen eigenen lokalen Speicher.

Die Kommunikation erfolgt explizit über den Austausch von Nachrichten über das Kommunikationsnetzwerk (Message Passing). Standard hierfür ist **MPI (Message Passing Interface)**.

---

## 2. MPI Kernkonzepte & Initalisierung

Ein MPI-Programm wird nach dem **SPMD-Modell** (Single Program, Multiple Data) gestartet: Alle Prozesse führen dasselbe Binärprogramm aus, steuern jedoch anhand ihrer eindeutigen Prozess-ID (**Rank**) unterschiedliche Pfade und Datenbereiche.

### Die minimalen MPI-Grundfunktionen

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv); // Initialisiert die MPI-Umgebung

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank); // Eigene Process ID (0 .. size-1)
    MPI_Comm_size(MPI_COMM_WORLD, &size); // Gesamtanzahl aller Prozesse

    printf("Hallo von Prozess %d von %d\n", rank, size);

    MPI_Finalize(); // Beendet die MPI-Umgebung
    return 0;
}
```

* **`MPI_COMM_WORLD`**: Der vordefinierte Standard-Communicator, der alle beim Programmstart gespawnten Prozesse umfasst.

---

## 3. Point-to-Point (P2P) Kommunikation

Point-to-Point-Kommunikation überträgt Daten direkt von einem festgelegten Sender-Prozess an einen Empfänger-Prozess.

### Blockierendes Senden & Empfangen

```c
int MPI_Send(const void *buf, int count, MPI_Datatype datatype, 
             int dest, int tag, MPI_Comm comm);

int MPI_Recv(void *buf, int count, MPI_Datatype datatype, 
             int source, int tag, MPI_Comm comm, MPI_Status *status);
```

#### Wichtige Parameter:
* `count` / `datatype`: Anzahl und MPI-Datentyp (`MPI_INT`, `MPI_DOUBLE`, `MPI_CHAR`, etc.).
* `tag`: Nachrichten-ID zur Zuordnung/Filterung von Nachrichten.
* `source` / `dest`: Rank des Senders bzw. Empfängers.
* Wildcards beim Empfang: `MPI_ANY_SOURCE`, `MPI_ANY_TAG`.

> [!NOTE] Semantik von `MPI_Send`
> `MPI_Send` kehrt erst dann zurück, wenn der Sende-Puffer gefahrlos wiederverwendet oder überschrieben werden darf. Es garantiert **nicht**, dass die Nachricht beim Empfänger bereits angekommen ist (hängt von interner Pufferung ab).

---

## 4. Die vier Sendemodi in MPI

| Modus | API-Funktion | Verhalten / Semantik |
| :--- | :--- | :--- |
| **Standard** | `MPI_Send` | Blockierend. Puffert entweder intern (Eager Protocol) oder wartet auf Recv (Rendezvous Protocol). |
| **Synchronous** | `MPI_Ssend` | Kehrt erst zurück, wenn der Empfänger den passenden `MPI_Recv` gestartet hat (Handshake). |
| **Buffered** | `MPI_Bsend` | Pufferung wird explizit vom Anwender im Speicher bereitgestellt (`MPI_Buffer_attach`). |
| **Ready** | `MPI_Rsend` | Darf nur aufgerufen werden, wenn der Empfänger `MPI_Recv` bereits gestartet hat (Performance-Boost). |
