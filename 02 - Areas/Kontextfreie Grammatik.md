---
date: 2026-02-18
tags:
  - Informatik
  - Computerlinguistik
  - Syntax
---
# Kontextfreie Grammatik (CFG)

Eine kontextfreie Grammatik ist ein formaler Mechanismus zur Beschreibung der syntaktischen Struktur von Sätzen. Sie ist "kontextfrei", weil die Ersetzung eines Nicht-Terminals unabhängig von seiner Umgebung geschieht.

## 1. Formale Definition
Eine CFG ist ein 4-Tupel $G = (N, \Sigma, P, S)$:

*   $N$: Endliche Menge von **Nicht-Terminalen** (syntaktische Kategorien wie $NP, VP, S$).
*   $\Sigma$: Endliche Menge von **Terminalen** (Wörter wie "Kind", "schläft").
*   $P$: Endliche Menge von **Produktionsregeln** der Form $A \to \alpha$, wobei $A \in N$ und $\alpha \in (N \cup \Sigma)^*$.
*   $S$: Das **Startsymbol** ($S \in N$).

## 2. Beispielgrammatik
$S \to NP\ VP$
$NP \to Det\ N$
$VP \to V\ NP$
$VP \to V$
$Det \to \text{der} \mid \text{die}$
$N \to \text{Hund} \mid \text{Katze}$
$V \to \text{sieht} \mid \text{schläft}$

## 3. Ableitung (Derivation)
Eine Ableitung ist eine Folge von Ersetzungsschritten, beginnend beim Startsymbol $S$ bis nur noch Terminale übrig sind.

**Beispiel:** "Der Hund schläft"
1.  $S$
2.  $\to NP\ VP$ (Regel $S \to NP\ VP$)
3.  $\to Det\ N\ VP$ (Regel $NP \to Det\ N$)
4.  $\to \text{Der}\ N\ VP$ (Regel $Det \to \text{Der}$)
5.  $\to \text{Der}\ \text{Hund}\ VP$ (Regel $N \to \text{Hund}$)
6.  $\to \text{Der}\ \text{Hund}\ V$ (Regel $VP \to V$)
7.  $\to \text{Der}\ \text{Hund}\ \text{schläft}$ (Regel $V \to \text{schläft}$)

## 4. Ambiguität
Eine Grammatik ist ambig, wenn es für einen Satz **mehr als einen** Ableitungsbaum gibt (strukturelle Ambiguität).
*   **Klassiker:** "I shot an elephant in my pajamas."
    *   Lesart 1: Ich trug den Pyjama. ($[_{VP} \text{shot} [_{NP} \text{an elephant}] [_{PP} \text{in my pajamas}]]]$)
    *   Lesart 2: Der Elefant trug den Pyjama. ($[_{VP} \text{shot} [_{NP} \text{an elephant} [_{PP} \text{in my pajamas}]]]]$)
