---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
  - LinAlg
  - Mengenlehre
---
Russell bildete seine Antinomie mit Hilfe der "Klasse aller Klassen, die sich nicht selbst als Element enthalten"
$$R:=\{x | x \notin x\}$$
Oft wird die Russellsche Klasse auch als "Menge aller Mengen, die sich nicht selbst als Element enthalten" definiert. Russel leitete seine Antinomie sinngemäß so ab: Angenommen, $R$ enthalte sich selbst, dann gilt aufgrunde der Klasseneigenschaft, mit der $R$ definiert wurde, dass $R$ sich nicht enthält, was der Annahme widerspricht. Angenommen, es gelte das Gegenteil und $R$ enthalte sich nicht selbst, dann erfüllt $R$ die Klasseneigenschaft, so dass $R$ sich doch selbst enthält, entgegen der Annahme. Mathematisch drückt dies folgende widersprüchliche Äquivalenz aus:
$$R \in R \Leftrightarrow R \notin R$$
Zur Ableitung dieses Widerspruchs werden keine Axiome und Sätze der Mengenlehre benutzt, sondern außer der Definition nur Freges [Abstraktionsprinzip](https://de.m.wikipedia.org/wiki/Klase_(Mengenlehre)#Klassenterme), das Russell in seine Typentheorie übernahm:
$$y \in \{x | A(x)\} \Leftrightarrow A(y)$$