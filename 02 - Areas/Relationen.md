---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
---
**Definition** Seien $X,Y$ Mengen, $R \subseteq X \times Y$. Das Tripel $R:= (X,Y,R)$ heißt (zweistellige) Relation zwischen (Elementen von) $X$ und (Elementen von) $Y$. Formal:
$$x \sim y :\Leftrightarrow (x,y) \in R$$
Statt $(X,Y,R)$ schreiben wir auch $(X,Y,\sim)$. Falls $Y=X$, spricht man von einer Relation auf $X$. In dem Fall schreibt man $(X,\sim)$ statt $(X,X,\sim)$.

## Äquivalenzrelation
Eine Relation $X, \sim)$ heißt Äquivalenzrelation, wenn gilt:
1) $\forall x \in X: \quad x \sim x$ (reflexiv)
2) $\forall x,y \in X: \quad x \sim y \Leftrightarrow y \sim x$ (symmetrisch)
3) $\forall x,y,z \in X: \quad x \sim y \land y \sim z \Rightarrow x \sim z$ (transitiv)
Die Äquivalenzrelation ist eine Abschwächung der Gleichheitsrelation. Insbesondere ist die Gleichheitsrelation selbst eine Äquivalenzrelation.

## Kongruenz modulo
Seien $x,y \in \mathbb{Z}$ und $m \in \mathbb{N}$. Die Relation
$$x \equiv {y\bmod{m}} \quad :\Leftrightarrow \quad m | (x-y)$$
heißt Kongruenz modulo. Wir sagen "$x$ kongruent $y$ modulo $m$"
## Äquivalenzklasse
Sei $(X, \sim)$ eine Äquivalenzrelation und $a \in X$. Die Menge
$$[a] := \{x \in X | x \sim a\}$$
heißt Äquivalenzklasse von $a$.
## Umkehrrelation
Sei $R = (X,Y,R)$ eine Relation. Das Tripel $R^{-1} := (X,Y,R^{-1})$ mit
$$R^{-1} = \{(y,x) \in Y \times X | (x,y) \in R\}$$
heißt Umkehrrelation.