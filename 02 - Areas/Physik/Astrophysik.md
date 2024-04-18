# 0. Wozu Astronomie / Astrophysik
<div class="grid-container">
	<span class="vertical-center background-252525">
		<h4 style= "grid-column: 1;">Zukunft</h4>
	</span>
	<ul class="ul-background" style= "grid-column: 2;">
		<li>Wo ist Leben möglich?</li>
		<li>Wo sind Kolonien möglich?</li>
	</ul>
	<span class="vertical-center background-252525">
		<h4 style= "grid-column: 1;">Neugierde</h4>
	</span>
	<ul class="ul-background" style= "grid-column: 2;">
		<li>Entstehung vom Universum</li>
		<li>Entstehung vom Sonnensystem</li>
	</ul>
	<span class="vertical-center background-252525">
		<h4 style= "grid-column: 1;">Wissenschaft</h4>
	</span>
	<ul class="ul-background" style= "grid-column: 2;">
		<li>Ressourcen z.B. He3</li>
		<li>Satteliten</li>
	</ul>
	<span class="vertical-center background-252525">
		<h4 style= "grid-column: 1;">Gefahrenabwehr</h4>
	</span>
	<ul class="ul-background" style= "grid-column: 2;">
		<li>Ablenken von Asteroiden</li>
	</ul>
</div>

# 1. Himmelskörper
## 1.1 Kleine Himmelskörper
### 1.1.1 Komet
- Durchmesser von einigen Kilometern
- Entwickelt Schweif in Sonnennahen Regionen seiner Umlaufbahn
- Enthalten Flüssigkeiten, Gase und Staub
	- Staub und Wasserdampf (Koma)
	- Gas (Ionenschweif)
### 1.1.2 Meteoroide
- Bruchstücke von Asteroiden, Kometen und manchmal auch Planeten
- Sehr klein und sehr leicht
	- Verglühen bei Eintritt in die Atmosphäre -> Meteor / Sternschnuppe
	- Treffen auf die Erde -> Meteorit
### 1.1.3 Asteroid
- unregelmäßig geformte Gesteinbrocken
- einige Meter bis einige tausend Meter Durchmesser
- Zusammensetzung aus Gestein und Metallen

## 1.2 Planeten
### 1.2.1 Zwergplaneten
- Anerkannt: Eris, Pluto, Haumea, Ceres und Makemake
- Kandidaten: Quaoar, Sedna und Orcus
- Definition
	- Umlaufbahn um die Sonne
	- Außreichende Masse, um eine Kugelform zu halten
	- Planetarische Diskriminante $\micro<100$

# 2. Sonnensystem
## 2.1 Grundlegendes
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sonnensystem-Grafik.pdf/page1-2560px-Sonnensystem-Grafik.pdf.jpg" class="img-15">

[Solar System Explorer](Information.html)
[Solar System Animation](Animation.html)

## 2.2 Entstehung des Sonnensystems
<p class="external-refference"><span>VID</span>Pirouetten-Effekt</p>

#### Drehimpuls
![[Impuls#Drehimpuls]]

## 2.3 Kepler
![[Kepler#Keplersche Gesetze]]

## 2.4 Entfenrungen im Sonnensystem
<div style="display: flex; gap: 15px"><p>Problem</p><p>KG3 Liefert nur Verhältnisse von Entfernungen. Nur wenn ein Ausgangswert (z.B. <math>1AE</math>) schon bekannt ist, liefert es absolute Werte.</p></div>
<br>

<div style="display: flex; gap: 15px"><p>Bestimmung von 1AE</p><p><span class="math inline">d_e = 1AE</span><br><span class="math inline">T_e=1a; \space T_v = 0,62a</span></p></div>
<br>

<div style="display: flex; gap: 15px"><p>Mit Hilfe ds KG3</p><p><span class="math inline">1\frac{a^2}{AE^3} = \frac{T_v^2}{a_v^3}</span><br>
-> <span class="math inline">d_v = 0,727AE</span><br>
-> <span class="math inline">d_r = 0,273AE</span></p></div>
<br>

<div style="display: flex; gap: 15px"><p>Trick: Radarsignal zur Venus & zurück</p><p><span class="math inline">t=\frac{1}{2}276,3s=183,15s</span><br>
<span class="math inline">d_r=c \cdot t</span><br>
<span class="math inline">1AE=1,5 \cdot 10^{11} m = 1,5 \cdot 10^8km</span></p></div><br>

## 2.5 Massebestimmung von Himmelskörpern
Ein Himmelskörper $(Z, Masse\space M)$ wird von einem anderen Körper $(K, Masse\space m)$ auf einer (praktisch) Kreisförmigen Bahn umrundet. Dann lässt sich die Masse von $Z$ bestimmen. 

---
$F_G=F_Z$ <- Standardansatz
$G \cdot \frac{m \cdot M}{r^2}= m \cdot \omega^2 r$
$M = \frac{\omega^2 \cdot r^3}{G} = \frac{4\pi^2 \cdot r^3}{T^2 \cdot G}$
$r$ Abstand zwischen $Z$ und $K$
$T$ Umlaufdauer von $K$ um $Z$
---
Merkur und Venus haben keine Monde $(K)$. Diese können bestimmt werden, indem man einen künstlichen Mond erzeugt (z.B. ein Satellit).
<br>

$M_{Sonne} = \frac{\omega^2 \cdot r^3}{G} = \frac{4\pi^2 \cdot r^3}{T^2 \cdot G} = \frac{4\pi^2 \cdot (1AE)^3}{(1a)^2 \cdot G} = 1,99 \cdot 10^{30}kg$

$M_{Erde} = \frac{\omega^2 \cdot r^3}{G} = \frac{4\pi^2 \cdot r^3}{T^2 \cdot G} = \frac{4\pi^2 \cdot (384400km)^3}{(27d)^2 \cdot G} = 5,97 \cdot 10^{24}kg$

## 2.6 Die Grenzen der Keplerschen Gesetze
![[Kepler#Grenzen]]

## 2.7 Bewegungen im Gravitationsfeld
### 2.7.1 Vis-viva-Gleichung

<div style="display: flex; gap: 1em;">
	<div style="display: inline-block; flex-grow: 2;">
		<p>
			Himmerlskörper <span class="math inline">K</span> auf elliptischer Bahn (große Halbachse <span class="math inline">a</span>) um einen Zentralkörper <span class="math inline">Z</span> (Masse <span class="math inline">M</span>). Abständ zwischen <span class="math inline">Z</span> und <span class="math inline">K</span> ändert sich ständig. <br>
			Seine Geschwindigkeit lässt sich in Abhängigkeit von <span class="math inline">r</span> bestimmen.<br>
			<span class="math inline" style="display: inline-block; text-align: center;">
				v=\sqrt{G \cdot M \left( \frac{2}{r} - \frac{1}{a} \right)}
			</span>
		</p>
	</div>
	<div class="img-25" style="width: 50%">
		<img src="https://upload.wikimedia.org/wikipedia/commons/1/1d/Angular_Parameters_of_Elliptical_Orbit.png">
	</div>
</div>

### 2.7.2 Die Hohmannbahn
<div style="display: flex; gap: 1em; margin-bottom: 2em;">
	<div>
		<p>Die sogenannte HMB ist die Bahn, die am energieeffizientesten ist. </p>
		<p>Sie stellt eine <a href="Mathe/Ellipse.md" class="internal-link">Ellipse</a> mit dem Zentralkörper in einem Brennpunkt dar, bei der Start- und Zielpunkt im Perihel bzw. Aphel liegen.</p>
		<div style="margin-top: 2em">
			<p class="external-refference"><span>Bsp</span> Reise zum Mars</p>
			<math class="math inline">a_{HMB}=\frac{1}{2}(a_M+a_E)=\frac{1}{2}(1,5AE+1AE)=1,25AE</math>
			<math class="math inline">v_p=\sqrt{G \cdot M \left( \frac{2}{r} - \frac{1}{a_{HMB}} \right)}=\sqrt{G \cdot 2 \cdot 10^{30}kg \left( \frac{2}{149,6\cdot10^{9}m} - \frac{1}{1,25 \cdot 149,6\cdot10^9m} \right)}</math>
			<math class="math inline">\;=32721,08676\frac{m}{s}=32,7\frac{km}{s}</math>
			<p style="margin-left: 2.5em">-> Momentane Geschwindigkeit, die die Rakete im Perihel haben muss</p>
			<p style="margin-left: 2.5em">-> Muss nur<span class="math inline">2,7\frac{km}{s}</span> schnell sein, da sich die Erde bereits mit <span class="math inline">30\frac{km}{s}</span> bewegt</p>
		</div>
	</div>
	<div class="img-25" style="width: 50%; flex-grow: fit-content; height: fit-content;">
		<img src="https://img.zeit.de/2020/24/raumfahrt-mars-grafik/original__1000x648">
	</div>
</div>

**Zeitdauer**:  Mit KG3 gilt:
$\frac{T_{HMB}^2}{a_{HMB}^3}=\frac{T_{Erde}^2}{a_{Erde}^3}$ -> $T_{HMB}=\left(\frac{a_{HMB}}{a_{Erde}}\right)^{\frac{3}{2}}\cdot T_{Erde}=\left(\frac{1,25AE}{1AE}\right)^{\frac{3}{2}}\cdot 1a=1,3975a$
-> $F_{Flug}=\frac{1}{2}\cdot T_{HMB}=0,698a=255d$

### 2.7.3 Die kosmischen Geschwindigkeiten
Als erste kosmische Geschwindigkeit $v_1$ bezeichnet man diejenige Geschwindigkeit, mit der ein Körper horizontal von der Erdoberfläche abgeschossen werden müsste, um antriebslos auf einer Kreisbahn an der Erdoberfläche zu bleiben, ohne auf die Erdoberfläche zurückzufallen.
Der Wert der ersten kosmischen Geschwindigkeit beträgt $v_1 = 7,910 \frac{km}{s}$.

Als zweite kosmische Geschwindigkeit $v_2$ bezeichnet man diejenige Geschwindigkeit, mit der ein Körper von der Erdoberfläche abgeschossen werden müsste, um antriebslos das Gravitationsfeld der Erde zu verlassen. Die Eigenrotation der Erde und mögliche Swing-By-Manöver am Mond oder anderen Planeten werden dabei nicht berücksichtigt.
Der Wert der zweiten kosmischen Geschwindigkeit beträgt $v_2 = 11,19 \frac{km}{s}$.

Als dritte kosmische Geschwindigkeit $v_3$ bezeichnet man diejenige Geschwindigkeit, mit der ein Körper von der Erdoberfläche abgeschossen werden müsste, um antriebslos die Gravitationsfelder von Sonne und Erde zu verlassen. Die Bahngeschwindigkeit der Erde um die Sonne wird dabei berücksichtigt, die Eigenrotation der Erde und mögliche Swing-By-Manöver am Mond oder anderen Planeten dagegen nicht.
Der Wert der dritten kosmischen Geschwindigkeit beträgt ungefähr v3≈16,67kms $v_3 = 16,67 \frac{km}{s}$.

### 2.7.4 Swing-By-Manöver
Neben der HMB werden noch weitere Bahnen in der Raumfahrt benutzt, z.B. das Swing-By-Manöver (um Treibstoff zu sparen).
Dadurch kann $|\vec{v}|$ verändert werden, oder die Richtung von $\vec{v}$

# 3 Die Sonne
## 3.1 Der Radius der Sonne
Scheinbare Winkelgröße der Sonne: $\alpha = 32' \left(=\frac{32}{60}\right) = 0,53°$
$tan\left(\frac{\alpha}{2}\right)=\frac{d}{2r}$
$d=tan\left(\frac{\alpha}{2}\right) \cdot 2r = 1392550 km$
$r=696275km$
Literaturwert: $696340km$

## 3.2 Das Sonnenspektrum
### 3.2.1 Die Elektromagnetische Strahlung

![[Elektromagnetische Strahlung]]

### 3.2.2 Grunsätzliches zu Spektren
- Die Spektren brennender oder glühender Festkörper sind kontinuierlich.
- Zum leuchten angeregte Gase erzeugen Linienspektren

### 3.2.4 Fraunhoferlinien
Die Fraunhoferlinien oder Fraunhoferschen Linien sind im engeren Sinne eine Reihe von mit Buchstaben bezeichneten Absorptionslinien im Spektrum der Sonne.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Fraunhofer_lines_DE.svg/2560px-Fraunhofer_lines_DE.svg.png" style="background: white; border-radius: 25px; margin: 1em 0em;">

Sonne besteht aus $75\%$ Wasserstoff, $23\%$ Helium und $2\%$ Metalle

## 3.3 Die Energieabstrahlung der Sonne
### 3.3.1 Solarkonstante und Leuchtkraft

<div style="display: grid;">
	<div style="grid-column: 1; grid-row: 1;">
		<h4>Solarkonstante</h4>
		<p>Die im Abstand von <math class="math inline">1AE</math> senkrecht auf die Oberfläche von einem Quadratmeter auftreffende Strahlung hat die Leistung <math class="math inline">S=1,367 \frac{kW}{m^2}</math> ("Solarkonstante")</p>
	</div>
	<div style="grid-column: 1; grid-row: 2;">
		<h4>Leuchtkraft</h4>
		<p>Die gesamte Strahlungsleistung der Sonne beträgt: <br><math class="math inline">L=4\pi D^2 \cdot S=4\pi \cdot (149,6\cdot 10^{9}m)^2 \cdot 1367 \frac{W}{m^2}=3,845 \cdot 10^{26} W</math></p>
	</div>
	<div style="grid-column: 2; grid-row: 1 / span 2;">
		<h4>Vergleich</h4>
		<ul>
			<li>Glühbrine: <math class="math inline">40-100W</math></li>
			<li>LED: <math class="math inline">2-4W</math></li>
			<li>Deutschland 2019: <math class="math inline">5,12\cdot 10^{12}kWh</math> <br>-> Mit der Energie, die die Sonne in einer Sekunde abstrahlt, ließe sich der Energiebedarf Deutschlands 20 Mio. Jahre decken</li>
		</ul>
	</div>
</div>

### 3.3.2 Strahlungsgesetze
Wie kann man die Temperatur der Sonne bestimmen?
Wärme kann transportiert werden durch: Wärmestrahlung, Konvektion, Wärmeleitung

### 3.3.3 Anwenung der Strahlungsgesetzte
#### Oberflächentemperatur der Sonne
Die Sonne ist in guter Näherung ein schwarzer Strahler
Die Oberflächentemperatur lässt sich über die emittierte Strahlung bestimmen

- Wiensche VG: $T = \frac{ b }{ \lambda_{max} } = \frac{ 2,9 \cdot 10^{ -3} mK }{ 500 \cdot 10^{ -9 } m } = 5800K$
- Stefan-Boltzmann-Gesetz: $T = \sqrt[4]{ \frac{ \Phi }{ A \cdot \sigma } } = \sqrt[4]{ \frac{ 3,845 \cdot 10^{ -26 } }{ 4\pi \cdot (6,957 \cdot 10^8 m)^2 \cdot \sigma } } = 5800K$

#### Oberflächentemperatur der Erde
Die Erde erzeugt im Gegensatz zur Sonne (fast) keine Energie selbst. Sie erhält ihre Energie durch Bestrahlung von der Sonne. Die Erde befindet sich im Strahlungsgleichgewicht. -> $P_{ab} = P_{em}$
Albedo $0,34$ -> $0,66 \cdot S \cdot A = \sigma \cdot A \cdot T^4$
$0,66 \cdot S \cdot \pi r^2 = \sigma \cdot 4\pi r^2 \cdot T^4$
$T = \sqrt[4]{ \frac{ 0,66 \cdot S }{ 4 \cdot S } } = 251,14K \approx -22°C$ -> Temperatur der Erde ohne den Treibhauseffekt
Realer Wert: $14°C$ -> Unterschied Hauptsächlich durch den Treibhauseffekt (mittlerweile auch anthropogener THE)

## 3.4 Kernfusion
![[Kernfusion]]

### 3.4.3 Der pp-Prozess
<div style="display: flex; gap: 1em;">
	<img src="https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg" style="width: 25%; background: white; padding: 1em; border-radius: 1em;">
	<div style="width: max-content; background: #1e1e1e; padding: 1em; border-radius: 1em; height: max-content;">
		<p>Proton-Proton-Reaktion (p-p-Reaktion)</p>
		<p class="math">H1 + H1 \to H2 + e^+ + v + 0,42MeV</p>
		<p class="math">H2 + H1 \to He3 + \gamma + 5,49MeV</p>
		<p class="math">He3 + He3 \to He4 + 2 \cdot H1 + 12,85MeV</p>
		<br>
		<p class="math">e^+: Positron</p>
		<p class="math">v: Neutrino</p>
		<p class="math">\gamma: Gammaquant</p>
	</div>
</div>

### 3.4.4 Der Tunneleffekt
### 3.4.5 Der CNO-Zyklus
<div>
	<math class="math">
		\begin{array}{} {}^{12}{\mathrm{C}} + {}^1{\mathrm{H}} \rightarrow {}^{13}\mathrm{N} + \gamma +1{,}95\,\rm{MeV}\\ \, \\ {}^{13}\mathrm{N} \rightarrow {}^{13}\mathrm{C} + \mathrm{e}^+ + \nu_\mathrm{e}+1{,}37\,\rm{MeV} \\ \, \\ {}^{13}\mathrm{C} + {}^1{\mathrm{H}} \rightarrow {}^{14}\mathrm{N} + \gamma +7{,}54\,\rm{MeV} \\ \, \\ {}^{14}\mathrm{N} + {}^1{\mathrm{H}} \rightarrow {}^{15}\mathrm{O} + \gamma+7{,}35\,\rm{MeV} \\ \, \\ {}^{15}\mathrm{O} \rightarrow {}^{15}\mathrm{N} + \mathrm{e}^+ + \nu_\mathrm{e} +1{,}86\,\rm{MeV}\\ \, \\ {}^{15}\mathrm{N} + {}^1{\mathrm{H}} \rightarrow {}^{12}{\mathrm{C}} + {}^{4}{\mathrm{He}}+4{,}96\,\rm{MeV} \end{array}
	</math>
</div>

## 3.5 Aufbau der Sonne
- Innerer Kern
- Strahlungszone
- Konvektionszone
- Photosphäre
- Chromosphäre
- Corona

## 3.6 Lebensdauer der Sonne
$2 \cdot 10^{30} kg \cdot 0,75 \cdot 0,1 = 0,15 \cdot 10^{30} kg$ -> Wasserstoff, der fusioniert werden kann
$26,2 Mev$ entspricht $4,67 \cdot 10^{-29}kg$ (pp-Zyklus)
Strahlungsleistung der Sonne: $3,845 \cdot 10^{26} W$
$\frac{\Delta m}{m} = 6,98 \cdot 10^{-3}\approx0,7\%$ -> Es werden $0,7\%$ der Masse in Energie umgewandelt
-> $0,15 \cdot 10^{30} kg \cdot 0,007 = 1,05 \cdot 10^{27} kg$
-> $\frac{1,05 \cdot 10^{27} kg}{4,67 \cdot 10^{-29}kg} \cdot 26,2MeV = 5,89 \cdot 10^{56}MeV=9,438 \cdot 10^{43}J$
-> Lebensdauer: $\frac{E}{L}=\frac{9,438 \cdot 10^{43}J}{3,845 \cdot 10^{26}W} = 2,4546 \cdot 10^{17}s = 7,78 \cdot 10^9 a$
-> Genaueres Ergebnis: $\tau = 10 \cdot 10^9 a$

# 4 Sterne
## 4.1 Entfernungsbestimmung mit der jährlichen Paralaxe
-   Nahe Fixsterne scheinen im Laufe eines Jahres bei der Beobachtung von der Erde aus vor dem weit entfernten Sternenhintergrund etwas zu wandern.
-   Ursache dafür ist, dass sich die Erde im Laufe eines Jahres einmal um die Sonne bewegt.
-   Mithilfe der beobachteten jährlichen Parallaxe $p$ kann die Entfernung relativ naher Sterne (mit einfachen Teleskopen vom Erdboden bis ca. $100pc=326Lj$) berechnet werden. Mit speziellen Raumsonden (z.B. Gaia) erhöht sich die Reichweite erheblich.

$$r=\frac{ 1,0" }{ p } \cdot 1pc$$

## 4.2 Die Bewegung von Sternen 
![[IMG_20230228_092655.jpg]]
$$v=\sqrt{ v_e^2 + v_r^2 }$$
$$tan(\phi)=\frac{v_e \cdot \Delta t}{r}$$
$$v_e=\frac{r \cdot tan(\phi)}{\Delta t}$$

## 4.3 Die Radialgeschwindigkeit von Sternen
![[Dopplereffekt]]

## 4.4 Die scheinbare Helligkeit von Sternen
Beziehung zwischen scheinbaren Helligkeiten: $m_1 - m_2 = -2,5 \cdot lg\left( \frac{E_1}{E_2} \right)$
- $E_1$, $E_2$ sind die Bestrahlungsstärken der beiden Sterne
- $E=\frac{L}{4 \pi \cdot r^2}$ ($r$ ist der Abstand zum Stern)

## 4.5 Die absolute Helligkeit von Sternen
Entfernungsmodul: $m-M = 5 \cdot lg\left(\frac{r}{10pc}\right)$ 
Beziehung zwischen absoluten Helligkeiten: $M_1 - M_2 = -2,5 \cdot lg\left( \frac{L_1}{L_2} \right)$
- $L_1$, $L_2$ sind die Leuchtkräfte der beiden Sterne

-> Entfernungsberechnung: $r=10^{0,2(m-M)} \cdot 10pc$

## 4.6 Spektralklassen
