---
date: 2026-07-31
tags: []
---
# 📷 Kameramodell & Projektion

#computergrafik #lmu #kamera #projektion #zbuffer #culling

> [!abstract] Navigation & MOC Zurück zur Hauptübersicht: [[MOC - Computergrafik 1]] Vorheriges Thema: [[3D-Geometrie & Modellierung]]

> [!info] Themenüberblick Diese Notiz behandelt das virtuelle Kameramodell und die Abbildung von 3D-Szenen auf Bildebenen:
> 
> - Klassische Projektionstaxonomie (Parallel vs. Perspektivisch)
>     
> - Synthetisches Kameramodell (Lochkamera-Prinzip)
>     
> - Die Kamera-Transformation (LookAt-Matrix)
>     
> - Sichtvolumen (Frustum) & Perspektivische Projektion
>     
> - Perspektivische Division & Viewport-Transformation
>     
> - Sichtbarkeitsberechnung & Verdeckung (Backface Culling, Z-Buffer, Painter's Algorithm)
>     

## 🏛️ Klassische Projektionstaxonomie

Die Abbildung einer dreidimensionalen Szene auf eine zweidimensionale Projektionsfläche erfordert Projektionsstrahlen (Projectors), die von Objektpunkten zur Projektionsfläche verlaufen.

> [!note] Grundannahmen klassischer Ansätze
> 
> - Objekte bestehen aus flachen Polygonflächen.
>     
> - Die Projektionsfläche ist eine ebene Fläche (Planar Projection).
>     

```
                      ┌── Parallele Projektoren ──► Parallelprojektion
                      │                             (Orthographisch, Axonometrisch, Schräg)
Projektionsstrahlen ──┤
                      │
                      └── Konvergierende Strahlen ─► Perspektivische Projektion
                                                    (1, 2 oder 3 Fluchtpunkte)
```

### 1. Parallelprojektion (Parallel Projection)

Die Projektionsstrahlen verlaufen parallel zueinander. Der Fluchtpunkt liegt im Unendlichen; Objektgrößen ändern sich nicht mit der Entfernung (keine perspektivische Verkürzung).

- **Orthographische Projektion (Orthographic)**: Projektionsstrahlen stehen **orthogonal (90°)** zur Projektionsfläche.
    
    - _Hauptansichten (Planar)_: Draufsicht (Top), Vorderansicht (Front), Seitenansicht (Side).
        
    - _Axonometrisch_: Projektionsfläche ist gegenüber den Hauptachsen geneigt.
        
        - **Isometrisch**: Alle drei Hauptachsen werden im gleichen Winkel geschnitten und gleich stark verkürzt.
            
        - **Dimetrisch**: Zwei Achsen werden gleich verkürzt.
            
        - **Trimetrisch**: Alle drei Achsen werden unterschiedlich verkürzt.
            
- **Schräge Projektion (Oblique)**: Projektionsstrahlen treffen in einem Winkel $\neq 90^\circ$ auf die Ebene.
    
    - _Kavalierprojektion (Cavalier)_: Winkel $45^\circ$, Längen in der Tiefe werden 1:1 abgebildet.
        
    - _Kabinettprojektion (Cabinet)_: Winkel $\approx 63.4^\circ$, Längen in der Tiefenachse werden auf die Hälfte ($1/2$) verkürzt.
        

### 2. Perspektivische Projektion (Perspective Projection)

Projektionsstrahlen laufen in einem gemeinsamen Projektionszentrum (Center of Projection / COP / Augpunkt) zusammen. Distanzierte Objekte erscheinen kleiner.

> [!tip] Fluchtpunkte (Vanishing Points) Parallele Objektlinien, die nicht parallel zur Bildebene verlaufen, schneiden sich im projizierten Bild in sogenannten **Fluchtpunkten**. Je nach Orientierung des Koordinatensystems zur Bildebene spricht man von **1-, 2- oder 3-Punkt-Perspektive**.

## 🎥 Das synthetische Kameramodell

In der Computergrafik wird das Prinzip der **Lochkamera (Pinhole Camera)** als mathematisches Modell verwendet.

> [!note] Parameter einer virtuellen Kamera
> 
> - **Position (Eye / Camera Position** $\mathbf{e}$**)**: Standort der Kamera in Weltkoordinaten.
>     
> - **Blickrichtung (Look-At Point** $\mathbf{g}$ **/ View Vector** $\mathbf{v}$**)**: Zielpunkt, auf den die Kamera gerichtet ist.
>     
> - **Up-Vektor (**$\mathbf{u}$**)**: Richtungsvektor, der angibt, wo für die Kamera „oben“ ist.
>     
> - **Öffnungswinkel (Field of View / FOV)**: Vertikaler oder horizontaler Sehwinkel.
>     
> - **Seitenverhältnis (Aspect Ratio** $a$**)**: Verhältnis von Breite zu Höhe des Bildes ($a = \frac{w}{h}$).
>     
> - **Near & Far Clipping Planes (**$z_{near}, z_{far}$**)**: Begrenzungsebenen des sichtbaren Tiefenbereichs.
>     

```
       [ Eye / Kamera e ]
             │   \
             │    \  Projektionsstrahl
             │     \
             ▼      ▼
    [ Near Plane ] ──► [ Intersecting Point ]
             │
             ▼
     [ Far Plane ]
```

### Die LookAt-Transformation (World Space $\rightarrow$ Camera Space)

Um die Szene aus Sicht der Kamera zu rendern, wird das globale Koordinatensystem so transformiert, dass die Kamera im Ursprung liegt und entlang der negativen Z-Achse blickt.

> [!warning] Konstruktion der Kamera-Basisvektoren Aus den Vektoren Position $\mathbf{e}$, Zielpunkt $\mathbf{g}$ und Up-Vektor $\mathbf{u}$ wird ein orthonormales Koordinatensystem $(\mathbf{w}, \mathbf{u}', \mathbf{v}')$ gebildet:
> 
> 1. **Blickrichtung (Z-Achse der Kamera)**: $\mathbf{w} = \frac{\mathbf{e} - \mathbf{g}}{\Vert{}\mathbf{e} - \mathbf{g}\Vert{}}$ (zeigt vom Ziel weg zur Kamera)
>     
> 2. **Rechte Achse (X-Achse der Kamera)**: $\mathbf{u}' = \frac{\mathbf{u} \times \mathbf{w}}{\Vert{}\mathbf{u} \times \mathbf{w}\Vert{}}$
>     
> 3. **Korrigierter Up-Vektor (Y-Achse der Kamera)**: $\mathbf{v}' = \mathbf{w} \times \mathbf{u}'$
>     

Die Transformationsmatrix $\mathbf{M}_{view}$ setzt sich zusammen aus Translation der Kamera in den Ursprung und anschließender Rotation zur Ausrichtung der Achsen:

$$\mathbf{M}_{view} = \mathbf{R}_{view} \cdot \mathbf{T}(-\mathbf{e}) = \begin{pmatrix} u'_x & u'_y & u'_z & 0 \\ v'_x & v'_y & v'_z & 0 \\ w_x & w_y & w_z & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 & -e_x \\ 0 & 1 & 0 & -e_y \\ 0 & 0 & 1 & -e_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

> [!example] Beispiel: Kamera in Three.js
> 
> ```
> // Erzeugung einer Perspektivkamera
> // PerspectiveCamera(fov, aspect, near, far)
> const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
> 
> // Positionieren und Ausrichten
> camera.position.set(0, 5, 10);
> camera.lookAt(new THREE.Vector3(0, 0, 0));
> scene.add(camera);
> ```

## 📐 Perspektivische Projektion & Frustum

Das Sichtvolumen einer Perspektivkamera bildet einen Pyramidenstumpf (Viewing Frustum).

> [!note] Ziel der Projektionsmatrix Die Projektionsmatrix verzerrt den Pyramidenstumpf in einen achsenparallelen Einheitswürfel, das sogenannte **Canonical View Volume (Normalized Device Coordinates / NDC)** im Bereich $[-1, 1]^3$.

### Der mathematische Ablauf: 2-Schritt-Verfahren

> [!warning] Klausurrelevanz: Die zwei Schritte der Perspektive Die Perspektivtransformation erfolgt strikt in zwei aufeinanderfolgenden Phasen:
> 
> 1. **Anwendung der Projektionsmatrix** $M_{proj}$: Transformation der homogenen Koordinaten. Hier wird der $z$-Wert in die vierte Koordinate $w$ geschrieben.
>     
> 2. **Perspektivische Division (Perspective Division)**: Multiplikation bzw. Division aller Komponenten durch $w$.
>     

#### Schritt 1: Projektionsmatrix

Für ein Sichtfeld mit Fokusdistanz $d$ (oder skaliert auf $z_{near}, z_{far}$) sieht die Matrixform typischerweise wie folgt aus:

$$\mathbf{M}_{proj} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & A & B \\ 0 & 0 & -1 & 0 \end{pmatrix} \cdot \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix} = \begin{pmatrix} x \\ y \\ Az + B \\ -z \end{pmatrix}$$

#### Schritt 2: Perspektivische Division

Nach der Matrizenmultiplikation wird der homogene Vektor durch seine $w$-Komponente ($w = -z$) dividiert:

$$\mathbf{p}_{ndc} = \begin{pmatrix} x / w \\ y / w \\ z_{ndc} / w \\ 1 \end{pmatrix} = \begin{pmatrix} -x / z \\ -y / z \\ z_{ndc} / -z \\ 1 \end{pmatrix}$$

> [!tip] Effekt der Division durch $-z$
> 
> - Punkte mit **größerer Entfernung** (größerer negativer $z$-Betrag) werden durch eine größere Zahl dividiert $\rightarrow$ **x und y schrumpfen** (Objekte werden kleiner dargestellt).
>     
> - Punkte auf der optischen Achse ($x=0, y=0$) bleiben exakt in der Bildmitte.
>     

### 🖼️ Viewport-Transformation (NDC $\rightarrow$ Screen Coordinates)

Abschließend werden die normierten Koordinaten $[-1, 1]^2$ auf die tatsächlichen Pixelkoordinaten des Fensters/Bildschirms $[0, w_{screen}] \times [0, h_{screen}]$ abgebildet:

$$x_{screen} = \frac{x_{ndc} + 1}{2} \cdot w_{screen} + x_{min}$$$$y_{screen} = \frac{y_{ndc} + 1}{2} \cdot h_{screen} + y_{min}$$

## 🔍 Sichtbarkeit & Verdeckungsrechnung (Occlusion)

Da bei der Projektion die dreidimensionale Szene auf ein flaches 2D-Raster reduziert wird, muss bestimmt werden, welche Oberflächen vom Betrachter aus sichtbar sind und welche verdeckt werden.

> [!info] Einteilung der Verfahren
> 
> - **Object-Precision Algorithms**: Arbeiten im kontinuierlichen 3D-Raum (z. B. Roberts-Algorithmus).
>     
> - **Image-Precision Algorithms**: Arbeiten im diskreten 2D-Rasterbereich (z. B. Z-Buffer).
>     

### 1. View Frustum Culling

Objekte oder Polygone, die vollständig außerhalb des Pyramidenstumpfs (Frustum) liegen, werden frühzeitig aus der Pipeline verworfen und nicht weiter verarbeitet.

### 2. Backface Culling

Entfernung von Polygonen, die vom Betrachter wegzeigen (Rückseiten geschlossener Körper).

> [!tip] Funktionsweise über das Skalarprodukt Gegeben sei der normale Oberflächenvektor $\mathbf{n}$eines Dreiecks und der Vektor zur Kamera $\mathbf{v}_{view}$:
> 
> - Berechne $d = \mathbf{n} \cdot \mathbf{v}_{view}$
>     
> - Wenn $d > 0$: Polygon zeigt zur Kamera $\rightarrow$ **Rendern**.
>     
> - Wenn $d \le 0$: Polygon zeigt von der Kamera weg $\rightarrow$ **Verwerfen (Culled)**.
>     
> - Spart ca. $50\%$ der zu rasternden Polygone ein.
>     

### 3. Der Painter's Algorithm (Maler-Algorithmus)

Sortiert alle Polygone nach ihrer Entfernung zur Kamera (von hinten nach vorne) und zeichnet sie nacheinander in den Puffer.

> [!danger] Probleme des Maler-Algorithmus
> 
> - **Rechenaufwand**: Aufwendiges Sortieren der Geometrien in jedem Frame.
>     
> - **Überlappungsproblem**: Kann zyklische Verdeckungen (A verdeckt B, B verdeckt C, C verdeckt A) oder sich durchdringende Polygone nicht ohne Aufspaltung lösen.
>     

### 4. Der Z-Buffer Algorithm (Depth Buffer)

Der Standard-Algorithmus moderner Grafikkarten auf Pixel-Ebene.

> [!note] Funktionsweise des Z-Buffers Neben dem Farbpuffer (Color Buffer) wird ein zweiter Puffer gleicher Auflösung verwaltet: der **Tiefenpuffer (Z-Buffer)**.
> 
> 1. Initialisiere alle Z-Buffer-Werte mit dem maximalen Tiefenwert (z. B. $1.0$).
>     
> 2. Für jedes zu zeichnende Fragment an Position $(x, y)$ mit berechnetem Tiefenwert $z$:
>     
>     - Vergleiche $z$ mit dem aktuell im Z-Buffer gespeicherten Wert $Z_{buffer}(x,y)$.
>         
>     - Wenn $z < Z_{buffer}(x,y)$ (Fragment liegt näher an der Kamera):
>         
>         - Schreibe die Farbe des Fragments in den Color Buffer.
>             
>         - Aktualisiere den Tiefenwert: $Z_{buffer}(x,y) = z$.
>             
>     - Sonst: Verwirf das Fragment (es wird durch ein näheres Objekt verdeckt).
>         

> [!tip] Vor- und Nachteile des Z-Buffers
> 
> - **Vorteil**: Unabhängig von der Reihenfolge, in der Polygone gezeichnet werden; löst zyklische Verdeckungen problemlos.
>     
> - **Nachteil**: Erfordert zusätzlichen Speicherplatz; Präzisionsverlust in der Tiefe durch die nichtlineare $z$-Skalierung der Perspektivprojektion (Z-Fighting bei nahe beieinander liegenden Flächen).
>     

## 🔗 Nächste Themen

- [[Rasterisierung]]
    
- [[Licht, Aussehen & Material]]
    
- [[Shading & Rendering]]