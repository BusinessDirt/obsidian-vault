---
date: 2025-07-25T14:26
tags:
  - Informatik
  - Mathe
---
Zwei Wörter $x$ und $y$ sind nicht unterscheidbar in Bezug auf eine Sprache $L$, wenn sie sich nicht durch irgendeine Fortsetzung unterscheiden lassen. Wenn man also nicht entscheiden kann, ob ein Wort in $L$ ist, basierend auf dem Unterschied zwischen $x$ und $y$, dann gehören sie zur gleichen Äquivalenzklasse.

## Formale Definition
Für eine Sprache $L \subseteq \Sigma^*$
Definiere eine Relation $\equiv_{L}$ auf $\Sigma^*$ wie folgt:
$$x \equiv_{L} y \iff \forall z \in \Sigma^* : xz \in L \iff yz \in L$$
Das heißt: Zwei Wörter $x$ und $y$ sind äquivalent, wenn das Anhängen beliebiger Wörter $z$ entweder beide in $L$ oder beide nicht in $L$ liegen
Diese Relation ist eine Äquivalenzrelation (reflexiv, symmetrisch, transitiv)
→ Eine Sprache $L \subseteq \Sigma^*$ ist regulär genau dann, wenn die Äquivalenzrelation $\equiv_{L}$ nur endlich viele Äquivalenzklassen hat

## Beispiel
Sprache: $L = \{ a^nb^n \space | \space n \geq 0 \}$
Behauptung: $L$ ist nicht regulär
Beweisidee mit Myhill-Nerode:
- Betrachte die Wörter $x_{n}=a^n$
- Für jedes $x_n$ hängt davon ab, wie viele $a$’s es gibt, um mit gleich vielen $b$’s in $L$ zu sein
- Für $n \neq m$, gilt:
  $$x_{n}b^n \in L, \quad x_{m}b^n \notin L \quad \Rightarrow x_{n}\not\$$