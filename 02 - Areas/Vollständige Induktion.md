---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
  - LinAlg
---
Ein sehr nützliches Beweisverfahren ist die vollständige Induktion. Wir benutzen sie, um zu zeigen, dass eine Aussage $A(n)$ für alle $n \in \mathbb{N}$ gilt (oder für alle $n \in \mathbb{N}_0$, je nach Aufgabe). Dabei ist $A(n)$ in der Regel eine Gleichung, in der ein freier Parameter $n \in \mathbb{N}$ vorkommt. Dafür müssen wir zwei Dinge zeigen:
1. $A(1)$ ist wahr (Induktionsanfang)
2. $A(n) \Rightarrow A(n + 1)$ ist wahr (Induktionsschritt)
Daraus folgt: $A(n)$ ist wahr $\forall n \in \mathbb{N}$
Ausführlicher: Schritt 2 ist der Beweis dafür, dass, wenn $A(n)$ wahr ist (Induktionsannahme), $A(n + 1)$ wahr ist (Induktionsbehauptung)