---
date: 2024-04-17T16:43
tags:
  - Informatik
  - Haskell
  - Programmiersprache
cssclasses:
---
# Wichtige Ausdrücke
- Constructor: `(:) :: a -> [a] -> [a]`
- Listen Aufzählungen: `[1,3..99]`
- List-Comprehensions: `[x | x <- [1..9], even x]`
- Konditional: `if .. then .. else ..`
- Lokale Definition: `let .. in ..`
- Pattern Matching `case .. of ..`

# Notationen zur Funktionsdefinition

## Standarddefinition
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
	| grd211, ..., grd21i = expr21
	| grd221, ..., grd22i = expr22
```

## Nachgeschobene lokale Definition pro Funktionsgleichung
```haskell
foo pat31 ... pat3n
	| grd311, ..., grd31k = expr31
  where idA = exprA
		idB = exprB
```

## Beispiele
```haskell
show_signed :: Integer -> String
show_signed 0 = " 0"
show_signed i | i>=0 = "+" ++ (show i)
              | otherwise = (show i)

printPercent :: Double -> String
printPercent x = lzero ++ (show p2) ++ "%"
  where
    p2 :: Double
    p2 = (fromIntegral (round' (1000.0*x))) / 10.0
    lzero = if p2 < 10.0 then "0" else ""
    round' :: Double -> Int
    round' z = round z
```
