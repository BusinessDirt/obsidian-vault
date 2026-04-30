---
date: 2026-02-18
tags:
- Biologie
- Computerlinguistik
- Informatik
- Linguistik
- Parsing
---
# Statistisches & Datengestütztes [[Parsing]]

Statistisches [[Parsing]] nutzt Wahrscheinlichkeiten, um Ambiguitäten aufzulösen und die wahrscheinlichste Analyse für einen Satz zu finden.

## 1. Probabilistische [[Kontextfreie Grammatik]] (PCFG)
Eine PCFG erweitert jede Regel $A \to \alpha$ einer CFG um eine Wahrscheinlichkeit $P(A \to \alpha)$.
- Die Summe der Wahrscheinlichkeiten aller Regeln mit derselben linken Seite ($A$) muss 1 ergeben: $\sum_{\alpha} P(A \to \alpha) = 1$.

### Wahrscheinlichkeit eines Baums
Die Wahrscheinlichkeit eines Parse-Baums $T$ ist das Produkt der Wahrscheinlichkeiten aller darin verwendeten Regeln $r_i$:
$$P(T) = \prod_{i \in T} P(r_i)$$

**Beispiel:**
- $P(S \to NP\ VP) = 1.0$
- $P(VP \to V\ NP) = 0.7$
- $P(VP \to V\ PP) = 0.3$
- ...
- Der [[Baum]] mit der höheren Gesamtwahrscheinlichkeit gewinnt.

## 2. Viterbi-Algorithmus
Der Viterbi-Algorithmus (oft im CYK-Parser integriert) findet effizient den **wahrscheinlichsten** [[Baum]] ($T_{best}$) für einen Satz $S$, ohne alle möglichen Bäume explizit aufzuzählen (Dynamische Programmierung).
- Er speichert in jeder Zelle der Chart nur die Teilbäume mit der höchsten Wahrscheinlichkeit.
- $T_{best} = \arg\max_{T} P(T|S)$

## 3. Probleme der PCFG
- **Unabhängigkeitsannahme:** Die Wahl einer Regel hängt nur vom Nicht-Terminal ab, nicht vom Kontext (z.B. lexikalischen Köpfen). "eat" nimmt eher "pizza" als "happiness" als Objekt, aber $VP \to V\ NP$ weiß das nicht.
- **Lösung:** Lexikalisierte PCFGs (L-PCFG), die Köpfe in die Regeln integrieren ($VP(eat) \to V(eat)\ NP(pizza)$).