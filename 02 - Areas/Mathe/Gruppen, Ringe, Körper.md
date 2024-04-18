# Gruppen
## Verknüpfung
Sei $M$ eine Menge. Eine Verknüpfung $\circ$ auf $M$ ist eine Abbildung $\circ : M \times M \to M,(a,b) \to a \circ b$.
## Definition
Eine Menge $G$ mit einer Verknüpfung $\circ$ heißt Gruppe $(G, \circ)$ genau dann, wenn gilt:
1) $\forall a,b,c \in G : (a \circ b) \circ c = a \circ (b \circ c)$ (Assoziativgesetz)
2) $\exists e \in G$, sodass $\forall a \in G : a \circ e = e \circ a = a$ (Existenz eines neutralen Elements)
3) $\forall a \in G \exists a^{-1} \in G: a \circ a^{-1} = a^{-1} \circ a = e$ (Existenz eines inversen Elements zu $a$)
$(G, \circ)$ heißt abelsche oder kommutative Gruppe, wenn zusätzlich gilt:
4) $\forall a,b \in G: a \circ b = b \circ a$ (Kommutativgesetz)

## Permutationsgruppe
Sei $M = \{1, \dots, n\}$. Man nennt die Menge der bijektiven Abbildungen auf $M$, i.e. $S_n := \{\phi: M \to M \space bijektiv\}$, zusammen mit der Funktionsverkettung $\circ$ die Permutationsgruppe.
	Die bijektiven Abbildungen $\phi:\{1,\dots,n\} \to \{1, \dots, n\},i \to \phi(i)$ nennt man Permutationen

## Homomorphismus, Isomorphismus, Automorphismus
Seien $(G, \circ)$ und $(H, \star)$ Gruppen. Eine Abbildung $\phi : G \to H$ heißt
1) Homomorphismus genau dann, wenn $\forall a,b \in G: \phi(a \circ b) = \phi(a) \star \phi(b)$
2) Isomorphismus genau dann, wenn $\phi$ Homomorphismus und $\phi$ bijektiv ist. In dem Fall nennen wir $(G, \circ)$ und $(H, \star)$ isomorphe Gruppen.
	1) Man bezeichnet zwei isomorphe Strukturen $S$ und $S'$ (Gruppen, Körper, [[Vektor#Vektorräume|Vektorräume]]) als "strukturgleich" und schreibt: $S \cong S'$
3) Ist $\phi: G \to G$ ein Isomorphismus einer Gruppe $G$ auf sich selbst, dann nennen wir $\phi$ einen Automorphismus
	1) Jede Struktur $S$ hat einen trivialen Automorphismus, die Identität $id:x \to x$. Vorwegnahme: Tatsächlich gibt es auf den Körpern $\mathbb{Q}$ und $\mathbb{R}$ nur den trivialen Automorphismus, erst auf $\mathbb{C}$ gibt es einen nichttrivialen Automorphismus, nämlich die [[Komplexe Zahlen#Komplexe Konjugation|komplexe Konjugation]] $z = x+iy \to \overline{z} = x - iy$.

# Ringe
**Definition**: Sei $R$ eine Menge mit zwei Verknüpfungen:
i) $+:R \times R \to R, \quad (a,b) \to a+b \quad$ ("Addition")
ii) $\cdot :R \times R \to R, \quad (a,b) \to a \cdot b \quad$ ("Multiplikation")
$(R,+,\cdot)$ heißt Ring genau dann, wenn gilt:
1) $(R,+)$ ist eine kommutative Gruppe
2) Die Multiplikation $\cdot$ ist assoziativ (oder äquivalent: $(R, \cdot)$ ist "Halbgruppe"), d.h. es gilt $\forall a,b,c \in R : (a \cdot b) \cdot c = a \cdot (b \cdot c)$
3) Es gelten die Distributivgesetze, d.h. $\forall a,,b,c \in R : (a+b) \cdot c = (a \cdot c) + (b \cdot c)$ und $c \cdot (a+b) = (c \cdot a) + (c \cdot b)$
$(R,+,\cdot)$  heißt kommutativer Ring, wenn zusätzlich gilt:
4) $\forall a,b \in R: a \cdot b = b \cdot a$

## Einselement
Sei $(R,+,\cdot)$ ein Ring. Ein neutrales Element der Multiplikation $e \in R$ heißt Einselement. Statt $e$ schreiben wir in dem Fall $1$ und dann gilt $\forall a \in R$:
$$1 \cdot a = a \cdot 1 = a$$
## Nullteilerfrei
Sei $(R, +, \cdot)$ ein Ring. Wir nennen $R$ nullteilerfrei genau dann, wenn $\forall a,b \in R$ gilt:
$$a \cdot b = 0 \Rightarrow a = 0 \lor b = 0$$

# Körper
$(K,+,\cdot)$ heißt Körper genau dann, wenn gilt:
1) $(K,+,\cdot)$ ist ein Ring
2) $(K \setminus \set{0}, \cdot)$ ist eine kommutative Gruppe
Für das neutrale Element der Multiplikation schreiben wir $1$. Für das inverse Element der Multiplikation zu $a$ schreiben wir $\frac{1}{a}$ oder $a^{-1}$. Damit können wir die Division definieren als $\frac{a}{b} := a \cdot \frac{1}{b} = a \cdot b^{-1}$.

## Körper der komplexen Zahlen
![[Komplexe Zahlen]]