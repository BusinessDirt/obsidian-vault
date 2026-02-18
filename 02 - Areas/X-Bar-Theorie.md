---
date: 2026-02-18
tags:
  - Informatik
  - Computerlinguistik
  - Syntax
---
# X-Bar-Theorie

Die X-Bar-Theorie ist eine Erweiterung der Phrasenstrukturgrammatik. Sie nimmt an, dass alle Phrasen ($XP$) dieselbe hierarchische Grundstruktur haben.

## 1. Das X-Bar-Schema
Jede Phrase wird um einen lexikalischen **Kopf** ($X$) herum aufgebaut.

### Die Regeln
1.  **XP-Regel:** $XP \to (Spec)\ X'$
    *   Eine Phrase ($XP$) besteht aus einem optionalen Spezifizierer ($Spec$) und einer Zwischenebene ($X'$).
2.  **Adjunktions-Regel:** $X' \to X'\ (Adj) \mid (Adj)\ X'$
    *   Die Zwischenebene ($X'$) kann rekursiv durch Adjunkte ($Adj$) erweitert werden.
3.  **Komplement-Regel:** $X' \to X\ (Comp)$
    *   Der Kopf ($X$) verbindet sich mit einem Komplement ($Comp$) zur Zwischenebene ($X'$).

### Strukturbaum
```text
      XP
     /  \
  Spec   X'
        /  \
      X'    Adj
     /  \
    X   Comp
```

## 2. Komponenten
*   **Kopf (Head) X:** Der Kern der Phrase (z.B. $N$ in einer $NP$, $V$ in einer $VP$). Bestimmt die Eigenschaften der Phrase.
*   **Spezifizierer (Spec):** Bestimmt die Phrase näher (z.B. Determinierer in $NP$: "der" in "der Mann").
*   **Komplement (Comp):** Notwendige Ergänzung des Kopfes (z.B. Objekt in $VP$: "den Ball" in "tritt den Ball"). Schwester von $X$.
*   **Adjunkt (Adj):** Optionale Zusatzinformation (z.B. Adjektive oder PPs). Schwester von $X'$ und Tochter von $X'$.

## 3. Rekursion
Die Regel $X' \to X'\ Adj$ erlaubt unendliche Rekursion, was erklärt, warum wir beliebig viele Adjektive oder Relativsätze anfügen können:
*   *Das [große, rote, alte ...] Auto*