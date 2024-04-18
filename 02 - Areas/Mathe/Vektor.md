- Ein Vektor ist eine Wegbeschreibung von einem Punkt $A$ zu einem anderen Punkt $B$
- Verwendung in der Mathematik und der [[Informatik]]

## Lineare Unabhängigkeit
Es sei $V$ ein Vektorraum über einem [[Gruppen, Ringe, Körper#Körper|Körper]] $K$. Die Vektoren $\vec{v_1}, \vec{v_2}, \dots , \vec{v_n}$ aus $V$ heißen linear unabhängig, wenn die einzig möglich Darstellung des Nullvektors als Linearkombination
$$a_1\vec{v_1} + a_2\vec{v_2} + \cdots + a_n\vec{v_n} = \vec{0}$$
mit Koeffizienten $a_1, a_2, \dots , a_n$ aus dem Grundkörper $K$ diejenige ist, bei der alle Koeffizienten $a_i$ gleich null sind. Lässt sich dagegen der Nullvektor auch nichttrivial (mit Koeffizienten ungleich null) erzeugen, dann sind die Vektoren linear abhängig.

# Vektorräume
**Definition**: Sei $K$ ein [[Gruppen, Ringe, Körper#Körper|Körper]]. Eine [[Mengenlehre|Menge]] $V$ mit zwei [[Gruppen, Ringe, Körper#Gruppen#Verknüpfung|Verknüpfungen]]
i) $+:V \times K \to V, \space (\vec{v},\vec{w}) \to \vec{v} + \vec{w}$ (Vektoraddition)
ii) $\cdot : K \times V \to V, \space (\lambda ,\vec{v}) \to \lambda \cdot \vec{v}$ (skalare Multiplikation)
heißt Vektorraum über $K$ oder $K$-Vektorraum genau dann, wenn gilt:
1. $(V,+)$ ist eine kommutative Gruppe
2. $\forall \lambda \in K$ und $\vec{v}, \vec{w} \in V$:  $\lambda \cdot (\vec{v} + \vec{w}) = \lambda \cdot \vec{v} + \lambda \cdot \vec{w}$
3. $\forall \lambda , \mu \in K$ und $\vec{v} \in V$:  $(\lambda + \mu) \cdot \vec{v} = \lambda \cdot \vec{v} + \mu \cdot v$
4. $\forall \lambda , \mu \in K$ und $\vec{v} \in V$:  $(\lambda \cdot \mu) \cdot \vec{v} = \lambda \cdot (\mu \cdot \vec{v})$
5. $\forall \vec{v} \in V$: $1 \cdot \vec{v} = \vec{v}$

## Lineare Hülle
Sei $m \in \mathbb{N}$. Sei $V$ ein $K$-Vektorraum und $b_{1}, \dots,b_{m} \in V$. Man bezeichnet die Menge der Linearkombinationen von $b_{1}, \dots, b_{n}$,
$$span(b_{1}, \dots, b_{m}) = \left\{\sum_{i=1}^{m}{\lambda_{i}b_{i}} | \lambda_{i} \in K \quad \forall i = 1,\dots,m\right\}$$
als lineare Hülle oder Spann von $b_{1}, \dots, b_{m}$.

## Erzeugendensystem
Weiter heißt $b_{1}, \dots, b_{m}$ Erzeugendensystem von $V$ genau dann, wenn
$$span(b_{1}, \dots, b_{m}) = V$$
Existiert ein Erzeugendensystem $V$, so sagen wir, $V$ ist endlich erzeugt.
## Basis
Sei $V$ ein $K$-Vektorraum, $m \in \mathbb{N}$ und $b_{1}, \dots, b_{m} \in V$. Die Vektoren $b_{1}, \dots, b_{m}$ heißen Basis von $V$ genau dann, wenn $b_{1}, \dots, b_{m}$ linear unabhängig sind und ein Erzeugendensystem von $V$ bilden.

## Untervektorräume
Sei $V$ ein $K$-Vektorraum. Eine nicht-leere [[Mengenlehre#Mengen|Menge]] $U \subseteq V$ heißt Untervektorraum von $V$ genau dann, wenn gilt:
1) $\forall \vec{v}, \vec{w} \in U: \quad \vec{v} + \vec{w} \in U$
2) $\forall \lambda \in K, \vec{v} \in U: \quad \lambda \cdot \vec{v} \in U$

## Kern, Bild
Seien $V$ und $W$ $K$-Vektorräume. Sei $f: V \to W$ eine [[Lineare Abbildungen|lineare Abbildung]]. Dann bezeichnen wir als Kern von $f$ die [[Mengenlehre#Mengen|Menge]]
$$Kern{f} := \set{v \in V | f(v) = 0}$$
Als Bild von $f$ bezeichnen wir die [[Mengenlehre#Mengen|Menge]]
$$Bild{f} := f(V)$$