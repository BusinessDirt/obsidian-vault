---
date: 2026-02-18
tags:
  - Informatik
  - Computerlinguistik
  - Syntax
  - Parsing
---
# Parsingalgorithmen

Parsing ist der Prozess, bei dem ein Computer die syntaktische Struktur eines Satzes basierend auf einer Grammatik analysiert. Man unterscheidet verschiedene Strategien.

## 1. Top-Down Parsing
**Strategie:**
- Beginnt beim Startsymbol $S$ und versucht, den Satz abzuleiten.
- Vorhersageorientiert ("Was erwarte ich?").
- **Problem:** Endlosrekursion bei linksrekursiven Regeln ($A \to A\ B$).
- **Algorithmus:** Recursive Descent.

## 2. Bottom-Up Parsing
**Strategie:**
- Beginnt bei den Wörtern (Input) und versucht, diese zu größeren Konstituenten zusammenzufassen (Reduktion).
- Datenorientiert ("Was habe ich gefunden?").
- **Algorithmus:** Shift-Reduce, CYK (Cocke-Younger-Kasami).

## 3. Shift-Reduce Parser
Ein Bottom-Up Parser, der einen **Stack** (Stapel) und einen **Buffer** (Input) verwendet.
Er kennt zwei Hauptoperationen:
- **Shift:** Ein Wort vom Buffer auf den Stack schieben.
- **Reduce:** Elemente auf dem Stack durch ein Nicht-Terminal ersetzen (gemäß einer Regel $A \to \alpha$).

### Beispieltrace
Grammatik: $S \to NP\ VP$, $NP \to \text{Det}\ N$, $VP \to V\ NP$.
Satz: "The cat chases mice"

| Schritt | Stack | Buffer | Aktion |
| :--- |
| :--- | :--- | :--- | :--- |
| 1 | $\epsilon$ | [The, cat, chases, mice] | Shift |
| 2 | [The] | [cat, chases, mice] | Shift |
| 3 | [The, cat] | [chases, mice] | Reduce ($NP \to \text{Det}\ N$) |
| 4 | [$NP$] | [chases, mice] | Shift |
| 5 | [$NP$, chases] | [mice] | Shift |
| 6 | [$NP$, chases, mice] | $\epsilon$ | Reduce ($NP \to N$) |
| 7 | [$NP$, chases, $NP$] | $\epsilon$ | Reduce ($VP \to V\ NP$) |
| 8 | [$NP$, $VP$] | $\epsilon$ | Reduce ($S \to NP\ VP$) |
| 9 | [$S$] | $\epsilon$ | Akzeptiert |

## 4. Chart Parsing (Earley)
Um Backtracking und redundante Berechnungen zu vermeiden, nutzen Chart-Parser eine Tabelle (Chart), um Zwischenergebnisse zu speichern (Dynamische Programmierung).
- Löst Ambiguität effizienter ($O(n^3)$).