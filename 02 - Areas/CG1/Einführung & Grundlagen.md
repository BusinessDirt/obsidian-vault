---
date: 2026-07-31
tags: []
---
# 🖥️ Einführung & Grundlagen
> [!abstract] Navigation & MOC Zurück zur Hauptübersicht: [[Computergrafik 1]]

> [!info] Themenüberblick Diese Notiz deckt alle Grundlagen und Kernkonzepte des ersten Kapitels ab:
> - Definition & Einordnung der Computergrafik
> - Die 3D-Rendering-Pipeline und ihre Koordinatensysteme
> - Hauptkomponenten einer virtuellen Szene
> - Mathematisches Überlebens-Kit (Vektoren, Produkte, Matrizen)

## 📌 Was ist Computergrafik?

Die Computergrafik befasst sich mit der computergestützten Erzeugung, Darstellung und Manipulation von visuellen Inhalten und Bildern aus digitalen Datenmodellen. Sie bildet das Fundament für Animationen, Spiele, wissenschaftliche Visualisierungen, medizinische Bildgebung und Benutzeroberflächen.

> [!tip] Abgrenzung verwandter Disziplinen
> - **Computergrafik (Bildsynthese)**: _Daten / 3D-Modell_ $\rightarrow$ **2D-Bild**
> - **Computer Vision / Bildverarbeitung (Bildanalyse)**: _2D-Bild_ $\rightarrow$ **Daten / 3D-Modell**
> - **Visualisierung**: Aufbereitung abstrakter Datenmengen in grafische Repräsentationen.

## 🔄 Die Grafik-Pipeline im Überblick

Der Prozess der Bildsynthese transformiert dreidimensionale Objektmodelle Schritt für Schritt in ein zweidimensionales Rasterbild aus Pixeln.

> [!note] Die Transformationsschritte & Koordinatensysteme
> 1. **Modellkoordinaten (Model Space)**: Jedes Objekt existiert in seinem eigenen, lokalen Koordinatensystem.
> 2. **Weltkoordinaten (World Space)**: Platzierung aller Objekte in einer gemeinsamen Szene via Szenengraph und Transformationen.
> 3. **Kamerakoordinaten (Camera / View Space)**: Ausrichtung der Szene relativ zur Position und Blickrichtung der virtuellen Kamera.
> 4. **Bild- / Bildschirmkoordinaten (Image / Screen Space)**: Projektion auf die 2D-Bildebene und Umrechnung in konkrete Pixelraster.

```
[ 3D-Modelle ] (Modellkoordinaten)
       │
       ▼  Scene Graph & Modell-Transformation
[ 3D-Welt ] (Weltkoordinaten)
       │
       ▼  Kamera-Transformation
[ 2D-Polygone ] (Kamerakoordinaten)
       │
       ▼  Rasterisierung & Shading
[ Pixels ] (Imagekoordinaten)
```

> [!info] Kernaufgaben der Stufen
> - **Tesselierung / Modellierung**: Zerlegung komplexer Oberflächen in einfache Grundelemente (Primitiven wie Dreiecke).
> - **Transformation**: Umrechnung von Punkten zwischen den einzelnen Koordinatensystemen mittels Matrizen.
> - **Clipping & Culling**: Entfernen von Objekten oder Polygonen, die außerhalb des Sichtfelds liegen oder dem Betrachter abgewandt sind.
> - **Beleuchtung & Shading**: Berechnung der Farbwerte an den Objektgrenzen basierend auf Lichtquellen und Materialeigenschaften.
> - **Rasterisierung**: Diskretisierung der kontinuierlichen Geometrie in konkrete Bildschirm-Pixel.

## 🧱 Bestandteile einer virtuellen Szene

Eine vollständige 3D-Szene besteht aus verschiedenen Bausteinen, die zusammenwirken:

> [!example] Komponentenübersicht
> - **Geometrie (3D-Meshes)**: Repräsentation von Objektformen durch Punktwolken, Polygonnetze (z. B. Stanford Bunny, Utah Teapot) oder mathematische Flächen.
> - **Materialeigenschaften**: Definition der optischen Eigenschaften wie Farbe, Rauheit, Glanz, Transparenz, Opazität und Texturen.
> - **Lichtquellen**: Lichtarten zur Simulation natürlicher und künstlicher Beleuchtung (Punktlicht, gerichtetes Licht, Spotlicht, Umgebungslicht).
> - **Kamera**: Parameter wie Standort, Blickrichtung, Öffnungswinkel (FOV) und Projektionsart (perspektivisch vs. orthographisch).
> - **Animation & Dynamik**: Hierarchie- und Zeitveränderungen von Objektpositionen, Deformationen und Eigenschaften.

## 📐 Mathematisches Überlebens-Kit

Lineare Algebra und Vektorrechnung bilden das mathematische Fundament der gesamten Computergrafik.

> [!warning] Klausurrelevanz Das Verständnis und sichere Anwenden von Vektoren, Skalar- und Kreuzprodukten sowie Matrizen ist essenziell für Prüfungsaufgaben zu Transformationen, Beleuchtung und Projektionen.

### 1. Vektoren

Ein [[Vektor]] $\mathbf{v} \in \mathbb{R}^3$ beschreibt eine Richtung und Länge im Raum:

$$\mathbf{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

- **Länge / Norm**: $\Vert{}\mathbf{v}\Vert{} = \sqrt{x^2 + y^2 + z^2}$
- **Normalisierung (Einheitsvektor)**: $\hat{\mathbf{v}} = \frac{\mathbf{v}}{\Vert{}\mathbf{v}\Vert{}}$ (Länge 1)

### 2. Skalarprodukt (Dot Product)

Das Skalarprodukt zweier [[Vektor|Vektoren]] $\mathbf{a}$ und $\mathbf{b}$ liefert einen Skalarwert:

$$\mathbf{a} \cdot \mathbf{b} = a_x b_x + a_y b_y + a_z b_z = \Vert{}\mathbf{a}\Vert{} \Vert{}\mathbf{b}\Vert{} \cos(\theta)$$

> [!tip] Wichtige Eigenschaften des Skalarprodukts
> - $\mathbf{a} \cdot \mathbf{b} = 0$: [[Vektor|Vektoren]] stehen **orthogonal** (senkrecht) zueinander.
> - **Für normierte [[Vektor|Vektoren]]**: Liefert direkt den Kosinus des eingeschlossenen Winkels $\cos(\theta)$.
> - **Anwendung**: Beleuchtungsberechnung (z. B. Lambert-Shader: Einstrahlwinkel des Lichts auf eine Oberfläche).

### 3. Kreuzprodukt (Cross Product)

Das Kreuzprodukt zweier [[Vektor|3D-Vektoren]] erzeugt einen neuen [[Vektor]], der senkrecht auf beiden Ausgangsvektoren steht:

$$\mathbf{a} \times \mathbf{b} = \begin{pmatrix} a_y b_z - a_z b_y \\ a_z b_x - a_x b_z \\ a_x b_y - a_y b_x \end{pmatrix}$$

> [!note] Wichtige Eigenschaften des Kreuzprodukts
> - Die Länge $\Vert{}\mathbf{a} \times \mathbf{b}\Vert{}$ entspricht der Fläche des von $\mathbf{a}$und $\mathbf{b}$ aufgespannten Parallelogramms.
> - Die Richtung folgt der **Rechte-Hand-Regel**.
> - **Anwendung**: Berechnung von **Flächen- und Normalenvektoren** auf Polygonen sowie der Konstruktion von Kamerakoordinatensystemen.  

### 4. Matrizen
[[Matrix|Matrizen]] dienen zur mathematischen Beschreibung von Transformationen (Skalierung, Rotation, Translation).

- **Multiplikation**: Matrizenmultiplikation ist i. d. R. **nicht kommutativ** ($A \cdot B \neq B \cdot A$). Die Reihenfolge der Ausführung ist entscheidend!

## 🔗 Nächste Themen
- [[Transformationen & Szenengraph]]
- [[3D-Geometrie & Modellierung]]
- [[Kameramodell & Projektion]]