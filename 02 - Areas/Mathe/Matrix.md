($m \times n$ Matrix über $K, K^{m\times n}$). Seien $m,n \in \mathbb{N}$ und $a_{ij} \in K$ für $i=1,\dots, m$ und $j = 1,\dots, n$. Das rechteckige Schema mit $m$ Zeilen und $n$ Spalten

$$A={\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &&\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\\\end{pmatrix}}$$
heißt $m \times n$ Matrix (über $K$). Wir schreiben kurz: $A=(a_{ij})_{i=1,\dots,m;j=1,\dots,n}$.
Die [[Mengenlehre#Mengen|Menge]] aller $m \times n$ Matrizen über $K$ wird mit $K^{m \times n}$ bezeichnet.
$a_j := \begin{pmatrix} a_{1j} \\ \vdots \\ a_{mj}\end{pmatrix} = (a_{ij})_{i=1,\dots,m} \in K^{m\times 1}$ heißt $j$-te Spalte von $A$ 
$a^i := (a_{i1} \enspace \cdots \enspace a_{in}) = (a_{ij})_{j=1,\dots,n} \in K^{1\times n}$ heißt $i$-te Zeile von $A$ 

## Matrizenaddition, skalare Multiplikation
Seien $m, n \in \mathbb{N}$. Sei $K$ ein [[Gruppen, Ringe, Körper#Körper|Körper]]. Seien $A=(a_{ij})_{i=1,\dots,m;j=1,\dots,n}$, $B=(b_{ij})_{i=1,\dots,m;j=1,\dots,n}$ $\in K^{m \times n}, \space \lambda \in K$. Wir definieren:
1) $A + B := (a_{ij} + b_{ij})_{i=1,\dots,m;j=1,\dots,n} \quad$ (Matrizenaddition)
2) $\lambda A := (\lambda a_{ij})_{i=1,\dots,m;j=1,\dots,n} \quad$ (skalare Multiplikation)

# Matrizenmultiplikation
Seien $m,n,p \in \mathbb{N}$. Sei $K$ ein [[Gruppen, Ringe, Körper#Körper|Körper]]. Seien $A=(a_{ij})_{i=1,\dots,m;j=1,\dots,n} \in K^{m \times n}$, $B=(b_{jk})_{j=1,\dots,n;k=1,\dots,p} \in K^{n \times p}$. Wir definieren:
$$A \cdot B := \left( \sum_{j=1}^{n}{a_{ij}b_{jk}} \right)_{i=1,\dots,n;k=1,\dots,p} \in K^{m \times p}$$
## Transponierte Matrix
Seien $m,n \in \mathbb{N}$. Sei $K$ ein [[Gruppen, Ringe, Körper#Körper|Körper]] und die Matrix $A=(a_{ij})_{i=1,\dots,m;j=1,\dots,n} \in K^{m \times n}$. Wir nennen
$$A^T := (a_{ji})_{j=1,\dots,m;i=1,\dots,n} \in K^{n \times m}$$
Die zu $A$ transponierte Matrix
> Die Zeilen von $A^T$ sind also die Spalten von $A$ und umgekehrt

## Inverse Matrix
Sei $n \in \mathbb{N}$. Sei $K$ ein [[Gruppen, Ringe, Körper#Körper|Körper]] und $A \in K^{n \times n}$. $A$ heißt invertierbar, wenn $A^{-1} \in K^{n \times n}$ existiert mit
$$A \cdot A^{-1} = A^{-1} \cdot A = E_{n}$$
$A^{-1}$ ist eindeutig definiert und heißt inverse Matrix zu $A$