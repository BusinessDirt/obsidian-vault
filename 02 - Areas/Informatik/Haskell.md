---
date: 2024-04-17T16:43
tags:
  - Informatik
  - Haskell
  - Programmiersprache
cssclasses:
---
# Wichtige Ausdrücke
- Cons-Constructor: `(:) :: a -> [a] -> [a]`
- Listen Aufzählungen: `[1,3..99]`
- List-Comprehensions: `[x | x <- [1..9], even x]`
- Konditional: `if .. then .. else ..`
- Lokale Definition: `let .. in ..`
- Pattern Matching `case .. of ..`

# Notationen zur Funktionsdefinition

## Standartdefinition
- Typdeklaration (optional) (Zeile 1)
- Funktionsname (in gleicher Spalte beginnen) (‘foo’)
- Funktionsparameter (‘var1 var2 var3’)
- Funktionsrumpf (‘expr1’)

```haskell
foo :: typ1 -> ... -> typ3 -> ergebnistyp
foo var1 var2 var3 = expr1
```

## Fallunterscheidung durch Mustervergleiche
```haskell
foo pat_1 ... pat_n = expr1
foo pat21 ... pat2n = expr2
foo pat31 ... pat3n = expr3
```

## Verfeinerung des Pattern-Match durch Wächter
```haskell
foo pat21 ... pat2n
	| grd211, ..., grd21i 
```