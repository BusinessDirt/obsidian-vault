---
date: 2024-04-17T20:14
tags:
  - Informatik
  - Computerlinguistik
  - Mathe
cssclasses: 
aliases:
  - reguläre Ausdrücke
  - regulärer Ausdruck
---
## Definition
Die **regulären Ausdrücke** über einem Alphabet $\Sigma$ werden induktiv definiert:
1. **Basisfälle**:
	1. $\emptyset$ ist ein regulärer Ausdruck, beschreibt die **leere Sprache**
	2. $\epsilon$ ist ein regulärer Ausdruck, beschreibt die Sprache $\{ \epsilon \}$ 
		1. $\epsilon$ beschreibt das leere Wort
	3. Für jedes $a \in \Sigma$, ist $a$ ein regulärer Ausdruck für $\{ a \}$
2. Induktive Regeln:
	1. Vereinigung: $r+s$ beschreibt $L(r) \cup L(s)$
	2. Konkatenation: $rs$ beschreibt $L(r) \cdot L(s)$
	3. [[Kleene-Stern]]: $r^*$ beschreibt $L(r)^*$

## Beispiel
- Ausdruck: $(a+b)^*$
- Sprache: alle Wörter über $\{ a,b \}$ (inkl. $\epsilon$)
- Ausdruck: $a^*b$
- Sprache: alle Wörter mit null oder mehr `a`, gefolgt von genau einem `b`, z.B. `b`, `ab`, `aaab`