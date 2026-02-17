### 1. Grundlagen & Konstituentenanalyse

- **Konstituententests:** Anwendung von Tests wie Permutation (Umstellprobe), Substitution (Ersatzprobe) und dem Geschehens-Test.
- **Kastendiagramme:** Visualisierung von Konstituentenstrukturen oberhalb der Wortebene.
- **Adjunkten vs. Komplemente:** Unterscheidung durch spezifische Tests und Kenntnis der strukturellen Unterschiede.

### 2. Grammatikmodelle (CFG & X-Bar)

- **Kontextfreie Grammatiken (CFG):** Erstellen minimaler CFGs für spezifische Phänomene (z. B. temporale Ambiguität).
- **X-Bar-Theorie:** Strukturbaum-Schema mit Spezifizierer, Kopf, Komplement und Adjunkt.
- **Rekursion:** Modellierung rekursiver Strukturen, wie die Adjunktion von Adverbialen oder PP-Attachement an NPs.

### 3. Parsingalgorithmen

- **Strategien:** Top-Down vs. Bottom-Up sowie der Unterschied zwischen verschiedenen Parsern (Recursive-Descent, Earley, Shift-Reduce).
- **Prozesse:** Stack-Zustände bei Shift-Reduce-Parsern analysieren und nächste Operationen vorhersagen.
- **Probleme:** Auswirkungen von Ambiguität und indirekter Rekursion auf die Laufzeit und das Backtracking. 

### 4. Dependenzgrammatik

- **UD-Richtlinien:** Erstellen von Dependenzbäumen gemäß den _Universal Dependencies_ (z. B. Primat der Inhaltswörter).
- **Labeling:** Korrekte Zuweisung von Relationen wie `nsubj`, `obj`, `det`, `amod`, `obl` etc..
- **Dependency Parsing:** Übergangsbasierte Parser (Shift, Right-Arc, Left-Arc, Reduce) und die Reihenfolge der Operationen.

### 5. Komplexe Sätze

- **Satztypen:** Identifikation von Satzgefügen und Einbettungen (z. B. Komplementsätze, Relativsätze).
- **Modellierung:** Erweiterung von CFGs um `SBAR` und `COMP` unter Berücksichtigung von Wortstellungsänderungen.  
- **Kontrollstrukturen:** Unterscheidung zwischen Subjekt- und Objektkontrolle.

### 6. Merkmalsstrukturen & Unifikation

- **Merkmalsstrukturen:** Darstellung syntaktischer Eigenschaften (CASE, NUM, PERS etc.) in Attribut-Wert-Matrizen.
- **Unifikation & Subsumption:** Prüfung, ob zwei Strukturen kompatibel sind oder ob eine Struktur eine andere allgemeiner beschreibt (⊑). 
- **Typhierarchien:** Darstellung von Vererbungsbeziehungen als Baum oder Verband und Unifikation von Typen.

### 7. Unifikationsgrammatiken

- **Beschränkungen:** Modellierung von Agreement (Kongruenz), Kasusrektion und Subkategorisierung mittels Merkmalsconstraints.
- **Pfadgleichungen:** Angabe von Constraints in Form von Gleichungen (z. B. NP@NUM=VP@NUM).

### 8. Statistisches & Datengestütztes Parsing

- **PCFG:** Berechnung von Ableitungswahrscheinlichkeiten (p) und Bestimmung fehlender Regelgewichte.
- **Viterbi-Algorithmus:** Verständnis der Funktionsweise zur Findung des wahrscheinlichsten Baums. 
- **Annotation:** Durchführung von Parent-Annotation und Kopfannotation (Lexikalisierung) in Syntaxbäumen.

### 9. Chunking & Evaluation

- **IOB-Tagging:** Annotation von Nominalphrasen mit dem Schema B-NP, I-NP, O.
- **Evaluation:** Berechnung von **Accuracy**, **Precision** und **Recall** anhand von Goldstandard (truth) und Hypothese (predict).