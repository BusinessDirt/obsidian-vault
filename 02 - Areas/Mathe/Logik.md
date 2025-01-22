---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Analysis
  - LinAlg
---
# Aussagenlogik
Die Aussagenlogik untersucht die Struktur von Sätzen (Aussagen) $A, B, \dots$ hinsichtlich ihres Wahrheitswerts. Sätze (Aussagen) können entweder $wahr$ ($w$) oder $falsch$ ($f$) sein.
## Rechenregeln
Für $\land$ und $\lor$ gelten das Kommutativgesetz, das Assoziativgesetz und das Distributivgesetz,
$$A \land B \Leftrightarrow B \land A$$
$$(A \land B) \land C \Leftrightarrow A \land (B \land C)$$
$$(A \lor B) \land C \Leftrightarrow (A \land C) \lor (B \land C)$$
Weiter gelten die De-Morgan-Regeln
$$\lnot (A \land B) \Leftrightarrow \lnot A \lor \lnot B$$
$$\lnot (A \lor B) \Leftrightarrow \lnot A \land \lnot B$$
Zuletzt gilt für die doppelte Verneinung:
$$\lnot(\lnot A) \Leftrightarrow A$$
## Äquivalenz
Zwei Aussagen $A_1$ und $A_2$ heißen (logisch) äquivalent, wenn sie dieselben Einträge in der Wahrheitstafel besitzen. Sind zwei Aussagen $A_1$ und $A_2$ äquivalent, dann ist die Aussage $A_1 \Leftrightarrow A_2$ eine Tautologie.
## Tautologie
Eine Aussage nennt man eine Tautologie ($=$ allgemein gültige Aussage), wenn alle ihre Einträge in der Wahrheitstafel wahr ($w$) sind. Eine Aussage nennt man ein Paradoxon, wenn alle ihre Einträge in der Wahrheitstafel falsch ($f$) sind.