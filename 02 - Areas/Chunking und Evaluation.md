---
date: 2026-02-18
tags:
  - Informatik
  - Computerlinguistik
  - Evaluation
---
# Chunking & Evaluation

Chunking ist eine robuste, flache syntaktische Analyse, die Phrasen (Chunks) identifiziert, ohne eine vollständige, rekursive Baumstruktur aufzubauen.

## 1. Chunking
Identifikation von nicht-überlappenden Phrasen (z.B. $NP$-Chunks, $VP$-Chunks).
- *[NP Der Mann] [VP liest] [NP das Buch].*
- Rekursion (z.B. PP in NP) wird oft ignoriert.

### IOB-Tagging
Ein Standardformat zur Repräsentation von Chunks als Sequenz von Labels.
- **B (Begin):** Erstes Wort eines Chunks.
- **I (Inside):** Wort innerhalb eines Chunks.
- **O (Outside):** Wort außerhalb eines Chunks.

**Beispiel:**
*Der (B-NP) Mann (I-NP) liest (O) das (B-NP) Buch (I-NP).*

## 2. Evaluation
Wie misst man die Qualität eines Parsers oder Chunkers? Man vergleicht die Ausgabe (Hypothese) mit einem Goldstandard (Referenz).

### Konfusionsmatrix
| | Relevant (Gold) | Nicht Relevant |
| :--- | :--- | :--- |
| **Gefunden (System)** | True Positive ($tp$) | False Positive ($fp$) |
| **Nicht Gefunden** | False Negative ($fn$) | True Negative ($tn$) |

### Metriken
**Accuracy (Genauigkeit):** Anteil korrekter Entscheidungen an allen Entscheidungen.
$$Accuracy = \frac{tp + tn}{tp + fp + fn + tn}$$
(Oft irreführend bei unbalancierten Klassen, z.B. wenn "O" sehr häufig ist.)

**Precision (Präzision):** Wie viele der gefundenen Chunks sind korrekt?
$$P = \frac{tp}{tp + fp}$$

**Recall (Trefferquote):** Wie viele der korrekten Chunks wurden gefunden?
$$R = \frac{tp}{tp + fn}$$

**F1-Measure (Harmonisches Mittel):** Kombiniert Precision und Recall.
$$F_1 = 2 \cdot \frac{P \cdot R}{P + R}$$