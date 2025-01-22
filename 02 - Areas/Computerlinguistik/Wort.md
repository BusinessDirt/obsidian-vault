---
date: 2024-04-17T20:14
tags:
  - Informatik
  - Computerlinguistik
cssclasses: []
---
- Der Begriff "Wort" ist ungenau, wenn nicht weiter spezifiziert.
- Ist das abstrakte Wort oder ein konkretes Vorkommen gemeint?
- Unterscheidungen:
	- Wortform vs. Lexem
	- Token vs. Type

## Wortform
> flektierte Form eines Wortes, so wie es im konkreten Text (gesprochen oder geschreiben) vorkommt.
> Beispiel: schönes

## Lexem
> Ein Lexem ist eine Klasse lexikalisch äquivalenter Wortformen. Diese Wortformen repräsentieren das Lexem in verschiedenen Umgebungen.
> Beispiel: $L_{1} = \{ \text{"sing", "sings", "singing", "sang", "sung"} \}$

Oft wird auf einem Lexem mit seiner Zitierform Bezug genommen, z.B. Infinitiv oder erste Person Singular für Verben und Nominativ Singular für Nomen.

## Token
> Konkretes Vorkommen z.B. einer Wortform (z.B. vor oder nach einem anderen Token)

## Type
> Ein Type bezeichnet eine Klasse von Token, die ...
> ... nicht unterschieden werden
> ... als Kopien wahrgenommen werden
> ... gleich sind

- 'eine Rose ist eine Rose' $\Rightarrow$ 5 Token, 3 Types
- Verhältnis von Types zu Tokens (type-to-token ratio) ist eine wichtige Kennzahl zur Charakterisierung von Texten.