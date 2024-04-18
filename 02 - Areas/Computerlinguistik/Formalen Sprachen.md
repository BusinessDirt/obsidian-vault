Formale Sprachen sind künstliche Sprachen, die es Computern ermöglichen, Daten und Informationen zu verarbeiten. Oft werden diese formalen Sprachen von [[Endliche Automaten|endliche Automaten]]verwaltet. Eine formale Sprache L besteht aus einer Menge von Wörtern, die wiederum aus Zeichen des Alphabets der Sprache bestehen. Das Alphabet  ist hierbei die Menge der Zeichen, die in einem Wort  benutzt werden dürfen, wie zum Beispiel die Buchstaben von A bis Z und Umlaute im deutschen Alphabet.

## EBNF
Grammatik: $G=(V, \Sigma, P, S)$
Alphabet: $\Sigma={0, 1, 2, 3, ..., 9, A, B, C, .., Z}$
Menge der syntaktischen Variablen: $V={beschriftung, lagerort, fachregal, feld, behälter, ziffer}$
Startvariable: $S=beschriftung$

<br>

$beschriftung=lagerort \space fachregal \space feld \space fachregal \space behälter$
$lagerort=A|B|C|D$
$fachregal=A|B|C|...|Z$
$feld=ziffer \space ziffer$
$behälter=1|2|...|9$
$ziffer=0|behälter$