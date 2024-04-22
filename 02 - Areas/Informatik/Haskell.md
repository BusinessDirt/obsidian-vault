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
## Typdeklaration (optional)
```haskell
foo :: typ1 -> ... -> typ3 -> ergebnistyp
foo var1 var2 var3 = expr1
```

