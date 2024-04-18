Der [[Vektor#Vektorräume|Vektorraum]] $\mathbb{R}^n$ mit darauf definiertem Skalarprodukt ist ein euklidischer Vektorraum.

## Skalarprodukt
Seien $x,y \in \mathbb{R}^n$. Wir nennen
$$\langle x,y\rangle := \sum_{i=1}^n{x_{i}y_{i}}$$
das Skalarprodukt von $x$ und $y$. Wir schreiben auch: $\langle x,y \rangle := x^T y$.
## Orthogonalität
Seien $x,y \in \mathbb{R}^n$. Falls
$$\langle x,y \rangle = 0$$
## Länge, Abstand
Sei $x \in \mathbb{R}^n$. Wir nennen
$$|x| := \sqrt{ \langle x,y \rangle } = \sqrt{ \sum_{i=1}^n{x_{i}^2} }$$
die euklidische Norm oder Länge von $x$. Alternativ schreiben wir: $|x| = ||x||_{2}$. Mit der euklidischen Norm können wir auf den Abstand $d(X,Y)$ zwischen zwei Punkten $X,Y \in \mathbb{R}^n$ definieren:
$$d(X,Y) := |x-y| = \sqrt{ \langle x-y,x-y \rangle } = \sqrt{ \sum_{i=1}^{n}{(x_{i} - y_{i})^2} }$$
### Eigenschaften der Norm
Die Abbildung $\mathbb{R}^n \rightarrow \mathbb{R}, x \rightarrow |x|$ ist definit, absolut homogen und erfüllt die Dreiecksgleichung.
1) Für $x \in \mathbb{R}^n: \quad |x| = 0 \Leftrightarrow x = 0$
2) Für $x \in \mathbb{R}^n \space und \space \lambda \in \mathbb{R}: \quad |\lambda x| = |\lambda| \cdot |x|$
3) Für $x,y \in \mathbb{R}^n: \quad |x+y| \leq |x| + |y|$

## Winkel
Seien $x,y \in \mathbb{R}^2 \setminus \{ 0 \}$. Wir nennen $\phi \in [0, \pi]$ mit
$$\cos{\phi} = \frac{{\langle x,y \rangle}}{|x| \cdot |y|} \quad \left( \text{bzw.} \quad \phi=\arccos{\frac{\langle x,y \rangle}{|x| \cdot |y|}} \right)$$
## Orthonormalsystem, Orthonormalbasis
Gegeben eine endliche Menge von Vektoren $\{ b_{1}, \dots, b_{m} \}$ mit $x_{i} \in \mathbb{R}^n$ für alle $i=1, \dots, m$ $(m < n, m,n \in \mathbb{N})$. Falls
$$\langle b_{i}, b_{j} \rangle = \delta_{ij} = \biggl\{\begin{matrix}
1 & falls & i = j \\
0 & falls & i \neq j
\end{matrix}$$
so nennen wir $\{ b_{1}, \dots, b_{m} \}$ ein Orthonormalsystem (kurz ONS). Ist $n = m$, so nennen wir $\{ b_{1}, \dots, b_{m} \}$ eine Orthonormalbasis (kurz ONB) des $\mathbb{R}^m$.

