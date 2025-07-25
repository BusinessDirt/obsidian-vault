---
date: 2024-04-17T20:14
tags:
  - Informatik
  - Mathe
cssclasses: 
aliases:
  - endliche Automaten
  - endlichen Automaten
  - endlicher Automat
---
> Ein endlicher Automat ist ein mathematisches Modell, das Wörter akzeptiert oder ablehnt, indem es durch Zustände über Eingabesymbole wandert.


## DFA (Deterministischer Endlicher Automat)
Ein DFA ist ein 5-Tupel
$$A=(Q, \Sigma, \delta, q_{0},F)$$

| Symbol   | Bedeutung                                  |
| :------- | :----------------------------------------- |
| $Q$      | endliche Menge von Zuständen               |
| $\Sigma$ | Eingabealphabet                            |
| $\delta$ | Übergangsfunktion: $Q \times \Sigma \to Q$ |
| $q_{0}$  | Startzustand $\in Q$                       |
| $F$      | akzeptierende Endzustände $\subseteq Q$    |

### Eigenschaften
- Deterministisch: Für jeden Zustand und jedes Zeichen gibt es genau einen Übergang
- Jeder Zustand hat höchstens einen Übergang pro Eingabesymbol

## NFA (Nichtdeterministischer Endlicher Automat)
Ein NFA ist fast wie ein DFA, aber die Übergangsfunktion ist “lockerer”
$$A=(Q, \Sigma, \delta, q_{0},F)$$
Unterschied:
$$\delta:Q \times \Sigma \to P(Q)$$
→ kann mehrere oder keine Übergange für ein Symbol geben.

### Eigenschaften
- Nichtdeterminismus: In einem Zustand kann es mehrere mögliche Übergänge für dasselbe Symbol geben
- Kann auch $\epsilon$-Übergänge haben (Übergang ohne Eingabezeichen)