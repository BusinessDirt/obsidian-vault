---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Fork-Join-Modell
  - Variable-Scoping
links:
  - "[[OpenMP - Scheduling]]"
  - "[[OpenMP - Synchronisation]]"
---
## 1. Das OpenMP Programmiermodell

OpenMP (Open Multi-Processing) ist ein direktivenbasierter Standard für die parallele Programmierung auf **Shared-Memory-Systemen** (Gemeinsamer Speicher).

### Das Fork-Join-Modell
* Ein OpenMP-Programm startet als einzelner Hauptthread (**Master Thread**).
* Trifft der Master Thread auf eine parallele Region (`#pragma omp parallel`), führt er ein **Fork** aus: Es wird ein Team von Worker Threads erzeugt.
* Alle Threads führen den Code innerhalb der Region parallel aus.
* Am Ende der parallelen Region erfolgt ein **Join**: Ein impliziter Barriere-Synchronisationspunkt führt dazu, dass die Worker Threads warten und aufgelöst werden, woraufhin der Master Thread alleine fortfährt.

```
Master Thread -------> FORK ======= Worker Threads ======= JOIN -------> Master Thread
                       (Parallel Region)
```

---

## 2. Worksharing Konstrukte

Damit nicht jeder Thread exakt denselben Code redundant ausführt, verwendet man Worksharing-Direktiven zur Aufteilung der Arbeit.

### 1. Schleifenparallelisierung (`#pragma omp for`)
Teilt die Iterationen einer `for`-Schleife auf das Team auf:

```c
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    c[i] = a[i] + b[i];
}
```

> [!IMPORTANT] Canonical Loop Form
> Schleifen für `#pragma omp for` müssen eine vorab bekannte Iterationszahl besitzen (Canonical Form). Der Schleifenindex darf innerhalb des Schleifenkörpers nicht manuell verändert werden (`i++` nur im Inkrement-Teil).

### 2. Sektionen (`#pragma omp sections`)
Teilt verschiedene unabhängige Aufgaben auf Threads auf:

```c
#pragma omp parallel sections
{
    #pragma omp section
    taskA();
    
    #pragma omp section
    taskB();
}
```

### 3. Einzel-Ausführung (`#pragma omp single` & `#pragma omp master`)
* `#pragma omp single`: Wird von genau **einem** (dem ersten ankommenden) Thread ausgeführt. Besitzt am Ende eine implizite Barriere.
* `#pragma omp master` / `#pragma omp masked`: Wird nur vom Master-Thread ausgeführt. Besitzt **keine** Barriere.

---

## 3. Data Sharing Attribute Clauses (Variable Scoping)

In OpenMP müssen Variablen explizit ihren Gültigkeitsbereich (Data-Sharing) zugewiesen bekommen:

| Clause | Semantik |
| :--- | :--- |
| **`shared`** | Variable existiert nur einmal im Speicher; alle Threads greifen auf dieselbe Adresse zu. (Gefahr von Data Races!) |
| **`private`** | Jeder Thread erhält eine uninitialisierte lokale Kopie. Der Wert vor der parallelen Region geht verloren. |
| **`firstprivate`** | Jeder Thread erhält eine lokale Kopie, die mit dem Wert der Variable vor Eintritt in die Region initialisiert wird. |
| **`lastprivate`** | Der Wert der sequentiell letzten Schleifeniteration wird nach Beendigung in die ursprüngliche Variable zurückgeschrieben. |
| **`default(none)`** | Erzwingt die explizite Deklaration des Scoping-Status für jede Variable im Block. Best Practice! |

---

## 4. Die `reduction` Clause

Zur Vermeidung von Race Conditions bei Summentformationen oder Produktbildungen nutzt man Reduktionen:

```c
double sum = 0.0;
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < N; i++) {
    sum += array[i];
}
```

* **Funktionsweise:** Jeder Thread erhält eine private Variable (initialisiert mit dem neutralen Element, z. B. `0` bei `+`). Am Ende kombiniert OpenMP die Teilergebnisse atomar.
