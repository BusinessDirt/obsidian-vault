---
date: 2026-02-18
tags:
- Computerlinguistik
- Informatik
- Linguistik
- Mathe
- Syntax
---
# Unifikationsgrammatiken

Unifikationsgrammatiken erweitern kontextfreie Grammatiken durch [[Merkmalsstrukturen]]. Dies ermöglicht eine kompakte Darstellung syntaktischer Phänomene wie Kongruenz, Rektion und Subkategorisierung.

## 1. Erweiterung von Regeln
Jede CFG-Regel wird mit einer Menge von Gleichungen (Constraints) versehen, die bestimmen, welche Merkmale die Konstituenten haben müssen.

**Beispiel:** $S \to NP\ VP$
- $NP.AGR = VP.AGR$ (Das Agreement-Merkmal von $NP$ und $VP$ muss unifizierbar sein.)

## 2. Pfadgleichungen
Gleichungen beziehen sich auf Pfade in der Merkmalsstruktur. Ein Pfad ist eine Folge von Attributen.
- `⟨SUBJ NUM⟩ = sg` (Das Numerus-Merkmal des Subjekts ist Singular.)
- `⟨X0 CAT⟩ = S` (Die Kategorie des Elternknotens ist S.)
- `⟨X1 AGR⟩ = ⟨X2 AGR⟩` (Die Tochterknoten X1 und X2 müssen übereinstimmen.)

## 3. Lexikalisierung
Statt Regeln für jede mögliche Merkmalskombination ($S \to NP_{sg}\ VP_{sg}, S \to NP_{pl}\ VP_{pl}$ ...) zu schreiben, verwenden wir Variablen und Unifikation.
- Lexikoneintrag für "der":
  $$
  \left[
  \begin{matrix}
  CAT & Det \\
  AGR & \left[ \begin{matrix} GEN & mask \\ NUM & sg \\ CAS & nom \end{matrix} \right]
  \end{matrix}
  \right]
  $$
- Wenn "der" mit einem Nomen wie "Mann" kombiniert wird, müssen deren AGR-Werte unifizieren. "der" + "Frau" schlägt fehl, da *mask* $\neq$ *fem*.

## 4. Head-Driven Phrase Structure Grammar (HPSG)
Eine bedeutende Theorie, die fast vollständig auf Unifikation basiert.
- Jedes linguistische Objekt ist eine Merkmalsstruktur (Zeichen, [[Wort]], Phrase).
- Prinzipien (z.B. Kopf-Merkmal-Prinzip) ersetzen viele explizite Regeln.
- **SUBCAT-[[Liste]]:** Ein Merkmal, das angibt, welche Argumente ein [[Wort]] noch benötigt (Valenz als [[Liste]], die "abgearbeitet" wird).