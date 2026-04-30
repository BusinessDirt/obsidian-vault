---
date: 2026-02-18
tags:
- Computerlinguistik
- Informatik
- Linguistik
- Physik
- Syntax
---
# Konstituentenanalyse

Die Konstituentenanalyse zerlegt Sätze in hierarchisch geordnete Einheiten, die **Konstituenten**. Eine Konstituente ist eine Wortgruppe, die eine syntaktische Einheit bildet.

## 1. Konstituententests
Um zu prüfen, ob eine Wortfolge eine Konstituente bildet, verwendet man verschiedene Tests. Nur wenn eine Wortfolge mehrere Tests besteht, gilt sie als Konstituente.

### Permutation (Verschiebeprobe)
Kann die Wortfolge als Ganzes an eine andere Position im Satz verschoben werden (oft ins Vorfeld)?
*   *Der Mann liest [das Buch] im Park.*
*   $	o$ *[Das Buch] liest der Mann im Park.* (Positiv)

### Substitution (Ersatzprobe)
Kann die Wortfolge durch ein einzelnes [[Wort]] (z.B. Pronomen) ersetzt werden?
*   *Der Mann liest [das interessante Buch].*
*   $	o$ *Der Mann liest [es].* (Positiv)

### Koordinationstest
Kann die Wortfolge mit einer gleichartigen Wortfolge durch "und" verbunden werden?
*   *Er kauft [alte Bücher] und [neue CDs].* (Positiv)

### Frage-Test
Kann man nach der Wortfolge fragen?
*   *Er liest [das Buch].* $	o$ *Was liest er?* - *[Das Buch].*

## 2. Strukturdiagramme
Konstituentenstrukturen werden oft als Bäume (Syntaxbäume) oder Kastendiagramme dargestellt.

**Beispiel:** "Der Hund bellt."
```text
      S
     / \
   NP   VP
  /  \    \
Det   N    V
 |    |    |
Der  Hund bellt
```

## 3. Adjunkte vs. Komplemente
Innerhalb einer Phrase unterscheidet man zwischen notwendigen und optionalen Ergänzungen.

| Komplement (Ergänzung) | Adjunkt (Angabe) |
| :--- | :--- |
| Vom Kopf gefordert (Valenz) | Optional, weglassbar |
| Oft obligatorisch | Beliebig oft wiederholbar |
| Bsp: *Er wohnt [in Berlin].* | Bsp: *Er isst [in Berlin].* |