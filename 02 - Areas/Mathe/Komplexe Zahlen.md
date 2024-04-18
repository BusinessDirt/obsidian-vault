Eine komplexe Zahl $z$ ist ein Paar $z = (x,y)$ reeller Zahlen $x,y \in \mathbb{R}$. Die Menge $\mathbb{C} = \set{(x,y)|x,y \in \mathbb{R}} = \mathbb{R}^2$ mit den [[Gruppen, Ringe, Körper#Verknüpfung|Verknüpfungen]]
$$+ \quad :\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2, \quad (x_1, y_1) + (x_2, y_2) := (x_1 + x_2, y_1 + y_2)$$
$$\cdot \quad :\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2, \quad (x_1, y_1) \cdot (x_2, y_2) := (x_1 \cdot x_2 - y_1 \cdot y_2, x_1 \cdot y_2 + x_2 \cdot y_1)$$
wird als Körper der komplexen Zahlen bezeichnet.
## Imaginäre Einheit
Wie definieren die imaginäre Einheit $i := (0,1)$
## Real- und Imaginärteil
Sei $z = x+iy \in \mathbb{C}$. Dann definieren wir wie folgt:
1) $Rez := x \quad$ (Realteil von $z$)
2) $Im z := y \quad$ (Imaginärteil von $z$)
## Komplexe Konjugation
Sei $z = x+iy \in \mathbb{C}$. Dann ist die komplex konjugierte Zahl $\overline{z}$ wie folgt definiert:  
$$\overline{z} := x -iy$$
## Betrag
Sei $z = x+iy \in \mathbb{C}$. Dann ist Betrag $|z|$ wie folgt definiert:  
$$|z| := \sqrt{x^2 + y^2}$$
## Polardarstellung
Geometrisch kann man die komplexen Zahlen als [[Vektor|Vektoren]] in der Zahlenebene $\mathbb{R}^2$ (siehe [[Euklidischer Vektorraum]]) auffassen, wobei auf der "$x-Achse$" der Realteil von $z$, auf der "$y-Achse$" der Imaginärteil von $z$ angetragen wird (die "$y-Achse$") trägt demnach die imaginäre Einheit $i$).
Die [[Euklidischer Vektorraum#Länge, Abstand|Länge des Vektors]] ist gegeben durch den Betrag $r := |z| = \sqrt{ x^2 + y^2 }$ und der [[Euklidischer Vektorraum#Winkel|Winkel]], unter dem der [[Vektor]] angetragen wird, durch $\phi := \arctan{\frac{y}{x}}$. Daraus ergibt sich die sog. Polardarstellung der komplexen Zahlen mit Polarkoordinaten $r$ und $\phi$:
$$z=x+iy=r \cos{\phi} + ir \sin{\phi} = re^{i \phi}$$
Hier haben wir im letzten Schritt die Eulersche Formel $e^{i \phi} = \cos{\phi} + i \sin{\phi}$
