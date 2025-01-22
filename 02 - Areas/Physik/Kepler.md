---
date: 2024-04-17T20:14
tags:
  - Informatik
cssclasses: []
---
# Keplersche Gesetze
**Erstes Keplersches Gesetz**
Die Planeten bewegen sich auf [[Ellipse|elliptischen]] Bahnen. In einem ihrer Brennpunkte steht die Sonne.

<br>

**Zweites Keplersches Gesetz**
Ein von der Sonne zum Planeten gezogener Fahrstrahl überstreicht in gleichen Zeiten gleich große Flächen.

<br>

**Drittes Keplersches Gesetz**
Die Quadrate der Umlaufzeiten zweier Planeten verhalten sich zueinander wie die Kuben (dritten Potenzen) der großen Halbachsen ihrer [[Ellipse|Bahnellipsen]].

<br>

> $$C = \frac{T^2}{a^3} = \frac{4 \cdot \pi ^2}{G \cdot m_{\rm{Zentralkörper}}}$$

<br>

>$$F_G = F_Z$$
>$$G \cdot \frac{m_S \cdot m_P}{r^2} = m_{\rm{P}} \cdot \omega^2 \cdot r_{\rm{P}}$$

<br>

# Grenzen

<div style="display: flex; width: 100%; gap: 1em; margin-bottom: 1em;">
	<div class="img-25" style="width: 100%">
		<img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Apsidendrehung.png">
	</div>
	<div style="display: inline-block; padding: 1em; background: #1e1e1e; border-radius: 25px;">
		<p class="external-refference"><span>Animation</span>Periheldrehung</p>
		<p style="font-weight: bold; color: white;">Korrektur des 1. KG</p>
		<p style="color: white;">Die Planeten umlaufen die Sonne nicht auf perfekten <a href="Mathe/Ellipse.md" class="internal-link">Ellipsen</a>. Die Bahn der Planeten wird durch gravitative Einflüsse der anderen Planeten gestört. Diese Änderung beträgt auf der Erde <math class="math inline">0,32°</math> pro Jahrhundert.</p>
	</div>
</div>
<div style="display: flex; width: 100%; box-sizing: border-box; gap: 1em; margin-bottom: 1em;">
	<div style="display: inline-block; padding: 1em; background: #1e1e1e; border-radius: 25px; flex-grow: 2;">
		<div style="display: inline-block;">
			<p class="external-refference"><span>Animation</span>Schwerpunktsbewegung</p>
			<p style="margin-bottom: 10px; color: white;">Der Zentralkörper ruht nicht im Brennpunkt der <a href="Mathe/Ellipse.md" class="internal-link">Ellipse</a>. Zentralkörper und umkreisendender Körper drehen sich um den gemeinsamen Schwerpunkt.</p>
		</div>
		<div style="display: flex; margin-top: 1em;">
			<div style="display: inline-block; flex-grow: 1; text-align: center;">
				<math class="math inline" style="color: white;">F_{Z_1}=F_{Z_2}</math><br>
				<math class="math inline" style="color: white;">M \cdot \omega_1^2 \cdot r_1 = m \cdot \omega_2^2 \cdot r_2</math><br>
				<math class="math inline" style="color: white;">\omega_1 = \omega_2</math>
			</div>
			<div class="red-box" style="flex-grow: 1;">
				<p>Schwerpunktsatz</p>
				<math class="math inline" style="color: white;">M \cdot r_1 = m \cdot r_2</math>
			</div>
		</div>
	</div>
	<div class="img-25" style="width: 100%;">
		<img src="https://upload.wikimedia.org/wikipedia/commons/5/59/Orbit3.gif">
	</div>
</div>
<div style="display: flex; background: #1e1e1e; padding: 1em; border-radius: 25px; flex-direction: column; margin-bottom: 1em;">
	<p style="color: white;">
		Weiteres "Problem": die Keplerkonstante aus KG3 ist nur in erster Näherung konstant. <br> &#10230 <math class="math inline">\frac{T^2}{a^3}</math> nochmal genau anschauen! &#10230 Kreisbewegung: <math class="math inline">\frac{T^2}{r^3}</math>
	</p>
	<div style="display: flex; margin-top: 1em; max-width: 100%;">
		<div style="display: inline-block; text-align: center; flex-grow: 1;">
			<math class="math inline" style="color: white;">F_G = F_Z</math><br>
			<math class="math inline" style="color: white;">G \cdot \frac{m \cdot M}{r^2} = M \cdot \omega^2 \cdot r_1</math><br>
			<math class="math inline" style="color: white;">G \cdot \frac{m}{r^2} = \left(\frac{2\pi}{T}\right)^2 \cdot \frac{m}{M+m} \cdot r</math><br>
			<math class="math inline" style="color: white;">\frac{G}{r^3} = \frac{4\pi^2}{T^2(M+m)}</math>
		</div>
		<div class="red-box" style="flex-grow: 1;">
			<p>Verallgemeinerung von KG3</p>
			<span class="math block" style="color: white;">\frac{T^2}{(r_1 + r_2)^3} = \frac{4\pi^2}{G(M+m)}</span>
		</div>
	</div>
</div>