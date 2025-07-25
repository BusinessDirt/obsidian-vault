---
date: 2024-04-17T20:14
tags:
  - Informatik
  - Computerlinguistik
cssclasses: []
---
Formale Sprachen sind künstliche Sprachen, die es Computern ermöglichen, Daten und Informationen zu verarbeiten. Oft werden diese formalen Sprachen von [[Endliche Automaten|endliche Automaten]]verwaltet. Eine formale Sprache L besteht aus einer Menge von Wörtern, die wiederum aus Zeichen des Alphabets der Sprache bestehen. Das Alphabet  ist hierbei die Menge der Zeichen, die in einem Wort  benutzt werden dürfen, wie zum Beispiel die Buchstaben von A bis Z und Umlaute im deutschen Alphabet.
## Reguläre Sprachen
> Eine Sprache ist **regulär**, wenn sie von einem [[Endliche Automaten|endlichen Automaten]] (DFA oder NFA) erkannt werden kann oder durch einen [[Reguläre Ausdrücke|regulären Ausdruck]] beschrieben werden kann

### Eigenschaften
- Können mit deterministischen (DFA) oder nichtdeterministischen [[Endliche Automaten|endlichen Automaten]] (NFA) dargestellt werden
- Können durch [[Reguläre Ausdrücke|reguläre Ausdrücke]] beschrieben werden
- Sind geschlossen unter:
	- Vereinigung
	- Konkatenation
	- Kleene-Stern (`*`)
	- Durchschnitt
	- Komplement

### Beispiele
1. $\left\{ w \in \{ a,b \}* | \text{w enthält nur a und b}\right\}$
2. $\left\{ w \in \{ 0,1 \}* | \text{w enthält eine gerade Anzahl von 0en}\right\}$
3. $\left\{ a^{n}b^{n}\space |\space n \leq 3\right\}$ → endlich viele Wörter → regulär

## Nicht-reguläre Sprachen
> Eine Sprache ist **nicht-regulär**, wenn sie von **keinem** [[Endliche Automaten|endlichem Automaten]] erkannt werden kann 
> Sie ist zu “komplex” für einen endlichen Speicher

### Eigenschaften
- Erfordern mehr Speicher oder Struktur (z.B. einen Stack)
- Können **nicht** durch [[Reguläre Ausdrücke|reguläre Ausdrücke]] dargestellt werden
- Können **nicht** mit einem [[Endliche Automaten|endlichen Automaten]] akzeptiert werden.
- Oft analysiert mit dem [[Pumping-Lemma]] oder dem **Myhill-Nerode-Theorem**, um die Nicht-Regularität zu zeigen

### Beispiele
1. $\left\{ a^{n}b^{n}\space |\space n \geq 0\right\}$ → Man muss sich “merken”, wie viele 