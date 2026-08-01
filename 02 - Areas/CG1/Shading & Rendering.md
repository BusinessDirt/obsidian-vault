---
date: 2026-07-31
tags:
  - Computergrafik
  - LMU
  - NPR
  - Radiosity
  - Raytracing
  - Rendering
  - RenderingEquation
  - Shading
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Licht, Aussehen & Material]] | Nächstes Thema: [[Animation]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu Shading & Rendering:
> - Lokale [[Shading & Rendering#Lokales Shading (Local Shading)|Shading-Verfahren]] (Flat Shading, Gouraud Shading, Phong Shading)
> - Unterschied: Phong-Beleuchtungsmodell vs. Phong-Shading
> - Globale Beleuchtungsmodelle I: [[Shading & Rendering#Globale Beleuchtungsmodelle: Ray Tracing|Ray Tracing]] (Ray Casting & Whitted Ray Tracing)
> - Globale Beleuchtungsmodelle II: [[Shading & Rendering#Globale Beleuchtungsmodelle: Radiosity|Radiosity]] & Formfaktoren
> - Die [[Shading & Rendering#Die Rendering-Gleichung & Monte-Carlo-Methoden|Rendering-Gleichung]] & Monte-Carlo-Methoden
> - Non-Photorealistic Rendering (NPR / Cel Shading)

## Lokales Shading (Local Shading)

Das Beleuchtungsmodell (z. B. Phong) berechnet die Lichtintensität an einzelnen Punkten. Shading-Algorithmen bestimmen, wie diese Farbwerte über ein gesamtes Polygon verteilt bzw. interpoliert werden.

> [!note] Prinzip der lokalen Beleuchtung 
> Bei lokalen Beleuchtungsverfahren wird die Farbe jedes Polygons nur anhand der Lichtquellen und der eigenen Geometrie/Materialeigenschaften berechnet. Objekte werfen **keine Schatten aufeinander** und erzeugen **keine gegenseitigen Reflexionen**.

### 1. Flat Shading (Facet Shading)

Das einfachste und schnellste Verfahren.

- **Ablauf**: Für das gesamte Polygon wird **ein einziger Farbwert** berechnet (meist unter Verwendung des Polygon-Mittelpunkts und der Flächennormale). Das gesamte Polygon wird einheitlich gefärbt.
- **Vorteil**: Extrem schnell zu berechnen.
- **Nachteil**: Ungewollte Sichtbarkeit der Polygonstruktur (Facettierung); stufenförmige Intensitätsübergänge erzeugen optische Täuschungen (**Mach-Bänder-Effekt**).

### 2. Gouraud Shading (Intensity Interpolation)

Entwickelt von Henri Gouraud (1971). Interpoliert Farbwerte sanft über die Fläche eines Polygons.

> [!note] Ablauf des Gouraud Shading
> 1. Berechne an jedem **Vertex** eine geglättete Vertex-Normale $\mathbf{N}_v$ als Mittelwert der angrenzenden Flächennormalen.
> 2. Wende das Beleuchtungsmodell an jedem Vertex an, um die **Vertex-Farben** zu berechnen.
> 3. Interpoliere die Farbwerte entlang der Polygonkanten und anschließend zeilenweise über die Scanline (baryzentrische / lineare Interpolation).

> [!warning] Nachteile des Gouraud Shading
> - **Verlorene Glanzpunkte (Specular Highlights)**: Fällt ein enges Glanzlicht in die Mitte eines Polygons, aber nicht auf die [[Knoten|Vertices]], geht der Glanzpunkt vollständig verloren.
> - **Mach-Bänder**: Sichtbar bei ungünstigen Übergängen der Intensitätsgradienten.
> - **Anisotropie**: Interpolationsergebnisse hängen von der Ausrichtung des Polygons im Raster ab.

### 3. Phong Shading (Normal Vector Interpolation)

Entwickelt von Phong Bui-Tuong (1975). Interpoliert Normalenvektoren statt Farbwerte.

> [!note] Ablauf des Phong Shading
> 1. Berechne an jedem **Vertex** die Vertex-Normale $\mathbf{N}_v$.
> 2. Interpoliere die **Normalenvektoren** linear über die Kanten und die Scanline für jedes einzelne Fragment/Pixel.
> 3. Normalisiere den interpolierten [[Vektor]] pro Pixel und wende das **Beleuchtungsmodell pro Pixel** an.

> [!tip] Vorteile des Phong Shading
> - **Exakte Glanzpunkte**: Glanzlichter werden auch mitten auf Polygonflächen korrekt dargestellt.
> - Sehr weiche, realistisch wirkende Oberflächenkrümmungen.
> - Eliminierung des Mach-Bänder-Effekts.

> [!danger] Klausur-Klassiker: Phong-Beleuchtungsmodell vs. Phong-Shading
> - **Phong-Beleuchtungsmodell (Empirische Formel)**: Die mathematische Gleichung $I = I_{amb} + I_{diff} + I_{spec}$, die beschreibt, wie aus Normalen-, Licht- und Blickvektor eine Farbe entsteht.
> - **Phong-Shading (Interpolationsverfahren)**: Das Verfahren, bei dem Normalenvektoren über ein Polygon interpoliert werden, um das Beleuchtungsmodell pro Pixel auszuwerten.

## Globale Beleuchtungsmodelle: Ray Tracing

Im Gegensatz zu lokalen Modellen berücksichtigen globale Beleuchtungsmodelle Wechselwirkungen zwischen allen Objekten der Szene (Schattenwurf, Spiegelungen, Lichtbrechung, indirektes Licht).

### 1. Ray Casting (Appel 1968)

Sende für jedes Bildschirm-Pixel einen Sehstrahl (Primary Ray) von der Kamera durch das Pixel in die Szene. Bestimme den ersten Schnittpunkt mit einem Objekt und berechne dort die Farbe (inkl. Schattenstrahl zur Lichtquelle).

### 2. Rekursives Ray Tracing (Whitted 1980)

Erweitert Ray Casting um spiegelnde Reflexion und Lichtbrechung durch rekursives Verfolgen von Sekundärstrahlen.

> [!info] Die Strahlenarten im Whitted Ray Tracing
> - **Primary Ray (Sehstrahl)**: Verläuft vom Augpunkt durch das Pixel in die [[Dimension|3D-Szene]].
> - **Shadow Ray (Schattenstrahl)**: Verläuft vom Schnittpunkt zur Lichtquelle. Ist der Weg blockiert, liegt der Punkt im Schatten.
> - **Reflection Ray (Reflexionsstrahl)**: Wird an spiegelnden Oberflächen im idealen Reflexionswinkel abgefeuert.
> - **Refraction Ray (Brechungsstrahl)**: Wird an transparenten Oberflächen gemäß dem **Brechungsgesetz von Snellius** gebrochen:
>
>     $$\eta_1 \sin(\theta_1) = \eta_2 \sin(\theta_2)$$

```
[ Kamera ] ──Primary Ray──► [ Oberfläche A (Glas) ]
                                 │           │
                     Reflection Ray         Refraction Ray
                                 ▼           ▼
                      [ Spiegel B ]       [ Objekt C ]
```

> [!tip] Eigenschaften von Ray Tracing
> - **Verfahren**: Bildraumbasiert (Image-Order Algorithm).
> - **Vorteile**: Perfekte Spiegelungen, Brechungen und scharfe Schatten.
> - **Nachteil**: Sehr hoher Rechenaufwand durch kontinuierliche Schnittpunktberechnungen (erfordert Beschleunigungsdatenstrukturen wie BVH oder Octrees).

## Globale Beleuchtungsmodelle: Radiosity

Radiosity basiert auf dem Modell des Wärmeaustauschs (Thermal Engineering) und simuliert diffuse Interreflexionen zwischen allen Oberflächen einer Szene.

> [!note] Grundprinzip
> - Alle Oberflächen der Szene werden in kleine Patches (Teilflächen) zerlegt.
> - Jedes Patch emittiert und reflektiert Licht ideal diffus (**Lambertsche Reflektoren**).
> - **Formfaktoren (Form Factors** $F_{ij}$**)** beschreiben rein geometrisch, wie viel Energie von Patch $i$auf Patch $j$ trifft.

> [!tip] Eigenschaften von Radiosity
> - **Verfahren**: Objektraumbasiert (Object-Order Algorithm).
> - **Bildelement-Unabhängigkeit**: Die Lichtverteilung wird im [[Dimension|3D-Raum]] (auf den [[Knoten|Vertices]]/Patches) berechnet und ist **vollständig unabhängig vom Kamerastandort**. Nach der Radiosity-Berechnung kann sich die Kamera frei in Echtzeit durch die Szene bewegen.
> - **Vorteil**: Extrem weiche, natürliche Schattenverläufe und indirektes Farbliefern (Color Bleeding).
> - **Nachteil**: Keine spekulären Glanzpunkte oder Spiegelungen.

## Die Rendering-Gleichung & Monte-Carlo-Methoden

Die von James Kajiya (1986) eingeführte **Rendering Equation** bildet das physikalische und mathematische Fundament der gesamten Bildsynthese.

> [!note] Die Rendering-Gleichung (Kajiya) Die abgestrahlte Radianz $L_o$ an einem Punkt $\mathbf{x}$ in Richtung $\mathbf{\omega}_o$ ist die Summe aus Eigenemission $L_e$ und aller reflektierten einfallenden Radianz $L_i$:
>
> $$L_o(\mathbf{x}, \mathbf{\omega}_o) = L_e(\mathbf{x}, \mathbf{\omega}_o) + \int_{\Omega} f_r(\mathbf{x}, \mathbf{\omega}_i, \mathbf{\omega}_o) \cdot L_i(\mathbf{x}, \mathbf{\omega}_i) \cdot (\mathbf{N} \cdot \mathbf{\omega}_i) \, d\mathbf{\omega}_i$$
>
> - $f_r$: Die BRDF (Bidirectional Reflectance Distribution Function) des Materials.
> - $\Omega$: Die Halbkugel (Hemisphere) aller Einfallswinkel.
> - $\mathbf{N} \cdot \mathbf{\omega}_i$: Lambertscher Kosinus-Faktor.

### Path Tracing & Monte-Carlo-Integration

Da die Rendering-Gleichung eine hochdimensionale Fredholm-Integralgleichung ist, lässt sie sich analytisch nicht lösen.

> [!tip] Monte-Carlo-Integration
> - Das Integral wird numerisch durch stochastisches Stichprobennehmen (Random Sampling) von Lichtstrahlen approximiert.
> - **Path Tracing**: Verfolgt zufällige Pfade von Photonen/Strahlen durch die Szene. Bei zu wenigen Samples entsteht Bildrauschen (Noise), das mit steigender Anzahl an Samples pro Pixel stochastisch konvergiert.

## Non-Photorealistic Rendering (NPR)

Nicht alle Grafikanwendungen streben nach Photorealismus. Non-Photorealistic Rendering erzeugt stilisierte, künstlerische oder technische Illustrationen.

> [!example] Populäre NPR-Techniken
> - **Cel Shading / Toon Shading**: Quantisiert kontinuierliche Beleuchtung in wenige diskrete Farb-Stufen (z. B. 2–3 Helligkeitsstufen für Comic-Look).
> - **Outline / Silhouette Rendering**: Zeichnet schwarze Außenlinien um Objekte (z. B. über Normalen- und Tiefenvergleiche im Post-Processing oder Backface-Expansion).
> - **Hatching & Cross-Hatching**: Erzeugt Schattierungen durch Strichmuster und Gravur-Stile.

## Nächste Themen

- [[Alternative Rendering-Pipelines]]
- [[Animation]]
- [[3D-Interaktion]]