---
date: 2026-02-18
tags:
  - Informatik
  - Computerlinguistik
  - Syntax
---
# Merkmalsstrukturen & Unifikation

Atomare Symbole wie $NP$ oder $VP$ reichen oft nicht aus, um grammatische Übereinstimmungen (Kongruenz) zu modellieren (z.B. *Subjekt und Verb müssen in Numerus und Person übereinstimmen*). Merkmalsstrukturen lösen dieses Problem.

## 1. Attribut-Wert-Matrizen (AVM)
Merkmalsstrukturen werden als AVM dargestellt. Ein Merkmal (Attribut) hat einen Wert, der atomar oder wiederum eine Merkmalsstruktur sein kann.

$$ 
\left(
\begin{matrix}
CAT & NP \\
AGR & \left( \begin{matrix} NUM & sg \\ PERS & 3 \end{matrix} \right)
\end{matrix}
\right)
$$ 

## 2. Subsumption ($\sqsubseteq$)
Eine Relation zwischen Merkmalsstrukturen. Struktur $A$ subsumiert Struktur $B$ ($A \sqsubseteq B$), wenn $A$ allgemeiner (weniger informativ) ist als $B$.
- $A$: $[ NUM: sg ]$
- $B$: $[ NUM: sg, PERS: 3 ]$
- $A$ ist in $B$ enthalten ("passt in $B$").

## 3. Unifikation ($\sqcup$)
Die Operation, die zwei Merkmalsstrukturen zu einer neuen, möglichst allgemeinen Struktur verschmilzt, die die Informationen beider enthält.
- Wenn Informationen widersprüchlich sind (z.B. $[ NUM: sg ]$ vs. $[ NUM: pl ]$), schlägt die Unifikation fehl ($\bot$). 

### Regeln der Unifikation
1.  Identische Werte bleiben erhalten.
2.  Spezifischere Werte überschreiben allgemeinere (wenn kompatibel).
3.  Zusätzliche Merkmale werden hinzugefügt.

**Beispiel:**
$$ 
\left( \begin{matrix} NUM & sg \end{matrix} \right) \sqcup \left( \begin{matrix} PERS & 3 \end{matrix} \right) = \left( \begin{matrix} NUM & sg \\ PERS & 3 \end{matrix} \right)
$$ 

## 4. Reentrancy (Strukturteilung)
Zwei Merkmale können auf **dasselbe** Objekt im Speicher zeigen (nicht nur gleicher Wert, sondern identisches Objekt). In AVMs oft durch Indizes (Boxen) markiert:
$$ 
\left(
\begin{matrix}
SUBJ & \boxed{1} \\
OBJ & \boxed{1}
\end{matrix}
\right)
$$ 
(Bedeutet: Subjekt und Objekt sind identisch, z.B. "Er rasiert sich".)