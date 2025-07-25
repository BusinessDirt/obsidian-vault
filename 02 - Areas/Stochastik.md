---
date: 2024-10-16T16:17
tags:
  - Mathe
  - Stochastik
---
# Stochastik
## Begriffe und Beispiele
> Ergebnisraum: Die Menge aller Ergebnisse ($\Omega = \{1, 2, 3, 4, ..., 8\}$)
> Ergebnis: Ein möglicher Versuchsausgang ($\omega = \{3\}$)
> Ereignis: Eine Teilmenge des Ergebnisraums ($A=\{2, 4, 6, 8\}$)
> Gegenereignis: Gegenteil eines Ereignisses ($\overline{A}=\{1, 3, 5, 7\}$)
> Sicheres Ereignis: tritt für jeden Fall ein (Ergebnis ist eine Zahl von $1 - 8$)
> unmögliches Ereignis: tritt für keinen Fall ein (Ergebnis ist ein Buchstabe)
> unvereinbare Ereignisse: wenn $A\cap B = \{\}$

## Der axiomatische Wahrscheinlichkeitsbegriff
1.  Für jedes Ereignis  $A\in \Sigma$ ist die Wahrscheinlichkeit von $A$ eine reelle Zahl zwischen 0 und 1: $0\leq P(A)\leq 1$
2.  Das sichere Ereignis $\Omega \in \Sigma$ hat die Wahrscheinlichkeit 1:  $P(\Omega )=1$
3.  Die Wahrscheinlichkeit einer Vereinigung abzählbar vieler _inkompatibler_ Ereignisse ist gleich der Summe der Wahrscheinlichkeiten der einzelnen Ereignisse. Dabei heißen Ereignisse $A_{i}$ _inkompatibel_, wenn sie paarweise sind, also bei $A_{i}\cap A_{j}=\emptyset$ für alle $i\neq j$. Es gilt daher $P\left(A_{1}\;\;\!\!{\dot {\cup }}\;\;\!\!A_{2}\;\;\!\!{\dot {\cup }}\;\;\!\!\!\cdots \right)=\sum P(A_{i})$. Diese Eigenschaft wird auch σ-Additivität genannt.

### Folgerungen aus den Axiomen:
1. Aus der Additivität der Wahrscheinlichkeit disjunkter Ereignisse folgt, dass komplementäre Ereignisse (Gegenereignisse) komplementäre Wahrscheinlichkeiten (**Gegenwahrscheinlichkeiten**) haben: $P(\Omega \setminus A)=1-P(A)$.

_Beweis:_ Es ist $(\Omega \setminus A)\cup A=\Omega$ sowie $(\Omega \setminus A)\cap A=\emptyset$. Folglich nach Axiom (3): $P(\Omega \setminus A)+P(A)=P(\Omega )$ und dann nach Axiom (2): $P(\Omega \setminus A)+P(A)=1$. Umgestellt ergibt sich: $P(\Omega \setminus A)=1-P(A)$

2. Daraus folgt, dass das _unmögliche Ereignis,_ die leere Menge, die Wahrscheinlichkeit Null hat: $P(\emptyset )=0$.

_Beweis:_ Es ist $\emptyset \cup \Omega =\Omega$ und $\emptyset \cap \Omega =\emptyset$, also nach Axiom (3): $P(\emptyset )+P(\Omega )=P(\Omega )$. Hieraus folgt $P(\emptyset )=0$.

3. Für die Vereinigung nicht notwendig disjunkter Ereignisse folgt: $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

_Beweis:_ Die für den Beweis erforderlichen Mengen sind im obigen Bild dargestellt. Die Menge $A\cup B$ kann danach als Vereinigung von drei disjunkten Mengen dargestellt werden:

## Verknüpfte Ereignisse
Verknüpfte Ereignisse und ihre Wahrscheinlichkeiten lassen sich gut in Mengendiagrammen, Vierfeldertafeln und Baumdiagrammen darstellen

## Stochastische Unabhängigkeit
Sei $(\Omega ,\Sigma ,P)$ ein Wahrscheinlichkeitsraum $I$ eine nichtleere Indexmenge und sei $(A_{i})_{i\in I}$ eine Familie von Ereignissen. Die Familie von Ereignissen heißt unabhängig, wenn für jede endliche nichtleere Teilmenge $J$ von $I$ gilt, dass

$$P\left(\bigcap _{j\in J}A_{j}\right)=\prod _{j\in J}P(A_{j})$$

Jede Paarmenge und die Gesamtmenge muss unabhängig sein

##  2 Zufallsvariablen und Binomialverteilung
### 2.1 Zufallsvariablen
<p class="external-refference"><span>Bsp</span>Monopoly: im Gefängnis</p>

Wie viele Runden dauert es bis zum nächsten Pasch?
Würfelergebnisse:
Spieler 1: $\omega_1=[(1;2), (5;3), (4;4)]$ -> $X(\omega_1)=3$
Spieler 2: $\omega_2=[(6;6), (2;4), (1;5)]$ -> $X(\omega_2)=1$
Spieler 3: $\omega_3=[(6;5), (3;3), (5;2)]$ -> $X(\omega_3)=2$
Eine Abbildung $X$, die jedem Ergebniss $\omega$ aus $\Omega$ eine Reelle Zahl zuordnet, heißt Zufallsvariable. 
$$X: \Omega \to \mathbb{R}$$
$$\omega \to X(\omega)$$

### 2.2 Die Wahrscheinlichkeitsverteilung einer Zufallsvariable
Wie sieht es mit den Wahrscheinlichkeiten der Werte einer Zufallsvariable aus?
Eine Funktion $P$, die jedem Wert eines ZV X die Wahscheinlichkeit $P(X=X_1)$ zuschreibt, heißt Wahrscheinlichkeitsverteilung der ZV X.

#### 2.2.1 Graphische Veranschaulichung der Wahrscheinlichkeitsverteilung

<div style="display: flex; gap: 1em; flex-direction: row;">
	<div class="img-25">
		<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM4AAAD0CAMAAADkIOk9AAAAwFBMVEX////m5uYAAAC7u7vAwMDQ0NCqqqq0tLRaWlrz8/Pg4ODGxsb8/Pz5+fn29vaBgYGWlpZRUVHa2tp0dHR6enrt7e1DQ0OlnZ1jWlre3t5mZmaHh4ecm5ukpKTR0dFhYWE3NzcdHR2Pj487OztKSkoXFxdWVlYrKysLCwumd3cwMDAUFBR9cHCvqKhLQEBubm4mJia8paWPd3emj4+PhIQlAAAWAACRhoYuAABxYWFDJyc2ERFXQkIhAAAYAAA3Jycf+eqdAAAIVElEQVR4nO2da2OiOhqAw8sdBAXBM3LxVqsdOx27u3PZ3bO75///qwWKikpiEcSXNs8H52CEk6chISR5gZCPhHDvDDTLx9cxOqxYknVRbD8bTVGmI7Wfjab4VDrOq+ZIxH7INtS4rUxdD1tnGaafav/tp/N2slSHC6WTiugwdp+IOiNDr718XckFnZWqjHVwhVc18MhQazFj13FBJ5jIfqJDLEjKqfs6byeb25tuN2r3dR6GJKs7MpAYyNBpL19XwtaxrPQzFolNehZxeq1l61recxk1IPtHnd4+O3V5V6/g7Ue6dfPc1OZTdXI6B13HaDknjUDVEfFfZEqg6OgODNvPTDUsXddPvyvRkcz0M9jePkP1UADg9Dv/7Ffhw0N6W1Cu47PuecIr01RGNXXpd/pqoqOdUNJvyUsH/cmmvqt0srpjD5/nQ+SXzTiSzoqO1rLplnVWzzpApy6jchwX6q4bR9HpLzqls0hri53T+xv4q9M+fqd0BonO16/Dv39NPjzPAeKdVu9O6SyO2jIVttDp0lHs4pZYkvdO6VyG62CG62CG67SJB0+jw1b0NL0wi4FcZwgwjwY5kfNALtzyI9fxANaCkSP01+TCuDJynSAMC73m0PP67N8j13GPti6PlSHXqQrXwQzXwQzXwQzXwQzXwQzXuS0jgMI9zRam6yp7o9NZAWzCfk64CS7dsB2DTscBWNl+jr119EoLgdDpLONIPWwFg3+8VNmbpmM6UycfnteXq0GN/FVEYGxV3Tsjm4iHMQk2b9uPEYGuLK2m6hgrWL5tr2d2h3WMKBYSHSkY5CNck/nTdDctZLFKn3Urz0rzbXqaXjIXzTjoefbEoScmOuAucp15NNmXjm4yjq5emSYzsixMGDuenzOUVR86qMRbkd58nrQ1fQIsC0zQWrZxchFL/gnT1Rr9fleqDr7rTj24Dma4Dma4Dma4Dma4TtPoum4Xt1gd7Esg0AGAwoznaLOoESaEQOcVYDPdrRyewqLa2M0xCHTmR6XjaJNul87MFAsT1EtJla8/FgIdi7FVFQQ6TcJ1MMN1MMN1MMN1MMN1MMN1MMN1MPNJdHRZ3k/j6fK4xRzVgqJjOaHq7NaXj/pdmUtkrCuQIZ/qXbLCv5FBneoVXlf5uoLZVKkxGNEu5zpZgL8OS2+3rmDmGbDzwRTgT8ji7Btq6UzJYkaImfz3a/cXsRBv6j2bpJdG0Ypz74G19qI63378KDQuv398Yy2iqAT1umNZaQBwr0d2j2ZqEPj567fh5gg//7C/NXXku1xG4Z8///XHjpefL6TjOv/+s7Do7s//fPnd1JHvovPC2KrHJ+mzdRSugxmugxmugxmugxmugxmugxmugxmugxmugxmugxmugxmugxmuc9X/RhDs4pZxo8cpt6OjAxQn8CDo3yjGnqYjOdPl4e85qznXayc6I+0QZ2Dq7eoUA/yJvq47N2qflE4Yt61jOLsAf7JWoOb5pzsTszC9upalqs9VeCdlAf6RkeiI291E/HwowG4BCDPAn7XUhRXgL9w0wN87CfAXFWX/jgebtZyFdUay0iasAH+XnkbOzxl6gL/laaT3/Jx+04PGZspvDDXAP8xi+7MPogz6+F+MlMF7BZjhOpjhOpjhOpjhOpjhOpjhOpjhOpjhOpjhOu877na4PYwb9YJg2krQzK10DABQJnKOCe5EaeCoF7mlzkLZEcO42zpjGG0OI34WrJat1Mhb6fhHjydlDp42CW/ZMMN1MMN1MMN1MMMI8N/3GWX5RhOzzUML8F8uxF2A/8JRn7rywAL6ugJzF+C/ijsdc70L8Nd26wqI+Xj5fXg4oAb4j/q7dQXEhP3Ef2cD/IMswF9KTjxpbpnNRsTfDmqAvzZ8ygP8YeZ1fl3BW2h/TkcWFZBPcxmtzmQ22hyqmLDRRqzlNDeiOR0TACI1H+tQI9DFOzxdp1kdcTcSJaugq93WGQ2Dw4JVYxNod+gZNacjHF2b9Pv0I3jLhhmugxmugxmugxmugxmug5k6OuqvVzhsyaCt7z5aWksnvWHb4wGJ7j4cV1fHHecYCvQWndZRgtA7bJmON7xRvOH7qaMjHD2R0r+7C+EtG24+hI6enOd+duZ/CB0JBBOyVvVD6BB5/vTWEFXTEWS5MBbomyaSx4hLm8e3YbFqOgOAQrdGBfN7008PvgoR/AlkI+LVdCL47/++7PkOxKvxQsDmSB/OnD2gubJOsXREiP9CUToHKp5sE6GwgyIad++knfAxWrY9JTr05srfBl8YtzSsZxCw0ljR/gar7TyfRs+O5MvwTuwXmZD9euJj3JFbnnAhbeKplCMmaUpITZNl5+igex1XUQuEoUohgl76fkalHHWmUlLYaUqwoKeFW3qaMioeNN7rnJQ9tXzdX1++MyY8h/QkZprCONlc1hKA/tk3lZoC5rMQUPDxWza6jiUxHzli0hMl+tIaQ5JoyzDSk0GQyk9+I7mA65J0srqmko42VF/pWU46CbSkxZKqI8zF7bY8SX5Mkl8Vc1ZSf/xnPX33TDw7vqWvpPNg9mBCS1Q2QIuaiJ5oO6XDc74KpSnBJtnNBTuG83ZkMILEYzPx4VigYt2JRrQBDnVD6DoQUS+jugZBVJ6kQKpjOKOSZnEMWUZC7bgPXE0nnlGTglkAa8o6sehZd2gL2lwwgfLq5DjT2SjbEp1JpnP2SuxKOoMlURnDT9RlYoNHsqW9vFoGQjnZ8tKJyLSkbo3BSsuGqDVKB0Yave4kf8w5pXT8eQC0JsTStHn5nyFYg+b2Am1asm9SdxyVwNKpV3eww3Uww3Uww3UwU6bTlYCDEkp0jLtP2F5Ph7NeBtfBjPB/Vr5qxCQh6esAAAAASUVORK5CYII=">
	</div>
	<div>
		<h4>Kumulative Wahrscheinlichkeitsverteilung</h4>
		<p>Eine Funktion <math class="math">F</math>, die jedem Wert <math class="math">x</math> einer ZV <math class="math">X</math> die Wahrscheinlichkeit <math class="math">P(x\le x)</math> zuordnet, heißt WKV.</p>
		<ul>
			<li><math class="math">W=[0;1]\;D=\mathbb{R}</math></li>
			<li><math class="math">\lim_{x\to -\infty}{F(x)}=0; \lim_{x\to\infty}{F(x)}=1</math></li>
			<li>monoton steigend</li>
		</ul>
	</div>
</div>


<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); width: 100%; margin: 1em 0em;">
	<div style="grid-column: 1; text-align: center;">
		<h2>Erwartungswert</h2>
		<math class="math">{\displaystyle E(x)=\sum_{i=1}^{n}{x_i \cdot P(X=x_i)}}</math>
	</div>
	<div style="grid-column: 2; text-align: center;">
		<h2>Varianz einer Zufallsgröße</h2>
		<math class="math">{\displaystyle \operatorname {Var} (X) := \sum_{i=1}^{n}{\left(E(X_i) - X_i\right)^2 \cdot P(X=X_i)}}</math>
	</div>
</div>

Die Varianz gewichtet die Abweichungen vom Erwartungswert auf Grund des Quadrats sehr starkt. Deshalb ist ein weiteres oft besseres Maß, die sogenannte Standartabweichung die bessere Wahl: $\sigma = \sqrt{Var(X)}$

## 5 Ziehen aus einer Urne mit Beachtung der Reihenfolge
**Ziehen mit BdR und mit Zurücklegen**
$n$ Kugeln, $k$ mal ziehen -> $n^k$ Ergebnisse möglich (k-Tupel)

<br>

**Ziehen mit BdR und ohne Zurücklegen**
$n$ Kugeln, $k$ mal ziehen -> $\frac{n!}{(n-k)!}$ Ergebnisse möglich

## 6 Ziehen aus einer Urne ohne Beachtung der Reihenfolge

**Ziehen ohne BdR und mit Zurücklegen**
$n$ Kugeln, $k$ mal ziehen -> ${n+k-1 \choose k}=\frac{(n+k-1)!}{k!(n-1)!}$ Ergebnisse möglich

<br>

**Ziehen ohne BdR und ohne Zurücklegen**
$n$ Kugeln, $k$ mal ziehen -> ${n \choose k}\frac{n!}{k!(n-k)!}$ Ergebnisse möglich (Binomialkoeffizient)

Wichtiger Sonderfall: zwei Sorten von Kugeln (rot/blau)
Insgesamt $N$ Kugeln; $S$ rote, $n$ werden gezogen
Wahrscheinlichkeit für $s$ rote Kugeln: $P(X=s)=\frac{{S \choose s} \cdot {N-S \choose n-s}}{N \choose n}$

## 7 Bernoulli-Experimente und Bernoulli-Kette
### Bernoulli-Experiment
Ein Bernoulli-Experiment ist ein wahrscheinlichkeitstheoretisches Experiment, bei dem es nur zwei mögliche Ausgänge gibt, die beide mit einer bestimmten Wahrscheinlichkeit eintreten können. Ein Beispiel für ein Bernoulli-Experiment ist das Werfen einer Münze, bei dem entweder Kopf oder Zahl herauskommen kann. Jedes Mal, wenn die Münze geworfen wird, gibt es nur zwei mögliche Ergebnisse: Kopf oder Zahl, die beide mit der Wahrscheinlichkeit von 0,5 eintreten können.

Ein Bernoulli-Experiment kann auch durch das Rollen eines Würfels dargestellt werden, bei dem entweder eine 1, 2, 3, 4, 5 oder 6 herauskommen kann. Auch in diesem Fall gibt es nur zwei mögliche Ergebnisse: Eine gerade oder ungerade Zahl.

Bernoulli-Experimente werden häufig in der Statistik und der Wahrscheinlichkeitstheorie verwendet, um das Verhalten von Zufallsvariablen und das Auftreten von Ereignissen zu untersuchen und zu modellieren. Sie sind auch in vielen Anwendungen in den Naturwissenschaften, der Medizin und der Ökonometrie von großer Bedeutung.

### Bernoulli-Kette
Eine Bernoulli-Kette wird durch eine Folge von Bernoulli-Experimenten repräsentiert, bei denen jedes Experiment nur zwei mögliche Ausgänge hat. Jedes Mal, wenn das Experiment durchgeführt wird, gibt es nur zwei mögliche Ergebnisse, die beide mit einer bestimmten Wahrscheinlichkeit eintreten können. Die Wahrscheinlichkeiten für die beiden möglichen Ergebnisse bleiben in jedem Experiment gleich.

$$f(k;p)=pk+(1-p)(1-k)$$

## 8 Binomialverteilung
Die Binomialverteilung ist eine wichtige Wahrscheinlichkeitsverteilung, die beschreibt, wie häufig bestimmte Ereignisse in einer Folge von Bernoulli-Experimenten auftreten. Die Binomialverteilung wird häufig verwendet, um zu berechnen, wie wahrscheinlich es ist, dass eine bestimmte Anzahl von Erfolgen in einer Folge von Bernoulli-Experimenten auftritt. Die Binomialverteilung wird durch drei Parameter beschrieben: $n$, $p$ und $x$. Der Parameter $n$ gibt an, wie viele Bernoulli-Experimente durchgeführt werden, während $p$ die Wahrscheinlichkeit für das Eintreten des Erfolgs in einem einzelnen Experiment beschreibt. Der Parameter $x$ gibt an, wie viele Ergebnisse zutreffen. 
$$P(X=k) = {n \choose k} p^{k} (1-p)^{n-k}=B(n;p;k)$$

## 9 Die 3-M Aufgaben
"Wie viele Personen müssen mindestens getestet werden, damit mit einer Wahrscheinlichkeit von mindestens 99% mindestens eine Testperson infiziert ist?" 
<br>

<p class="external-refference"><span>Bsp</span> p=0,01</p>

$P(X \ge 1) \ge 0,99$
$1- P(X = 0) \ge 0,99$
${n \choose 0} \cdot p^0 \cdot (1-p)^{n} \le 0,01$
$(1-p)^{n} \le 0,01$
$ln((1-p)^n) \le \ln(0,01)$
$n \ge \frac{ln(0,01)}{ln(1-p)} \ge \frac{ln(0,01)}{ln(0,99)} \ge 458,21$ -> $n$ muss mindestens $489$ sein

## 10 Erwartungswert und Varianz von Bernoulli Experimenten
Eine binomialverteilte Zufallsvariable $X$ (mit $n$ und $p$) hat den Erwartungswert $\mu = E(x) = n \cdot p$ und die Varianz $Var(X)=n \cdot p \cdot q$. Für die Standartabweichung gilt dann $\sigma = \sqrt{n \cdot p \cdot q}$

> Ist der Erwartungswert eine natürliche Zahl, dann ist dieser Wert automatisch der wahrscheinlichste der entspechenden Binomialverteilung.
> Ist der Erwartungswert keine natürliche Zahl, dann sind die nächst gelegenen natürlichen Zahlen die wahrscheinlichsten der entsprechenden Binomialverteilung.

<br>
<p class="external-refference"><span>Bsp</span>n=15; p=0,5</p>

$E(X)=np=7,5$ -> die wahrscheinlichsten Werte sind $7$ und $8$ un sie haben den selben Wert -> nur bei $p=0,5$ ist die Binomialverteilung symmetrisch. 