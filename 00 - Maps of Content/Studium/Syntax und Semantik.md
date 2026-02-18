# Syntax und Semantik

Diese Übersicht dient als Lernleitfaden für das Modul Syntax und Semantik. Sie verknüpft die theoretischen Grundlagen der Satzstruktur (Syntax) mit der Bedeutungslehre (Semantik) und computerlinguistischen Methoden.

## 1. Grundlagen der Strukturanalyse
Die Analyse von Sätzen beginnt mit der Zerlegung in ihre Bestandteile.
- [[Konstituentenanalyse]]: Wie identifiziert man zusammengehörige Wortgruppen? (Tests, Kastendiagramme)
- [[Kontextfreie Grammatik]] (CFG): Das formale Rückgrat der syntaktischen Beschreibung ($S \to NP\ VP$).
- [[X-Bar-Theorie]]: Eine generalisierte Strukturhypothese für alle Phrasen (Kopf, Komplement, Spezifizierer).

## 2. Syntaktische Modelle und Phänomene
Erweiterte Konzepte zur Beschreibung natürlicher Sprache.
- [[Dependenzgrammatik]]: Fokus auf die Abhängigkeiten zwischen Wörtern (Kopf-Dependent) statt Phrasenstruktur.
- [[Komplexe Sätze]]: Koordination, Subordination, Relativsätze und Kontrollstrukturen.
- [[Merkmalsstrukturen]]: Feinkörnige Beschreibung grammatischer Eigenschaften (Kasus, Numerus, Person).
- [[Unifikationsgrammatik]]: Kombination von CFG mit Merkmalsstrukturen zur Modellierung von Kongruenz.

## 3. Algorithmische Verarbeitung (Parsing)
Wie Computer syntaktische Strukturen erkennen.
- [[Parsing|Parsingalgorithmen]]: Verfahren zur Analyse (Top-Down, Bottom-Up, Shift-Reduce).
- [[Statistisches Parsing]]: Wahrscheinlichkeitsbasierte Ansätze (PCFG) zur Auflösung von Ambiguitäten.
- [[Chunking und Evaluation]]: Flache Analyse (Chunking) und Messung der Qualität (Precision, Recall).

---
**Lernziele:**
- Syntaktische Strukturen formal beschreiben können.
- Parsing-Algorithmen manuell durchführen können.
- Grammatiken für natürliche Sprache schreiben und erweitern.