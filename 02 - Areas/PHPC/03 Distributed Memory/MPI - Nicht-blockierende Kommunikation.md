---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Deadlocks
links: "[[MPI - Grundlagen & P2P]]"
---
## 1. Motivation: Überlappung von Kommunikation & Berechnung

Blockierende Kommunikationsaufrufe (`MPI_Send` / `MPI_Recv`) führen oft zu unproduktiven Wartezeiten (Idle Time) und bergen ein hohes Risiko für **Deadlocks**.

**Nicht-blockierende Kommunikation** (Non-blocking Communication) trennt den Initiierungsschritt einer Nachricht vom eigentlichen Vervollständigungsschritt. Dadurch lässt sich die Datenübertragung über das Netzwerk zeitlich mit rechenintensiven lokalen Aufgaben überlappen (**Latency Hiding**).

---

## 2. Nicht-blockierende P2P-Funktionen

Funktionsnamen beginnen mit `MPI_I...` (I = Immediate). Sie kehren **sofort** zurück, unabhängig vom Status der Datenübertragung.

```c
int MPI_Isend(const void *buf, int count, MPI_Datatype datatype, 
              int dest, int tag, MPI_Comm comm, MPI_Request *request);

int MPI_Irecv(void *buf, int count, MPI_Datatype datatype, 
              int source, int tag, MPI_Comm comm, MPI_Request *request);
```

> [!WARNING] Speicher-Gefahr bei Nicht-blockierenden Aufrufen
> Nach dem Aufruf von `MPI_Isend` / `MPI_Irecv` darf der Puffer `buf` **weder gelesen noch verändert werden**, bis die Übertragung explizit als abgeschlossen bestätigt wurde!

---

## 3. Synchronisation & Abfrage von Requests

Um den Abschluss der nicht-blockierenden Operation sicherzustellen, stehen folgende Funktionen bereit:

### Blockierende Fertigstellung (`MPI_Wait`)
```c
MPI_Request req;
MPI_Status status;

MPI_Irecv(buf, count, MPI_DOUBLE, 0, 99, MPI_COMM_WORLD, &req);

// Local Computation (Latency Hiding)
compute_local_data();

// Warten, bis Empfang garantiert abgeschlossen ist
MPI_Wait(&req, &status);
```

### Nicht-blockierende Statusabfrage (`MPI_Test`)
```c
int flag;
MPI_Test(&req, &flag, &status);
if (flag) {
    // Übertragung abgeschlossen!
}
```

### Vektor-Varianten für mehrere Requests
* `MPI_Waitall(count, array_of_requests, array_of_statuses)`: Wartet auf *alle* Requests im Array.
* `MPI_Waitany(...)`: Wartet, bis *mindestens einer* abgeschlossen ist.

---

## 4. Deadlock-Vermeidung

### Das klassische P2P Deadlock-Szenario
Wenn zwei Prozesse gleichzeitig blockierend `MPI_Send` aneinander schicken und die Puffergröße überschritten wird:

```c
// Process 0:                  // Process 1:
MPI_Send(..., dest=1, ...);    MPI_Send(..., dest=0, ...); // DEADLOCK! Beide warten!
MPI_Recv(..., src=1, ...);     MPI_Recv(..., src=0, ...);
```

### Lösungsansätze:
1. **Verwendung von Nicht-blockierenden Aufrufen (`MPI_Isend` / `MPI_Irecv`).**
2. **Nutzung von `MPI_Sendrecv`**: Führt Senden und Empfangen in einem atomaren, deadlock-freien Aufruf aus.
