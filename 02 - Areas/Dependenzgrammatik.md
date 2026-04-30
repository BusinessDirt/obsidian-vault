---
date: 2026-02-18
tags:
- Computerlinguistik
- Informatik
- Linguistik
- Syntax
---
# Dependenzgrammatik

Im Gegensatz zur Konstituentengrammatik (Phrasenstruktur) stellt die Dependenzgrammatik die **Abhängigkeitsbeziehungen** ([[Relationen]]) zwischen Wörtern in den Mittelpunkt. Es gibt keine Phrasenknoten ($NP, VP$), sondern direkte Links zwischen Wörtern.

## 1. Grundprinzip: Kopf und Dependent
Jede Beziehung besteht aus einem **Kopf** (Head, Regens) und einem **Dependenten** (Modifier, Rectum).
- Der Kopf bestimmt die grammatischen Eigenschaften der Konstruktion.
- Der Dependent ist vom Kopf abhängig.
- Das Hauptverb ist meist die Wurzel (Root) des gesamten Satzes.

**Notation:** $H \to D$ (Kopf regiert Dependent) oder $D \to H$ (Pfeil zeigt Abhängigkeit).

## 2. Valenz
Die Valenz eines Wortes bestimmt, wie viele und welche Art von Dependenten es fordert.
- **Nullwertig:** *es regnet* (kein echtes Subjekt).
- **Einwertig (intransitiv):** *schlafen* (fordert Subjekt). $\to$ *[Er] schläft.*
- **Zweiwertig (transitiv):** *essen* (fordert Subjekt, Objekt). $\to$ *[Er] isst [einen Apfel].*
- **Dreiwertig (ditransitiv):** *geben* (fordert Subjekt, direktes Objekt, indirektes Objekt).

## 3. Universal Dependencies (UD)
Ein Standard für sprachübergreifende Dependenzannotation.
Wichtige [[Relationen]] (Labels):
- `nsubj`: Nominal subject (Subjekt)
- `obj`: Object (Objekt)
- `root`: Wurzel
- `det`: Determiner (Artikel)
- `amod`: Adjectival modifier (Adjektivattribut)

**Beispielbaum (UD):**
*The small cat sits on the mat.*
```text
      sits (root)
      /   \
   nsubj   obl
    /       \
  cat       mat
 /   \      /
det amod   case
|    |      |
The small  on
```

## 4. Projektivität
- **Projektiv:** Kanten im Dependenzbaum überkreuzen sich nicht (Normalfall).
- **Nicht-projektiv:** Kanten überkreuzen sich (häufiger in Sprachen mit freier Wortstellung wie Deutsch).
  - Bsp: *Das Buch habe ich gestern [gelesen].* ("gelesen" hängt von "habe" ab, "Buch" von "gelesen" -> Kreuzung über "habe").