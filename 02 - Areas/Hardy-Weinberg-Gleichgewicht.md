---
date: 2026-04-09 11:02
tags:
  - Stochastik
  - Statistik
  - Biologie
  - Genetik
  - Populationsgenetik
  - Evolution
aliases:
  - HWG
---
## 🧬 Definition
Das Hardy-Weinberg-Gleichgewicht beschreibt einen theoretischen Zustand einer Population, in der keine Evolution stattfindet. Die Allelfrequenzen und Genotypfrequenzen bleiben von Generation zu Generation konstant.

> [!important] Die Idealpopulation
> Damit das HWG gilt, müssen folgende Bedingungen erfüllt sein:
> 1. **Sehr große Population** (kein Zufallseffekt/Gendrift).
> 2. **Panmixie** (Jeder paart sich mit jedem mit gleicher Wahrscheinlichkeit).
> 3. **Keine Mutationen**.
> 4. **Keine Selektion** (alle Individuen sind gleich fit).
> 5. **Keine Isolation/Migration** (kein Genfluss von außen).

---
## 🧮 Die mathematischen Formeln

### 1. Allelebene
Betrachtet man die einzelnen [[Allele]] in einem Genpool:
$$p + q = 1$$
*(Dabei ist p = Frequenz von A; q = Frequenz von a)*

### 2. Genotypebene
Betrachtet man die Individuen der Population:
$$p^2 + 2pq + q^2 = 1$$

- **$p^2$**: Frequenz des Genotyps **AA** (homozygot dominant)
- **$2pq$**: Frequenz des Genotyps **Aa** (heterozygot)
- **$q^2$**: Frequenz des Genotyps **aa** (homozygot rezessiv)

---
## 💡 Beispielrechnung: Vererbung von Allelen
Angenommen, wir untersuchen eine Population von 100 Individuen. Wir wissen, dass 4 Individuen eine rezessive Erbkrankheit zeigen (Genotyp **aa**).

1. **q² bestimmen:**
   $q^2 = 4 / 100 = 0,04$
   
2. **Allelfrequenz q berechnen:**
   $\sqrt{0,04} = 0,2$ -> Das Allel **a** hat eine Frequenz von **20%**.

3. **Allelfrequenz p berechnen:**
   Da $p + q = 1$, ist $p = 1 - 0,2 = 0,8$. -> Das Allel **A** hat eine Frequenz von **80%**.

4. **Anteil der Mischerbigen (Aa) berechnen:**
   $2pq = 2 \cdot 0,8 \cdot 0,2 = 0,32$. -> **32%** der Population sind Überträger ([[Allele]]-Kombination Aa).

---
## ⚠️ Das Hardy-Weinberg-Ungleichgewicht
In der Realität sind die Bedingungen einer Idealpopulation fast nie erfüllt. Weichen die beobachteten Zahlen von den berechneten HWG-Werten ab, deutet dies auf **Evolutionsfaktoren** hin:
- **Mutationen** verändern Allele.
- **Selektion** bevorzugt bestimmte Genotypen.
- **Migration** bringt neue Gene ein.
