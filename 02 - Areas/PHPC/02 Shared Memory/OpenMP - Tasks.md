---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Tasking-Modell
  - Rekursion
links: "[[OpenMP - Synchronisation]]"
---
## 1. Das OpenMP Tasking Modell

Während klassische Worksharing-Konstrukte (`#pragma omp for`) gut für regelmäßige Schleifen geeignet sind, stoßen sie bei unregelmäßigen Datenstrukturen (z. B. Bäumen, Graphen oder rekursiven Algorithmen) an ihre Grenzen.

Ein **Task** in OpenMP ist eine unabhängige Arbeitseinheit bestehend aus:
1. Dem auszuführenden Code.
2. Den zugehörigen Daten (Data Environment).

---

## 2. Erzeugung und Synchronisation von Tasks

### Task-Erzeugung (`#pragma omp task`)
Wird ein Task-Konstrukt von einem Thread angetroffen, erzeugt dieser ein Task-Objekt und gibt es an den Laufzeit-Scheduler ab. Der Erzeuger-Thread kann sofort ohne Warten fortfahren.

```c
#pragma omp parallel
{
    #pragma omp single
    {
        #pragma omp task
        do_work_A();

        #pragma omp task
        do_work_B();
    }
}
```

### Task-Synchronisation
* `#pragma omp taskwait`: Der aufrufende Task suspendiert die eigene Ausführung, bis alle von ihm direkt erzeugten **Child-Tasks** abgeschlossen sind.
* `#pragma omp taskgroup`: Wartet auf die Fertigstellung aller direkten und rekursiv erzeugten Nachkommen-Tasks innerhalb des Blocks.

---

## 3. Task Dependencies (Aufgaben-Abhängigkeiten)

OpenMP 4.0 führte die `depend`-Klausel ein, mit der Directed Acyclic Graphs (DAGs) von Tasks explizit definiert werden können:

```c
#pragma omp task depend(out: x)
init(x);

#pragma omp task depend(in: x) depend(out: y)
process(x, y);

#pragma omp task depend(in: y)
finalize(y);
```

* `depend(in: ...)`: Read-Only Abhängigkeit.
* `depend(out: ...)` / `depend(inout: ...)`: Write / Read-Write Abhängigkeit.
* Die OpenMP-Runtime stellt sicher, dass Tasks erst dann zur Ausführung freigegeben werden, wenn alle vorausgesetzten Daten-In-Abhängigkeiten erfüllt sind.

---

## 4. Beispiel: Rekursive Fibonacci-Berechnung

```c
int fib(int n) {
    if (n < 2) return n;
    int x, y;

    #pragma omp task shared(x) final(n < 20)
    x = fib(n - 1);

    #pragma omp task shared(y) final(n < 20)
    y = fib(n - 2);

    #pragma omp taskwait
    return x + y;
}
```

> [!WARNING] Task Overhead beachten
> Das Erzeugen mikroskopisch kleiner Tasks erzeugt spürbaren Laufzeit-Overhead. Mittels `final`-Klausel oder Schwellenwerten (Cut-off Thresholds) schaltet man bei kleinen Problemgrößen auf sequentiellen Code um.
