---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Locks
  - Race-Conditions
links: "[[OpenMP - Tasks]]"
---
## 1. Notwendigkeit der Synchronisation

Sobald mehere Threads zeitgleich auf gemeinsamen Speicher (`shared`) zugreifen und mindestens ein Zugriff schreibend ist, entsteht ein **Data Race** (Datenrennen). Das Verhalten des Programms wird unbestimmt (Undefined Behavior).

---

## 2. Synchronisationskonstrukte in OpenMP

### 1. Barriere (`#pragma omp barrier`)
Erzwingt einen Synchronisationspunkt: Kein Thread passiert die Barriere, bevor nicht alle Threads im Team diesen Punkt erreicht haben.

> [!NOTE] Implizite Barrieren
> OpenMP setzt am Ende folgender Konstrukte automatisch eine implizite Barriere:
> * `#pragma omp parallel`
> * `#pragma omp for`
> * `#pragma omp sections`
> * `#pragma omp single`
>
> Unterdrückt werden kann dies durch Hinzufügen der `nowait`-Klausel.

### 2. Kritischer Abschnitt (`#pragma omp critical [(name)]`)
Garantiert, dass der umschlossene Codeblock zu jedem Zeitpunkt von **höchstens einem Thread** ausgeführt wird.

```c
#pragma omp critical (update_global_data)
{
    global_counter += local_counter;
}
```

### 3. Atomare Operationen (`#pragma omp atomic`)
Nutzt spezielle Hardware-Instruktionen (z. B. Compare-And-Swap oder Atomic Add) zur Aktualisierung einer einzelnen Speicherstelle. 

```c
#pragma omp atomic update
x += expr;
```

> [!TIP] Critical vs. Atomic
> `#pragma omp atomic` hat einen drastisch geringeren Overhead als `#pragma omp critical`, da keine schwerfälligen Mutex-Locks erzeugt werden, sondern direkte CPU-Hardware-Instruktionen zum Einsatz kommen.

---

## 3. Die OpenMP Lock API

Für komplexe, dynamische Datenstrukturen (z. B. Hash-Tabellen oder Bäume) bietet OpenMP eine explizite Lock-Schnittstelle:

* `omp_init_lock(omp_lock_t *lock)`: Initialisiert ein Lock.
* `omp_set_lock(omp_lock_t *lock)`: Blockiert, bis das Lock erworben wurde.
* `omp_unset_lock(omp_lock_t *lock)`: Gibt das Lock frei.
* `omp_test_lock(omp_lock_t *lock)`: Nicht-blockierender Versuch, das Lock zu erwerben (gibt 1 bei Erfolg, 0 bei Fehlschlag zurück).
* `omp_destroy_lock(omp_lock_t *lock)`: Gibt Ressourcen des Locks frei.
