# Symbole
- **Terminale**: Wörter wie zum Beispiel "Buch"
- **Nicht-Terminale**: [[Syntax|syntaktische]] Label wie "NP" oder "NN"

# Productions (rules)
$W \to XYZ$
- Exakt ein Nicht-Terminal auf der linken Seite
- Eine geordnete Liste an Symbolen auf der rechten Seite
	- Terminale und Nicht-Terminale

# Startsymbol
- meistens "S" genannt (= Satz Knoten bzw. die [[Baum#Wurzel|Wurzel]])

# [[Reguläre Ausdrücke]] als CFGs
Beispielsweise ein [[Reguläre Ausdrücke|regulärer Ausdruck ]] der Wörter die mit einem Großbuchstaben beginnen definiert: $[A-Z][a-z]*$
Kann als Grammatik umgeschrieben werden:
- $\text{S} \to \text{U} \qquad \text{S} \to \text{U LS}$
- $\text{U} \to \text{"A"} \qquad \text{U} \to \text{"B"} \dots \qquad \text{U} \to \text{"Z"}$
- $\text{LS} \to \text{L} \qquad \text{LS} \to \text{L LS}$
- $\text{L} \to \text{"a"} \qquad \text{L} \to \text{"b"} \dots \qquad \text{L} \to \text{"z"}$
