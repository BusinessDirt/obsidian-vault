---
date: 2025-02-06T17:36
tags:
  - Computerlinguistik
  - NLTK
  - NLP
cssclasses:
  - pen-white
---
<div class="card">
    <h3>📚 Korpus in NLTK</h3>
    <ul>
        <li>Sammlungen von strukturiertem Text für NLP-Aufgaben</li>
        <li>Enthält Rohtext, annotierte Datensätze und Lexika</li>
        <li>Unterstützt mehrere Sprachen und Domänen</li>
    </ul>
</div>

<div class="card">
    <h3>📝 Darstellung von Dokumenten / Rohtext</h3>
    <ul>
        <li>Dokumente werden als Zeichenketten oder Token-Listen gespeichert</li>
        <li>Rohtext wird in strukturierte Formate umgewandelt, um für NLP-Aufgaben nutzbar zu sein</li>
    </ul>
</div>

<div class="card">
    <h3>✂️ Tokenisierung</h3>
    <ul>
        <li>Zerlegung von Text in kleinere Einheiten (Wörter oder Sätze)</li>
        <li>NLTK-Funktionen:</li>
        <ul>
            <li><code>word_tokenize()</code>: Zerlegt Text in Wörter</li>
            <li><code>sent_tokenize()</code>: Zerlegt Text in Sätze</li>
        </ul>
    </ul>
</div>

<div class="card">
    <h3>🔍 Konkordanzen</h3>
    <ul>
        <li>Zeigt Vorkommen eines Wortes im Kontext an</li>
        <li>Hilft, Wortverwendungs-muster zu analysieren</li>
        <li>NLTK-Funktion: <code>Text.concordance()</code></li>
    </ul>
</div>

<div class="card">
    <h3>📊 Lexikalische Dispersionsdiagramme</h3>
    <ul>
        <li>Visualisierung der Verteilung von Wörtern in einem Text</li>
        <li>Zeigt, wo bestimmte Wörter erscheinen</li>
        <li>NLTK-Funktion: <code>dispersion_plot()</code></li>
    </ul>
</div>

<div class="card">
    <h3>📈 Grundlegende Textstatistiken</h3>
    <ul>
        <li><strong>Häufigkeitsverteilungen:</strong> Zählt Vorkommen von Wörtern (<code>FreqDist</code>)</li>
        <li><strong>Bedingte Häufigkeitsverteilungen:</strong> Wortfrequenzen basierend auf Bedingungen</li>
        <li><strong>Typen vs. Token:</strong></li>
        <ul>
            <li><strong>Token:</strong> Gesamtzahl der Wörter im Text</li>
            <li><strong>Typen:</strong> Einzigartige Wörter im Text</li>
        </ul>
        <li><strong>Lexikalische Diversität:</strong> Verhältnis einzigartiger Wörter zur Gesamtanzahl der Wörter</li>
    </ul>
</div>

<div class="card">
    <h3>📌 N-Gramme</h3>
    <ul>
        <li>Sequenzen von <em>n</em> Wörtern in einem Text</li>
        <li>Nützlich für Sprachmodellierung und Textvorhersagen</li>
        <li>Gängige Typen:</li>
        <ul>
            <li>Unigramme (1-Gramm)</li>
            <li>Bigramme (2-Gramm)</li>
            <li>Trigramme (3-Gramm)</li>
        </ul>
        <li>NLTK bietet Funktionen zur Erstellung und Analyse von N-Grammen</li>
    </ul>
</div>

<div class="card">
    <h3>🌍 Sprachenerkenner</h3>
    <ul>
        <li>Erkennt die Sprache eines gegebenen Textes</li>
        <li>Nutzt Wort-/Zeichenmuster und Häufigkeitsverteilungen</li>
    </ul>
</div>

<div class="card">
    <h3>🏷️ Annotierte Korpora</h3>
    <ul>
        <li>Texte mit zusätzlicher Metadaten (POS-Tags, Syntax, benannte Entitäten)</li>
        <li>Beispiele in NLTK: Penn Treebank, CoNLL-Datensätze</li>
    </ul>
</div>

<div class="card">
    <h3>📖 Wortlisten-Korpora</h3>
    <ul>
        <li>Sammlungen von Wörtern für NLP-Aufgaben</li>
        <li>Beispiele:</li>
        <ul>
            <li><strong>Stoppwort-Liste:</strong> Häufige Wörter zum Herausfiltern</li>
            <li><strong>Swadesh-Liste:</strong> Grundwortschatz zum Vergleich zwischen Sprachen</li>
        </ul>
    </ul>
</div>

<div class="card">
    <h3>⚖️ Kollokation vs. Konkordanz</h3>
    <ul>
        <li><strong>Kollokationen:</strong> Wortpaare, die häufig zusammen vorkommen (z. B. „starker Kaffee“)</li>
        <li><strong>Konkordanzen:</strong> Zeigen das Vorkommen eines Wortes im Kontext</li>
        <li>Verwandte Konzepte:</li>
        <ul>
            <li><strong>Stoppwörter:</strong> Häufige Wörter, die in NLP-Aufgaben oft entfernt werden</li>
            <li><strong>Typen & Token:</strong> Einzigartige vs. gesamte Wörter</li>
            <li><strong>Swadesh-Liste:</strong> Gemeinsame Wörter über verschiedene Sprachen hinweg</li>
        </ul>
    </ul>
</div>

<div class="card">
    <h3>🏗️ NLP-Pipeline: Vorverarbeitung</h3>
    <ul>
        <li>Schritte zur Bereinigung und Vorbereitung von Texten für NLP</li>
        <li>Häufige Schritte: Tokenisierung, Normalisierung, Merkmalsextraktion</li>
    </ul>
</div>

<div class="card">
    <h3>📌 Satzsegmentierung</h3>
    <ul>
        <li>Aufteilung von Text in Sätze</li>
        <li>Verwendet Satzzeichen und linguistische Regeln</li>
        <li>NLTK-Funktion: <code>sent_tokenize()</code></li>
    </ul>
</div>

<div class="card">
    <h3>🔄 Normalisierung</h3>
    <ul>
        <li><strong>Kleinschreibung:</strong> Konvertiert Text in Kleinbuchstaben</li>
        <li><strong>Stemming:</strong> Reduziert Wörter auf ihren Stamm (z. B. „laufend“ → „lauf“)</li>
        <li><strong>Lemmatisierung:</strong> Wandelt Wörter in ihre Basisform um (z. B. „besser“ → „gut“)</li>
        <li><strong>Stoppwort-Entfernung:</strong> Entfernt häufig vorkommende, wenig bedeutungsvolle Wörter</li>
    </ul>
</div>
