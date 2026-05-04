---
date: 2026-04-09 11:02
tags:
  - Mathe
  - Statistik
  - Stochastik
  - Wahrscheinlichkeit
---

## 1. Definition und Grundlagen
Eine **Zufallsvariable (ZV)** $X$ ist formal eine [[Abbildungen|Abbildung]] von der Ergebnismenge $\Omega$ eines Zufallsexperiments in die reellen Zahlen $\mathbb{R}$:
$$X: \Omega \rightarrow \mathbb{R}$$
Anstatt mit abstrakten Ergebnissen zu hantieren, rechnen wir direkt mit den Realisierungen $x \in \mathbb{R}$. Der Bereich aller möglichen Werte, die $X$ annehmen kann, wird als **Träger $\mathcal{T}$** bezeichnet.
## 2. Diskrete Zufallsvariablen
Eine Zufallsvariable heißt **diskret**, wenn ihr Träger $\mathcal{T}$ nur aus endlich vielen oder abzählbar unendlich vielen Werten $\{x_1, x_2, \dots\}$ besteht.

### Wahrscheinlichkeitsfunktion (Zähldichte)
Jedem Wert $x_i$ im Träger wird eine Wahrscheinlichkeit zugeordnet:
$$f(x_i) = P(X = x_i)$$
**Eigenschaften:**
- $f(x) \ge 0$ für alle $x$.
- $\sum_{x_i \in \mathcal{T}} f(x_i) = 1$ (Normierungseigenschaft).

### Verteilungsfunktion
Die Verteilungsfunktion $F(x)$ gibt die kumulierte Wahrscheinlichkeit an:
$$F(x) = P(X \le x) = \sum_{i: x_i \le x} f(x_i)$$
> [!INFO] Formhinweis
> Bei diskreten ZV ist $F(x)$ eine **Treppenfunktion**, die an den Stellen $x_i$ nach oben springt.
## 3. Stetige Zufallsvariablen
Eine Zufallsvariable heißt **stetig**, wenn sie jeden beliebigen Wert in einem Intervall (oder einer überabzählbaren Menge) annehmen kann.
### Wahrscheinlichkeitsdichte
Da die Wahrscheinlichkeit für einen exakten Punkt $P(X = x) = 0$ ist, nutzen wir eine **Dichtefunktion** $f(x)$. Wahrscheinlichkeiten entsprechen Flächen unter dieser Kurve:
$$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx$$
### Verteilungsfunktion
Die Verteilungsfunktion ist das Integral über die Dichte von links bis zum Punkt $x$:
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(u) \, du$$
An allen Stellen, an denen $f(x)$ stetig ist, gilt der Zusammenhang: $F'(x) = f(x)$.
## 4. Vergleichstabelle

| Merkmal                 | Diskrete ZV                 | Stetige ZV                               |
| :---------------------- | :-------------------------- | :--------------------------------------- |
| **Wertebereich**        | Abzählbar (einzelne Punkte) | Überabzählbar (Intervalle)               |
| **Punkt-W'keit**        | $P(X=x) = f(x)$             | $P(X=x) = 0$                             |
| **Summen/Integrale**    | $\sum f(x_i) = 1$           | $\int_{-\infty}^{\infty} f(x) \, dx = 1$ |
| **Verteilungsfunktion** | Treppenfunktion             | Stetig differenzierbar                   |
