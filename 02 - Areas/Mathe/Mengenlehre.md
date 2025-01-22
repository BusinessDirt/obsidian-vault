---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
  - LinAlg
---
# Cantor
"Eine Menge $M$ ist die Zusammenfassung zu einem Ganzen von wohlunterschiedenen Objekten $m$ unserer Anschauung oder unseres Denkens".
-> $m$ sind die Elemente von $M$
-> Nicht frei von Wiedersprüchen (z.B. die [[Russellsche Antinomie]]), die in der axiomatischen Mengenlehre vermieden werden

# Mengen
## Leere Menge
**Definition**: Die Menge ohne Elemente heißt leere Menge, Symbol: $\emptyset$
## Gleichheit
Zwei Mengen $A$ und $B$ sind gleich, wenn sie dieselben Elemente enthalten:
$$A = B \Leftrightarrow \forall x: x \in A \Leftrightarrow x \in B$$
## Teilmenge
$A$ ist eine Teilmenge von $B$, wenn alle Elemente, die in $A$ enthalten sind, auch in $B$ enthalten sind:
$$A \subseteq B \Leftrightarrow \forall x: x \in A \Rightarrow x \in B$$
## Potenzmenge
Als Potenzmenge $P(A)$ bezeichnen wir die Menge aller Teilmengen von $A$,
$$P(A) = \{M | M \subseteq A\}$$
**Beispiel** Sei $A = \{1, 2, 4\}$.
$$P(A) = P(\{1, 2, 4\}) = \{\emptyset, \{1\}, \{2\}, \{4\}, \{1, 2\}, \{1, 4\}, \{2, 4\}, \{1, 2, 4\}\}$$
## Differenz
Die Differenz $B \setminus A$ der Mengen $B$ und $A$ ist die Menge aller Elemente, die in $B$, aber nicht in $A$ liegen:
$$B \setminus A = \{x | x \in B \land x \notin A\} = \{x \in B | x \notin A\}$$
Ist $A$ eine Teilmenge von $B$, dann nennen wir $B \setminus A$ das Komplement von $A$ in $B$. Ist $B$ eine nicht eigens zu spezifizierende Grundmenge (im Allgemeinen $\Omega$ genannt), dann schreiben wir für das Komplement $A^c$
## Schnitt
Der Schnitt der Mengen $A$ und $B$ ist die Menge aller Elemente, die in $A$ und $B$ liegen:
$$A \cap B = \{x | x \in A \land x \in B\} = \{x \in A \ x \in B\}$$
Ist $A \cap B = \emptyset$, so nennen wir $A$ und $B$ disjunkt.
## Vereinigung
Die Vereinigung der Mengen $A$ und $B$ ist die Menge aller Elemente, die in $A$ oder $B$ liegen:
$$A \cup B = \{x | x \in A \lor x \in B\}$$
## Endliche Menge
Eine Menge $A$ heißt endlich, wenn sie nur endlich viele Elemente enthält. Wir bezeichnen die Anzahl der Elemente mit $|A|$.
**Beispiel** Seit $A = \{1, 2, 4, 7, 9\}$. Dann ist $|A|=5$

# Unendliche Mengen
## Gleichmächtigkeit
Eine Menge $M$ heißt gleichmächtig zu einer anderen Menge $N$ genau dann, wenn eine bijektive Abbildung $\phi: M \to N$ existiert. Wir schreiben dann:
$$|M|=|N|$$
## Endliche, abzählbar und überabzählbar unendliche Mengen
Sei $M$ eine nicht-leere Menge und $n \in \mathbb{N}$. Dann gilt:
1) $|\emptyset| = 0$
2) $M$ hat $n$ Elemente, $|M| = n \Leftrightarrow \exists \phi: \{1, \dots, n\} \to M$ bijektiv
3) $M$ heißt $endlich$ $\Leftrightarrow \exists n \in \mathbb{N}$ mit $|M| = n$ (sonst heißt $M$ unendlich)
4) $M$ heißt $abzählbar$ $unendlich$ $\Leftrightarrow M$ gleichmächtig zu $\mathbb{N}$
5) $M$ heißt $überabzählbar$ $unendlich$, falls $M$ nicht endlich und $M$ nicht abzählbar unendlich ist

## Primzahl
$p$ ist Primzahl $: \Leftrightarrow p \in \mathbb{N}, p \geq 2$ und $\forall a \in \mathbb{N} : a|p \Rightarrow a = 1 \lor a = p$.