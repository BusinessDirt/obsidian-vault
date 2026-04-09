---
date: 2026-04-09 11:02
tags:
  - Stochastik
  - Statistik
---
## Formel
Für zwei Ereignisse $A$ und $B$ mit $P(B)>0$ lässt sich die Wahrscheinlichkeit von $A$ unter der Bedingung, dass $B$ eingetreten ist, durch die Wahrscheinlichkeit von $B$ unter der Bedingung, dass $A$ eingetreten ist, errechnen:

$$P(A∣B)=P(B∣A)⋅P(A)P(B)$$

> **Hierbei ist**
> _$P(A∣B)$_ die (bedingte) Wahrscheinlichkeit des Ereignisses _$A$_ unter der Bedingung, dass _$B$_ eingetreten ist,
> _$P(B∣A)$_ die (bedingte) Wahrscheinlichkeit des Ereignisses _$B$_ unter der Bedingung, dass _$A$_ eingetreten ist,
> _$P(A)$_ die A-priori-Wahrscheinlichkeit des Ereignisses _$A$_ und
> _$P(B)$_ die A-priori-Wahrscheinlichkeit des Ereignisses _$B$_.

**Bei endlich vielen Ereignissen lautet der Satz von Bayes:**
Wenn $A_{i},i=1,…,N$ eine Zerlegung der Ergebnismenge in disjunkte Ereignisse ist, gilt für die A-posteriori-Wahrscheinlichkeit $P(A_i∣B)$

$$P(A_i∣B)=\frac{P(B∣A_i)⋅P(Ai)}{P(B)}=P(B∣A_i)⋅P(A_i)∑j=1NP(B∣A_j)⋅P(A_j)$$

Den letzten Umformungsschritt bezeichnet man auch als _Marginalisierung_.

Da ein Ereignis A![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) und sein [Komplement](https://de.wikipedia.org/wiki/Komplement%C3%A4res_Ereignis "Komplementäres Ereignis") Ac![{\displaystyle A^{\mathrm {c} }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b4f1e46abbbe52728bb91baab66b584218d2c406) stets eine Zerlegung der Ergebnismenge darstellen, gilt insbesondere

P(A∣B)=P(B∣A)⋅P(A)P(B∣A)⋅P(A)+P(B∣Ac)⋅P(Ac)![{\displaystyle P(A\mid B)\;=\;{\frac {P(B\mid A)\cdot P(A)}{P(B\mid A)\cdot P(A)+P(B\mid A^{\mathrm {c} })\cdot P(A^{\mathrm {c} })}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b92c17640794d624a3205e9ea4b8fd0e2e96f1f4).

Des Weiteren gilt der Satz auch für eine Zerlegung des Grundraumes Ω![{\displaystyle \Omega }](https://wikimedia.org/api/rest_v1/media/math/render/svg/24b0d5ca6f381068d756f6337c08e0af9d1eeb6f) in [abzählbar](https://de.wikipedia.org/wiki/Abz%C3%A4hlbare_Menge "Abzählbare Menge") viele paarweise disjunkte Ereignisse.

## Interpretation

Siehe auch: [Beurteilung eines binären Klassifikators](https://de.wikipedia.org/wiki/Beurteilung_eines_bin%C3%A4ren_Klassifikators "Beurteilung eines binären Klassifikators")

Der Satz von Bayes erlaubt in gewissem Sinn das Umkehren von Schlussfolgerungen: Man geht von einem bekannten Wert P(B∣A)![{\displaystyle P(B\mid A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e2fe9ad0fdfd8920e56ca948400e111852af0665) aus, ist aber eigentlich an dem Wert P(A∣B)![{\displaystyle P(A\mid B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8f8f30f4da85b53901e0871eb41ed8827f511bb7) interessiert. Beispielsweise ist es von Interesse, wie groß die Wahrscheinlichkeit ist, dass jemand eine bestimmte Krankheit hat, wenn ein dafür entwickelter [Schnelltest](https://de.wikipedia.org/wiki/Schnelltest "Schnelltest") ein positives Ergebnis zeigt. Aus [empirischen Studien](https://de.wikipedia.org/wiki/Empirie "Empirie") kennt man in der Regel die Wahrscheinlichkeit dafür, mit der der Test bei einer von dieser Krankheit befallenen Person zu einem positiven Ergebnis führt. Die gewünschte Umrechnung ist nur dann möglich, wenn man die [Prävalenz](https://de.wikipedia.org/wiki/Pr%C3%A4valenz "Prävalenz")der Krankheit kennt, das heißt die (absolute) Wahrscheinlichkeit, mit der die betreffende Krankheit in der Gesamtpopulation auftritt (siehe [Rechenbeispiel 2](https://de.wikipedia.org/wiki/Satz_von_Bayes#Rechenbeispiel_2)).

Für das Verständnis kann ein [Entscheidungsbaum](https://de.wikipedia.org/wiki/Entscheidungsbaum "Entscheidungsbaum") oder eine [Vierfeldertafel](https://de.wikipedia.org/wiki/Vierfeldertafel "Vierfeldertafel") helfen. Das Verfahren ist auch als [Rückwärtsinduktion](https://de.wikipedia.org/wiki/R%C3%BCckw%C3%A4rtsinduktion "Rückwärtsinduktion")bekannt.

Mitunter begegnet man dem [Fehlschluss](https://de.wikipedia.org/wiki/Fehlschluss "Fehlschluss"), direkt von P(B∣A)![{\displaystyle P(B\mid A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e2fe9ad0fdfd8920e56ca948400e111852af0665) auf P(A∣B)![{\displaystyle P(A\mid B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8f8f30f4da85b53901e0871eb41ed8827f511bb7) schließen zu wollen, ohne die A-priori-Wahrscheinlichkeit P(A)![{\displaystyle P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f264d19e21604793c6dc54f8044df454db82744) zu berücksichtigen, beispielsweise indem angenommen wird, die beiden bedingten Wahrscheinlichkeiten müssten ungefähr gleich groß sein (siehe [Prävalenzfehler](https://de.wikipedia.org/wiki/Pr%C3%A4valenzfehler "Prävalenzfehler")). Wie der Satz von Bayes zeigt, ist das aber nur dann der Fall, wenn auch P(A)![{\displaystyle P(A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f264d19e21604793c6dc54f8044df454db82744) und P(B)![{\displaystyle P(B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e593d180a26fd68657ea50368dbfe1a661e652aa) ungefähr gleich groß sind.

Ebenso ist zu beachten, dass bedingte Wahrscheinlichkeiten für sich allein nicht dazu geeignet sind, eine bestimmte [Kausalbeziehung](https://de.wikipedia.org/wiki/Kausalit%C3%A4t "Kausalität") nachzuweisen.