---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
  - LinAlg
---
**Definition**: Wir nennen eine [[Relationen|Relation]] $f = (X,Y,R)$ eine Abbildung oder Funktion genau dann, wenn gilt:
$$\forall x \in X \quad \exists! \quad y \in Y : (x,y) \in R$$
Hier bedeutet $\exists!$: "es existiert genau ein". Wir nennen $y$ den Funktionswert von $f$ an der Stelle $x$ und schreiben $x = f(x)$. Statt $f = (X,Y,R)$ schreiben wir $f: X \to Y$. Wir nennen $X$ den Definitionsbereich, $Y$ den Wertebereich und $R = G_f$ den Graph von $f$.
$D(f) := X$: Definitionsbereich (domain) von $f$
$F(f) := Y$: Wertebereich (range) von $f$

## Identität, Einbettung, Einschränkung
Sei $X$ eine Menge. Die Abbildung
$$id_x : X \to X, \quad x \to x$$
heißt Identität. Sei $A \subseteq X$. Die Abbildung
$$i_A : A \to X, \quad x \to x$$
heißt Einbettung (Inklusion) von $A$ in $X$. Sei $Y$ eine Menge, $f : X \to Y$ eine Funktion. Die Abbildung
$$f|_A: \quad A \to Y, \quad x \to x$$
heißt Einschränkung (Restriktion) von $f$ auf $A$
## Bild, Urbild
Sei $f: X \to Y$ eine Abbildung, $A \subseteq X, B \subseteq Y$. Die Menge
$$f(A) := \{f(x)|x \in A\} = \{y \in Y| \exists y \in B : f(x) = y\}$$
heißt Bild von $A$ unter $f$. Die Menge
$$f^{-1}(B):=\{x \in X | f(x) \in B\} = \{x \in X | \exists y \in B : f(x) = y\}$$
heißt Urbild von $B$ unter $f$.

## Verkettung
Seien $f: X \to Y$ und $g: Y \to Z$ Abbildungen. Dann heißt die Abbildung $X \to Z, x \to g(f(x))$ Verkettung von $g$ und $f$. Wir schreiben dafür $g \circ f$. 

## Injektivität, Sujektivität, Bijektivität
Sei $f: X \to Y$ eine Abbildung. $f$ heißt
- $injektiv \Leftrightarrow \forall x, x' \in X : x \neq x' \Rightarrow f(x) \neq f(x')$
	- auch eindeutig; jedes $y \in Y$ hat höchstens ein Urbild
- $surjektiv \Leftrightarrow \forall y \in Y: \exists x \in X$ mit $y = f(x)$ (oder kurz: $f(X) = Y$)
	- jedes $y \in Y$ hat mindestens ein Urbild
- $bijektiv \Leftrightarrow f$ injektiv und surjektiv

## Umkehrfunktionen
Eine Abbildung $g: Y \to X$ heißt Umkehrabbildung oder Umkehrfunktion von $f:X \to Y$ genau dann, wenn gilt:
1) $g \circ f = id_X$,   d.h.   $g(f(x))=x \quad \forall x \in X$
2) $f \circ g = id_Y$,   d.h.   $f(g(y))=y \quad \forall y \in Y$
Wir schreiben dann: $g =: f^{-1}$

## Geordnetes Paar
Sei $x \in A, y \in B$. Dann heißt
$$(x,y) := \left\{ \{ x \}, \{ x,y \}\right\}$$
das geordnete Paar aus $x$ und $y$.

## Kartesisches Produkt

$$x \in A, y \in B \qquad A \times B := \{ (x,y) : x \in A \land y \in B
\}$$