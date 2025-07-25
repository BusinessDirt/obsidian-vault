---
date: 2025-07-25T11:29
tags:
  - Informatik
---
> Das **Pumping-Lemma** ist ein **Beweiswerkzeug**, um zu zeigen, dass **eine [[Formale Sprachen|Sprache]] nicht regulär** ist

## Idee
Wenn eine Sprache regulär ist, dann gibt es eine maximale “Pumping-Länge” $p$, sodass **alle langen Wörter** aus der Sprache in 3 Teile aufgeteilt werden können:
$$w=xyz$$
mit folgenden Eigenschaften:
1. $|xy|\leq p$
2. $|y|>0$ ($y$ ist nicht leer)
3. Für alle $i \geq 0: xy^iz \in L$

### Bedeutung
Man kann den mittleren Teil $y$ beliebig oft wiederholen, und das neue Wort bleibt immer noch in der Sprache - **wenn die Sprache regulär ist**

## Beispiel
Sprache: $L = \{ a^n b^n \mid n \geq 0 \}$
**Behauptung**: $L$ ist nicht regulär.
**Beweisidee mit Pumping-Lemma**:
- Angenommen, $L$ ist regulär → es gibt ein Pumping-Lemma mit Länge $p$
- Wähle $w=a^pb^p \in L$
- Zerlege: $w=xyz$, wobei $|xy|\leq p$ und $|y|\geq 0$
	- Beispielhaft: $x= a^k$, $y=a^m$ ($m>0$), $z=a^{p-k-m}b^p$
- Pumpen (z.B. $i=2$): $xy^{2}z=a^ka^{2m}a^{p-k-m}b^p=a^{p+m}b^p$
- → $xy^2z \notin L$, Wiederspruch da mehr a’s als b’s
→ $L$ ist nicht regulär