---
date: 2026-02-18
tags:
- Computerlinguistik
- Informatik
- Linguistik
- Mathe
- Syntax
---
# Komplexe Sätze

Die [[Syntax]] natürlicher Sprache erlaubt die Konstruktion beliebig langer und komplexer Sätze durch Rekursion.

## 1. Koordination (Parataxe)
Verbindung von gleichrangigen Konstituenten (z.B. zwei Hauptsätze oder zwei $NP$s).
- Konjunktionen: *und, oder, aber*.
- Struktur: $XP \to XP\ Conj\ XP$.
- Bsp: *[Der Mann schläft] und [die Frau liest].*

## 2. Subordination (Hypotaxe)
Einbettung eines Satzes in einen anderen (Nebensatz).
- **Komplementsätze:** Der Nebensatz füllt eine Lücke des Hauptverbs (z.B. Objekt).
  - *Er sagt, [dass er kommt].* (Objektsatz zu "sagen")
- **Adverbialsätze:** Geben Umstände an (Zeit, Grund, Ort).
  - *Er ging, [weil er müde war].*
- **Relativsätze:** Modifizieren ein Nomen (Attribut).
  - *Das Buch, [das ich lese], ist spannend.*

## 3. Kontrollstrukturen (Control vs. Raising)
Bei infiniten Komplementen ("zu ...") fehlt oft das explizite Subjekt. Die Interpretation hängt vom Matrixverb ab.

### Subjektkontrolle (Equi-NP-Deletion)
Das Subjekt des Infinitivs ist identisch mit dem Subjekt des Hauptsatzes.
- *[Er]$_i$ verspricht, [$\\emptyset_i$ zu kommen].*
- Wer kommt? Er.

### Objektkontrolle
Das Subjekt des Infinitivs ist identisch mit dem Objekt des Hauptsatzes.
- *Er überredet [ihn]$_i$, [$\\emptyset_i$ zu bleiben].*
- Wer bleibt? Er (das Objekt).

### Anhebung (Raising)
Das Subjekt des Infinitivs wird syntaktisch zum Subjekt des Hauptsatzes "angehoben", obwohl es semantisch nicht zum Hauptverb gehört.
- *[Er]$_i$ scheint [$\\emptyset_i$ zu schlafen].*
- Semantisch: Es scheint, dass er schläft. "Er" ist nicht der "Scheinende", sondern der "Schlafende".