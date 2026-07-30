---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Speedup
  - Effizienz
  - Scaling
links: "[[Parallel and High Performance Computing]]"
---
## 1. Fundamentale Performancemetriken

Um die Güte und Leistungsfähigkeit eines parallelen Programms auf $p$ Prozessorkernen zu bewerten, werden standardisierte Kennzahlen verwendet.

### 1. Ausführungszeit (Execution Time)
* $T(1)$: Sequentielle Ausführungszeit des besten sequentiellen Algorithmus auf einem Prozessor.
* $T(p)$: Parallele Ausführungszeit des Programms auf $p$ Prozessoren.

### 2. Speedup (Beschleunigung)
Der **Speedup** $S(p)$ gibt an, um welchen Faktor die Ausführung durch die Verwendung von $p$ Prozessoren beschleunigt wird:

$$S(p) = \frac{T(1)}{T(p)}$$

* **Idealer (linearer) Speedup:** $S(p) = p$.
* **Sublinearer Speedup:** $S(p) < p$ (Der Regelfall aufgrund von Kommunikations- und Synchronisations-Overhead).
* **Superlinearer Speedup:** $S(p) > p$.

> [!TIP] Superlinearer Speedup
> Superlinearer Speedup entsteht in der Praxis meist durch **Cache-Effekte**: Durch die Aufteilung der Datenmenge auf $p$ Prozessoren passt das lokale Teilproblem plötzlich vollständig in den schnellen L1/L2-Cache jedes Prozessors, wodurch DRAM-Zugriffe wegfallen.

### 3. Parallele Effizienz (Efficiency)
Die **Effizienz** $E(p)$ misst die prozentuale Auslastung der eingesetzten Rechenressourcen:

$$E(p) = \frac{S(p)}{p} = \frac{T(1)}{p \cdot T(p)}$$

* Ideale Effizienz: $E(p) = 1.0$ (bzw. $100\%$).
* In der Praxis sinkt $E(p)$ mit steigender Prozessoranzahl $p$.

---

## 2. Skalierungsgesetze

### Amdahlsches Gesetz (Strong Scaling)
Amdahls Gesetz betrachtet ein **Problem fester Gesamtdatengröße** (Strong Scaling). 
Sei $s$ der sequentielle (nicht parallelisierbare) Anteil des Programms ($0 \le s \le 1$), und $(1-s)$ der perfekt parallelisierbare Anteil.

$$T(p) = s \cdot T(1) + \frac{(1-s)}{p} \cdot T(1)$$

Damit ergibt sich der **Amdahl-Speedup**:

$$S_{\text{Amdahl}}(p) = \frac{T(1)}{s \cdot T(1) + \frac{1-s}{p} \cdot T(1)} = \frac{1}{s + \frac{1-s}{p}}$$

Asymptotische Grenze für $p \to \infty$:

$$\lim_{p \to \infty} S_{\text{Amdahl}}(p) = \frac{1}{s}$$

> [!WARNING] Konsequenz von Amdahls Gesetz
> Selbst wenn $95\%$ eines Programms parallelisiert werden ($s = 0.05$), beträgt der maximale theoretische Speedup auf beliebig vielen Prozessoren **maximal 20**!

---

### Gustafsonsches Gesetz (Weak Scaling)
Gustafson argumentierte, dass man mit größeren Supercomputern nicht dieselben kleinen Probleme schneller löst, sondern **größere Probleme in derselben Zeit** berechnet (Weak Scaling).
Hier wächst der parallelisierbare Arbeitsaufwand proportional mit der Prozessoranzahl $p$.

Sei $s'$ der sequentielle Zeitanteil an der parallelen Gesamtlaufzeit. Der **Gustafson-Speedup** lautet:

$$S_{\text{Gustafson}}(p) = s' + p \cdot (1 - s') = p - s' \cdot (p - 1)$$

---

### Gegenüberstellung: Strong vs. Weak Scaling

| Kriterium | Strong Scaling (Amdahl) | Weak Scaling (Gustafson) |
| :--- | :--- | :--- |
| **Problemgröße** | **Konstant** | **Skaliert proportional mit $p$** |
| **Ziel** | Minimierung der Laufzeit für festes Problem | Maximierung der Problemgröße in fester Zeit |
| **Flaschenhals** | Sequentieller Anteil $s$ dominiert schnell | Kommunikations- & Netzwerk-Overhead |
| **Typischer Einsatz** | Interaktive Simulationen, Echtzeitsysteme | Klimamodelle, Big Data, Molekulardynamik |

---

## 3. Die Karp-Flatt-Metrik

Die **Karp-Flatt-Metrik** $e$ ermöglicht es, den tatsächlich gemessenen sequentiellen Overhead $e$ (inklusive Synchronisations- und Kommunikations-Overhead) experimentell aus Laufzeitmessungen abzuleiten:

$$e = \frac{\frac{1}{S(p)} - \frac{1}{p}}{1 - \frac{1}{p}}$$

* Wenn $e$ mit steigendem $p$ **konstant** bleibt: Der Leistungsverlust ist rein auf den sequentiellen Codeanteil zurückzuführen.
* Wenn $e$ mit steigendem $p$ **ansteigt**: Das System leidet unter wachsendem parallelem Overhead (z.B. Kommunikations-Engpässe oder Lock-Contention).
