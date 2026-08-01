---
date: 2026-07-31
tags:
  - Computergrafik
  - LMU
  - Licht
  - Material
  - Phong
  - Shader
  - Texturen
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Rasterisierung]] | Nächstes Thema: [[Shading & Rendering]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu Licht, Aussehen & Material:
> - Physik von Licht & Abstandsgesetz in Natur vs. Computergrafik
> - [[Licht, Aussehen & Material#Lichtquellen in der Computergrafik|Lichtquellentypen in der CG]] (Ambient, Directional, Point, Spot)
> - Schattenbildung (Kern- vs. Halbschatten, [[Licht, Aussehen & Material#Shadow Mapping (Schattenmap-Verfahren)|Shadow Mapping]])
> - Lokale Beleuchtungsmodelle ([[Licht, Aussehen & Material#Das Phong-Beleuchtungsmodell|Phong & Blinn-Phong]])
> - [[Licht, Aussehen & Material#Texturen & Mappings (Texture Mapping)|Texturen & Mappings]] (UV-Mapping, Filtering, Normal/Bump/Displacement Mapping)
> - Prozedurale Oberflächen & [[Licht, Aussehen & Material#Prozedurale Oberflächen & Shader|Shader]]

## Licht in der Natur vs. Computergrafik

Licht lässt sich physikalisch als [[Elektromagnetische Strahlung|elektromagnetische Welle]] oder Photonenstrom beschreiben. Das menschliche Auge deckt einen riesigen Dynamikumfang ab, den digitale Displays nur näherungsweise darstellen können.

### Das Abstandsgesetz (Inverse Square Law)

> [!note] Physikalische Realität In der Natur fällt die Lichtintensität $I$ quadratisch mit der Entfernung $d$ zur Lichtquelle ab:
>
> $$I(d) \propto \frac{1}{d^2}$$
>
> - **Grund**: Die emittierte Energie verteilt sich auf eine Kugeloberfläche $A = 4\pi d^2$, deren Fläche quadratisch mit dem Radius wächst.
>
> [!warning] Warum die Physik in der CG oft angepasst wird Eine strikte $1/d^2$-Dämpfung führt in der Computergrafik zu Problemen:
> - Objekte sehr nahe an der Lichtquelle werden extrem überbelichtet (Überstrahlen).
> - Objekte in mittlerer Distanz werden zu schnell dunkel.
>
> Daher nutzt man in der Praxis oft eine **gemilderte Dämpfungsformel**:
>
> $$f_{att}(d) = \frac{1}{a + b \cdot d + c \cdot d^2}$$
>
> Oft wird die Dämpfung im interaktiven Rendering sogar komplett auf $1$ gesetzt (keine Dämpfung), um eine gleichmäßige Ausleuchtung zu garantieren.

## Lichtquellen in der Computergrafik

Um reale Beleuchtung in Echtzeit anzunähern, nutzt man vereinfachte abstrakte Lichtquellentypen:

> [!tip] Übersicht der Lichtarten
> - **Ambientes Licht (Ambient Light)**:
>     - Richtungslose, globale Grundhelligkeit.
>     - Simuliert Mehrfachreflexionen im Raum, ohne sie aufwendig zu berechnen.
>     - Beleuchtet alle Oberflächen in alle Richtungen gleich stark.
> - **Gerichtetes Licht (Directional / Distant Light)**:
>     - Simuliert unendlich weit entfernte Lichtquellen (z. B. die Sonne).
>     - Besitzt **keine Position**, sondern nur einen festen Richtungsvektor.
>     - Alle Lichtstrahlen verlaufen parallel zueinander.
> - **Punktlicht (Point Light)**:
>     - Besitzt eine feste Position im Raum und strahlt gleichmäßig in alle Richtungen ab.
> - **Spotlicht (Spot Light)**:
>     - Strahlungsbereich ist auf einen Kegel eingeschränkt (Position, Richtung, Öffnungswinkel/Cutoff und Fokus-Exponent).

## Schattenbildung (Shadows)

Schatten entstehen, wenn undurchsichtige Objekte den Lichtstrom von einer Lichtquelle zu einer Oberfläche blockieren.

- **Kernschatten (Umbra)**: Bereich, der von keinem Punkt der Lichtquelle erreicht wird (entsteht bei Punktlichtquellen $\rightarrow$ **harte Schattenkanten**).
- **Halbschatten (Penumbra)**: Bereich, der nur von einem Teil einer ausgedehnten Lichtquelle erreicht wird (entsteht bei Flächenlichtquellen $\rightarrow$ **weiche Schattenkanten**).

> [!note] Shadow Mapping (Schattenmap-Verfahren) 
> Bildraumbasiertes 2-Pass-Verfahren zur Schattenberechnung:
> 1. **Pass 1**: Rendere die Szene aus der **Perspektive der Lichtquelle** und speichere nur die Tiefenwerte im **Shadow Buffer (Depth Map)**.
> 2. **Pass 2**: Rendere die Szene aus Kamerasicht. Transformiere jeden Oberflächenpunkt in das Koordinatensystem der Lichtquelle und vergleiche seinen Abstand zur Lichtquelle mit dem Wert im Shadow Buffer.
>     - Ist der Punkt weiter entfernt als der Wert im Shadow Buffer $\rightarrow$ **Punkt liegt im Schatten**.

## Das Phong-Beleuchtungsmodell

Das empirische Beleuchtungsmodell nach Bui Tuong Phong berechnet die reflektierte Lichtintensität an einem Punkt als Summe aus drei Komponenten.

```
Reflektierte Farbe = Ambient + Diffus + Spekulär (Glanzlicht)
```

> [!warning] Klausurrelevanz: [[Vektor|Vektoren]] des Phong-Modells 
> Für die Berechnung an einem Punkt $\mathbf{P}$auf der Oberfläche werden vier normierte [[Vektor|Vektoren]] benötigt:
> - $\mathbf{N}$: Oberflächennormalenvektor (Normal Vector)
> - $\mathbf{L}$: [[Vektor]] von $\mathbf{P}$ zur Lichtquelle (Light Vector)
> - $\mathbf{V}$: [[Vektor]] von $\mathbf{P}$ zur Kamera / Augpunkt (View Vector)
> - $\mathbf{R}$: Vektor des ideal reflektierten Lichtstrahls (Reflection Vector)

### 1. Ambiente Komponente ($I_{amb}$)

$$I_{amb} = k_a \cdot I_a$$

- $k_a$: Materialkoeffizient für ambiente Reflexion ($0 \le k_a \le 1$).
- $I_a$: Intensität des umgebenden Lichts.

### 2. Diffuse Komponente ($I_{diff}$) – Lambertsches Gesetz

Körper mit rauer Oberfläche reflektieren Licht gleichmäßig in alle Richtungen (ideale streuende Reflexion). Die Intensität hängt nur vom Einstrahlwinkel $\theta$ ab:

$$I_{diff} = k_d \cdot I_L \cdot \cos(\theta) = k_d \cdot I_L \cdot (\mathbf{N} \cdot \mathbf{L})$$

> [!note] Bedingung für das Skalarprodukt Nur wenn $\mathbf{N} \cdot \mathbf{L} > 0$ ist, wird die Vorderseite beleuchtet. Ist das Skalarprodukt negativ, liegt die Oberfläche im Selbstschatten ($\max(0, \mathbf{N} \cdot \mathbf{L})$).

### 3. Spekuläre Komponente ($I_{spec}$) – Glanzlicht

Glänzende Oberflächen reflektieren Licht bevorzugt in die ideale Reflexionsrichtung $\mathbf{R}$. Das Glanzlicht nimmt ab, je weiter die Blickrichtung $\mathbf{V}$ von $\mathbf{R}$ abweicht (Winkel $\phi$):

$$I_{spec} = k_s \cdot I_L \cdot \cos^n(\phi) = k_s \cdot I_L \cdot (\mathbf{R} \cdot \mathbf{V})^n$$

- $k_s$: Spekulärer Materialkoeffizient.
- $n$: **Glanzexponent (Shininess)**.
    - Kleines $n$ (z. B. $n=4$): Breites, mattes Glanzlicht.
    - Großes $n$ (z. B. $n=100$): Konzentrierter, scharfer Glanzpunkt (z. B. poliertes Metall oder Glas).

> [!tip] Berechnen des Reflexionsvektors $\mathbf{R}$ Aus der Geometrie der Spiegelung ergibt sich der Vektor $\mathbf{R}$ aus Normalenvektor $\mathbf{N}$ und Lichtvektor $\mathbf{L}$:
>
> $$\mathbf{R} = 2 \cdot (\mathbf{N} \cdot \mathbf{L}) \cdot \mathbf{N} - \mathbf{L}$$

### Gesamte Phong-Gleichung für $m$ Lichtquellen

$$I_{phong} = k_a \cdot I_a + \sum_{i=1}^{m} I_{L,i} \left[ k_d (\mathbf{N} \cdot \mathbf{L}_i) + k_s (\mathbf{R}_i \cdot \mathbf{V})^n \right]$$

### Blinn-Phong-Modell (Variante)

Nutzt statt des Reflexionsvektors $\mathbf{R}$ den sogenannten **Halfway-Vektor** $\mathbf{H}$ zwischen Licht- und Blickvektor:

$$\mathbf{H} = \frac{\mathbf{L} + \mathbf{V}}{\Vert{}\mathbf{L} + \mathbf{V}\Vert{}}$$$$I_{spec, Blinn} = k_s \cdot I_L \cdot (\mathbf{N} \cdot \mathbf{H})^n$$

- Recheneffizienter auf Hardware, da $\mathbf{H}$ bei unendlicher Lichtquelle und Kamera konstant ist.

## Texturen & Mappings (Texture Mapping)

Texturen überziehen einfache 3D-Geometrien mit 2D-Bilddaten, um hohe visuelle Komplexität ohne zusätzliche Polygone zu erzeugen.

> [!note] UV-Koordinaten Jeder Vertex eines 3D-Meshes erhält ein zweidimensionales Texturkoordinaten-Paar $(u, v) \in [0, 1]^2$.
> - $u$: Horizontale Achse der 2D-Textur.
> - $v$: Vertikale Achse der 2D-Textur.

### Texturfilterung & Mipmapping

Wird eine 2D-Textur auf Bildschirm-Pixel abgebildet, entstehen Größendifferenzen:

- **Magnification (Vergrößerung)**: Ein Texturpixel (Texel) deckt viele Bildschirm-Pixel ab.
    - _Nearest Neighbor_: Pixelige Blöcke.
    - _Bilinear Filtering_: Sanfte, aber verschwommene Interpolation.
- **Minification (Verkleinerung)**: Ein Bildschirm-Pixel überdeckt viele Texel $\rightarrow$ führt zu starkem Flimmern (Aliasing).
- **Mipmapping**: Vorberechnete Bildpyramide der Textur in halbierten Auflösungen ($1/2, 1/4, 1/8 \dots$). Die GPU wählt automatisch die passende Mipmap-Stufe basierend auf dem Abstand zur Kamera aus.

### Weiterführende Mapping-Techniken

> [!tip] Arten von Surface Maps
> - **Bump Mapping**: Modifiziert rechnerisch die Oberflächennormale $\mathbf{N}$ pro Pixel anhand einer Graustufen-Map, ohne die Geometrie zu verändern. Erzeugt eine Illusion von Rauheit/Struktur an der Oberfläche (Silhouetten bleiben flach).
> - **Normal Mapping**: Verwendet ein RGB-Bild, um echte 3D-Normalenvektoren $(x, y, z)$ direkt im Tangentenraum abzuspeichern (R-Kanal = X, G-Kanal = Y, B-Kanal = Z).
> - **Displacement Mapping**: Verschiebt die tatsächlichen [[Knoten|Vertices]] des Polygonnetzes anhand einer Map. Verändert die reale 3D-Geometrie und die Silhouette (erfordert dichte Meshes).
> - **Environment Mapping (Reflection Map)**: Bildebene wird auf eine umgebende Kugel oder einen Würfel (Cube Map) abgebildet, um spiegelnde Oberflächen ohne aufwendiges Raytracing zu simulieren.

## Prozedurale Oberflächen & Shader

Anstatt statische Grafiken zu nutzen, können Material- und Oberflächeneigenschaften auch mathematisch/programmatisch generiert werden.

> [!info] Shader-Typen in OpenGL / WebGL
> - **Vertex Shader**: Verarbeitet einzelne Eckpunkte der Geometrie (Transformationen, Positionen, Projektionen).
> - **Fragment Shader (Pixel Shader)**: Berechnet für jedes projizierte Raster-Fragment den finalen Farb- und Tiefenwert (Implementierung des Phong-Modells, Textur-Lookups, Noise-Funktionen wie Perlin Noise).

## Nächste Themen

- [[Shading & Rendering]]
- [[Alternative Rendering-Pipelines]]