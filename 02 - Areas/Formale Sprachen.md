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
3. $\left\{ a^{n}b^{n} | n \leq 3\right\}$