---
date: 2026-04-09 11:02
tags:
  - Mathe
  - Pharmakologie
  - Physik
  - Statistik
  - Stochastik
---

## Formel
Für zwei Ereignisse $A$ und $B$ mit $P(B)>0$ lässt sich die Wahrscheinlichkeit von $A$ unter der Bedingung, dass $B$ eingetreten ist, durch die Wahrscheinlichkeit von $B$ unter der Bedingung, dass $A$ eingetreten ist, errechnen:

$$P(A∣B)=P(B∣A)⋅P(A)P(B)$$

> **Hierbei ist**
> _$P(A∣B)$_ die (bedingte) Wahrscheinlichkeit des Ereignisses _$A$_ unter der Bedingung, dass _$B$_ eingetreten ist,
> _$P(B∣A)$_ die (bedingte) Wahrscheinlichkeit des Ereignisses _$B$_ unter der Bedingung, dass _$A$_ eingetreten ist,
> _$P(A)$_ die A-priori-Wahrscheinlichkeit des Ereignisses _$A$_ und
> _$P(B)$_ die A-priori-Wahrscheinlichkeit des Ereignisses _$B$_.

**Bei endlich vielen Ereignissen lautet der Satz von Bayes:**
Wenn $A_{i},i=1,…,N$ eine Zerlegung der Ergebnismenge in disjunkte Ereignisse ist, gilt für die A-posteriori-Wahrscheinlichkeit $P(A_i∣B)$

$$P(A_i∣B)=\frac{P(B∣A_i)⋅P(Ai)}{P(B)}=\frac{P(B∣A_i)⋅P(A_i)}{\sum_{j=1}^{N}{P(B|A_{j})\cdot P(A_{j})}}$$

Den letzten Umformungsschritt bezeichnet man auch als _Marginalisierung_.

Da ein Ereignis $A$ und sein Komplement ${\displaystyle A^{\mathrm {c} }}$ stets eine Zerlegung der Ergebnismenge darstellen, gilt insbesondere

$${\displaystyle P(A\mid B)\;=\;{\frac {P(B\mid A)\cdot P(A)}{P(B\mid A)\cdot P(A)+P(B\mid A^{\mathrm {c} })\cdot P(A^{\mathrm {c} })}}}$$

Des Weiteren gilt der Satz auch für eine Zerlegung des Grundraumes ${\displaystyle \Omega }$ in abzählbar viele paarweise disjunkte Ereignisse.

## Interpretation

Siehe auch: [Beurteilung eines binären Klassifikators](https://de.wikipedia.org/wiki/Beurteilung_eines_bin%C3%A4ren_Klassifikators "Beurteilung eines binären Klassifikators")

Der Satz von Bayes erlaubt in gewissem Sinn das Umkehren von Schlussfolgerungen: Man geht von einem bekannten Wert ${\displaystyle P(B\mid A)}$ aus, ist aber eigentlich an dem Wert ${\displaystyle P(A\mid B)}$ interessiert. Beispielsweise ist es von Interesse, wie groß die Wahrscheinlichkeit ist, dass jemand eine bestimmte Krankheit hat, wenn ein dafür entwickelter Schnelltest ein positives Ergebnis zeigt. Aus empirischen Studien kennt man in der Regel die Wahrscheinlichkeit dafür, mit der der Test bei einer von dieser Krankheit befallenen Person zu einem positiven Ergebnis führt. Die gewünschte Umrechnung ist nur dann möglich, wenn man die Prävalenz der Krankheit kennt, das heißt die (absolute) Wahrscheinlichkeit, mit der die betreffende Krankheit in der Gesamtpopulation auftritt.

Für das Verständnis kann ein Entscheidungsbaum oder eine Vierfeldertafel helfen. Das Verfahren ist auch als Rückwärtsinduktion bekannt.

Mitunter begegnet man dem Fehlschluss, direkt von ${\displaystyle P(B\mid A)}$ auf ${\displaystyle P(A\mid B)}$ schließen zu wollen, ohne die A-priori-Wahrscheinlichkeit $P(A)$ zu berücksichtigen, beispielsweise indem angenommen wird, die beiden bedingten Wahrscheinlichkeiten müssten ungefähr gleich groß sein (siehe Prävalenzfehler). Wie der Satz von Bayes zeigt, ist das aber nur dann der Fall, wenn auch $P(A)$ und $P(B)$ ungefähr gleich groß sind.

Ebenso ist zu beachten, dass bedingte Wahrscheinlichkeiten für sich allein nicht dazu geeignet sind, eine bestimmte Kausalbeziehung nachzuweisen.