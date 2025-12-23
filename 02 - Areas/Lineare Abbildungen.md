---
date: 2024-10-16T16:17
tags:
  - Mathe
  - LinAlg
  - Analysis
---
Seien $V$ und $W$ $K$-[[Vektor#Vektorräume|Vektorräume]]. Eine [[Abbildungen|Abbildung]] $f:V \to W$ heißt lineare Abbildung oder Vektorraumhomomorphismus  genau dann, wenn gilt:
1) $\forall \vec{u},\vec{v} \in V: \quad f(\vec{u}+\vec{v}) = f(\vec{u}) + f(\vec{v})$
2) $\forall \lambda \in K : \quad f(\lambda \vec{v}) = \lambda f(\vec{v})$
Für die Menge der linearen Abbildungen $f$ von $V$ nach $W$ schreiben wir:
$$Hom(V, W) := \set{f:V \to W|f \space linear}$$
Alternativ bezeichnet man die Menge $Hom(V,W)$ auch als $\mathcal{L}(V,W)$.
Ist $f$ zusätzlich bijektiv, dann heißt $f:V \to W$ Vektorraumisomorphismus. In dem Fall sagen wir, $V$ und $W$ sind isomorph.

## Linearform, Dualraum
Sei $V$ ein $K$-[[Vektor#Vektorräume|Vektorraum]] und $f : V \to K$ eine lineare Abbildung. In diesem Fall nennt man $f$ Linearform, $1$-Form oder lineares Funktional auf $V$. Die Menge aller Linearformen auf $V$ bezeichnet man mit $V^*$. Man nennt $V^*$ den Dualraum von $V$.

## Lineares Gleichungssystem
Sei $x=(x_1, \dots, x_n) \in K^n, y = (y_1, \dots, y_n) \in K^m$. Ein lineares Gleichungssystem ist ein Gleichungssystem der folgenden Form:
$$\begin{matrix}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n & = & y_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n & = & y_2 \\
& \vdots & \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n & = & y_m
\end{matrix}$$
Man nennt das Gleichungssystem homogen, falls $y=0$, und inhomogen, falls $y \neq 0$.
