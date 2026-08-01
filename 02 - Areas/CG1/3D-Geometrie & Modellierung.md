---
date: 2026-07-31
tags:
  - CSG
  - Computergrafik
  - Curves
  - Geometrie
  - LMU
  - Modellierung
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Transformationen & Szenengraph]] | Nächstes Thema: [[Kameramodell & Projektion]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu 3D-Geometrie & Modellierung:
> - Repräsentationsformen & [[3D-Geometrie & Modellierung|Polygonnetze]] (Triangle Meshes)
> - Datenstrukturen für Meshes (Indexed Face Sets, Half-Edge)
> - Geometrische [[3D-Geometrie & Modellierung|Primitive]] & [[3D-Geometrie & Modellierung#Constructive Solid Geometry (CSG)|CSG]]
> - Erzeugungsverfahren: Extrusion & Rotationskörper
> - Freiformkurven & -flächen ([[3D-Geometrie & Modellierung#Bézier-Kurven|Bézier-Kurven]], De-Casteljau-Algorithmus, [[3D-Geometrie & Modellierung#Splines & NURBS|NURBS]])
> - Levels of Detail (LOD) & Netz-Vereinfachung (QEM)
> - Voxel- und punktbasierte Grafik

## Repräsentation von 3D-Objekten

Um dreidimensionale Körper im Computer darzustellen, werden unterschiedliche Modellierungsansätze genutzt. Man unterscheidet grundsätzlich zwischen Volumen-Repräsentationen (Solid Representations) und Oberflächen-Repräsentationen (Boundary Representation / B-Rep).

> [!note] Wünschenswerte Eigenschaften von Repräsentationen
> - **Repräsentationskraft**: Fähigkeit, eine große Vielfalt komplexer 3D-Formen darzustellen.
> - **Eindeutigkeit**: Eineindeutige Zuordnung zwischen Datenstruktur und geometrischem Körper.
> - **Gültigkeit (Surjektivität)**: Jede gültige Parameterkombination ergibt ein mathematisch/physikalisch mögliches Objekt.
> - **Kompaktheit & Effizienz**: Geringer Speicherbedarf und schnelle Verarbeitung durch Grafikhardware.

## Polygonnetze (Triangle Meshes)

Polygonnetze sind die Standard-Repräsentation in der Echtzeit-[[Dimension|3D-Grafik]]. Sie approximieren Oberflächen durch eine Menge von verbundenen Polygonen.

> [!warning] Klausurrelevanz: Warum fast ausschließlich Dreiecke? 
> In internen Datenstrukturen und [[Pipeline|Grafik-Pipelines]] werden Oberflächen fast immer auf **Dreiecke (Triangles)** reduziert:
> 1. **Garantierte Planarität**: Drei Punkte im Raum liegen immer exakt in einer gemeinsamen Ebene. (Vierecke können windschief sein).
> 2. **Garantierte Konvexität**: Ein Dreieck ist immer konvex, was Rasterisierung und Inside/Outside-Tests vereinfacht.
> 3. **Hardware-Optimierung**: GPUs sind speziell auf das extrem schnelle Verarbeiten und Interpolieren von Dreiecken ausgelegt.

### Vertex-Orientierung & Winding Order

Die Reihenfolge, in der die Eckpunkte ([[Knoten|Vertices]]) eines Dreiecks definiert werden, bestimmt die Ausrichtung seiner Vorder- und Rückseite.

> [!tip] Rechte-Hand-Regel (Right-Hand-Rule)
> - **Counter-Clockwise (CCW)**: Werden die [[Knoten|Vertices]] gegen den Uhrzeigersinn definiert, zeigt der Normalenvektor nach außen (Vorderseite / Front Face).
> - **Clockwise (CW)**: Definition im Uhrzeigersinn kennzeichnet die Rückseite (Back Face).
> - **Bedeutung**: Unerlässlich für das **Backface Culling** (Verwerfen abgewandter Polygone im Rendering-Prozess).

### Datenstrukturen für Polygonnetze

#### 1. Explicit Mesh (Naive Liste)

Speichert jedes Dreieck als 3 konkrete 3D-Punkte.

- _Nachteil_: Extrem redundanter Speicherbedarf, da gemeinsame Vertices mehrfach gespeichert werden; keine Topologieinformationen über Nachbarschaften.

#### 2. Shared Vertex / Indexed Face Set (IFS)

Trennt die geometrische Position von der topologischen Verknüpfung.

- **Vertex List**: Array aller eindeutigen Punkte $\begin{pmatrix} x, y, z \end{pmatrix}$.
- **Index / Face List**: Array von Dreiecken, die jeweils auf 3 Indizes der Vertex List verweisen.

> [!example] Beispiel: Indexed Face Set in Three.js
>
> ```
> const geometry = new THREE.BufferGeometry();
> // Vertex List (Koordinaten)
> const vertices = new Float32Array([
>   -1.0, 0.0,  1.0, // Index 0
>    1.0, 0.0,  1.0, // Index 1
>    1.0, 0.0, -1.0, // Index 2
>    0.0, 2.0,  0.0  // Index 3 (Spitze)
> ]);
> // Index List (Face-Definitionen)
> const indices = [
>   0, 1, 3, // Dreieck 1 (Vorne)
>   1, 2, 3, // Dreieck 2 (Rechts)
>   2, 0, 3  // Dreieck 3 (Links)
> ];
> geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
> geometry.setIndex(indices);
> ```

#### 3. Erweiterte Topologie-Strukturen (Winged-Edge / Half-Edge)

Zeigerbasierte Datenstrukturen, die explizit Nachbarschaftsbeziehungen zwischen Kanten, Flächen und Vertices speichern. Essenziell für Geometrie-Editoren (z. B. Subdivisions, Mesh Editing).

## Geometrische Primitive & CSG

### Geometrische Primitive

Einfache Grundkörper (Würfel, Kugel, Zylinder, Kegel, Torus), die entweder implizit (z. B. Kugelgleichung $x^2 + y^2 + z^2 - r^2 = 0$) oder parametrisch definiert sind.

### Constructive Solid Geometry (CSG)

CSG kombiniert einfache Grundkörper mittels boolescher Mengenoperationen zu komplexen festen [[Dimension|3D-Objekten]].

> [!note] Die 3 booleschen Hauptoperationen
> - **Vereinigung (**$\cup$**, Union)**: Verbindet zwei Objekte zu einem gemeinsamen Volumen.
> - **Schnittmenge (**$\cap$**, Intersection)**: Behält nur den Bereich bei, der in beiden Objekten gleichzeitig enthalten ist.
> - **Differenz (**$\setminus$**, Difference)**: Schneidet das Volumen des zweiten Objekts aus dem ersten Objekt heraus (z. B. Erzeugung von Bohrungen).

```
        [ CSG Tree Root: Differenz (\) ]
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
  [ Würfel (Cube) ]     [ Zylinder (Cylinder) ]
```

## Swept Volumes (Extrusion & Rotation)

Erzeugung von 3D-Körpern durch das Bewegen (Sweeping) eines 2D-Profils entlang eines Pfades im Raum.

- **Lineare Extrusion**: Verschieben einer 2D-Kontur entlang eines Vektors (z. B. Erzeugung von Prismen, Rohren oder Profilen).
- **Rotationskörper (Rotational Sweeps / Lathing)**: Rotation einer 2D-Kurve um eine Rotationsachse (z. B. Erzeugung von Vasen, Flaschen, Gläsern oder Donut-Formen).

## Kurven & Freiformflächen

Einfache Polygonnetze stoßen bei organischen, geschwungenen Formen an Grenzen. Hier werden mathematische Freiformkurven genutzt.

### Bézier-Kurven

Eine Bézier-Kurve wird durch $n+1$ Kontrollpunkte $P_0, P_1, \dots, P_n$ definiert.

> [!note] Mathematische Formel (Bernstein-Polynome) 
> Eine Bézier-Kurve vom Grad $n$ ist definiert als:
>
> $$C(t) = \sum_{i=0}^{n} B_{i,n}(t) \cdot P_i \quad \text{mit } t \in [0, 1]$$
>
> Die Bernstein-Polynome lauten:
>
> $$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$$

> [!tip] Wichtige Eigenschaften von Bézier-Kurven
> - **Endpunktinterpolation**: Die Kurve beginnt exakt in $P_0$ und endet exakt in $P_n$.
> - **Tangenten an den Endpunkten**: Die Ausrichtung der Kurve in $P_0$ entspricht der Richtung des Vektors $(P_1 - P_0)$, am Ende entsprechend $(P_n - P_{n-1})$.
> - **Konvexe-Hülle-Eigenschaft**: Die gesamte Kurve liegt vollständig innerhalb der konvexen Hülle ihrer Kontrollpunkte.
> - **Affine Invarianz**: Eine affine Transformation der Kontrollpunkte führt zur selben Kurve wie die spätere Transformation der Kurvenpunkte.

### De-Casteljau-Algorithmus

Numerisch stabiler und intuitiver Algorithmus zur Auswertung von Bézier-Kurven durch wiederholte lineare Interpolation.

> [!example] Algorithmus-Idee für ein Parameter $t \in [0,1]$ 
> Gegeben seien die Kontrollpunkte $P_0, P_1, P_2, P_3$ (kubische Bézier-Kurve):
> 1. Interpoliere linear zwischen je zwei benachbarten Punkten:
>     $$P_0^1(t) = (1-t)P_0 + tP_1$$$$P_1^1(t) = (1-t)P_1 + tP_2$$$$P_2^1(t) = (1-t)P_2 + tP_3$$
> 2. Wiederhole den Schritt für die neuen Punkte:
>     $$P_0^2(t) = (1-t)P_0^1(t) + tP_1^1(t)$$$$P_1^2(t) = (1-t)P_1^1(t) + tP_2^1(t)$$
> 3. Der finale Kurvenpunkt ergibt sich aus:
>     $$C(t) = P_0^3(t) = (1-t)P_0^2(t) + tP_1^2(t)$$

### Splines & NURBS

- **B-Splines**: Setzen Kurven aus mehreren Abschnitten zusammen. Änderung eines Kontrollpunkts wirkt sich nur **lokal** aus (im Gegensatz zu global wirkenden Bézier-Kurven).
- **NURBS (Non-Uniform Rational B-Splines)**: Industriestandard im CAD-Bereich. Ermöglichen die exakte Darstellung von Kegelschnitten (Kreise, Ellipsen) durch gewichtete homogene Koordinaten.

## Levels of Detail (LOD) & Netz-Vereinfachung

Um Rechenleistung beim Rendering großer Szenen zu sparen, werden Objekte je nach Entfernung zur Kamera in unterschiedlichen Detailstufen dargestellt.

> [!info] Arten von LOD
> - **Diskreter LOD**: Mehrere vorgefertigte Varianten eines Meshes mit unterschiedlicher Polygonanzahl (z. B. High-Poly, Mid-Poly, Low-Poly).
> - **Kontinuierlicher LOD**: Dynamische Echtzeit-Reduktion der Polygonanzahl basierend auf dem Abstand zur Kamera.

### Algorithmen zur Mesh-Simplifizierung

- **Vertex Clustering**: Einteilen des Raums in ein Gitter; alle Vertices innerhalb einer Gitterzelle werden zu einem einzigen Vertex verschmolzen. Fast, aber führt oft zu Qualitätsverlusten.
- **Edge Collapse**: Zusammenziehen zweier benachbarter Vertices $u$ und $v$ zu einem neuen Vertex $v'$. Dabei werden entfallende Dreiecke entfernt.
- **Quadric Error Metrics (QEM)**: Berechnet mathematisch den Fehler durch das Zusammenziehen von Kanten. Kanten mit dem geringsten geometrischen Fehler werden zuerst reduziert (Stanford Bunny Reduktion).

### Billboards (Impostors)

Flache 2D-Polygone (bestehend aus 2 Dreiecken) mit einer transparenten Textur, die sich immer automatisch zur Kamera ausrichten. Extrem effizient für Vegetation, Partikel oder weit entfernte Objekte.

## Volumen- und Punktbasierte Grafik

Neben polylokalen Grenzflächendarstellungen existieren Ansätze für spezielle Anwendungsfälle:

### Voxel-Daten (Volume Rendering)

- **Voxel** = „Volume Pixel“ (kleinste Einheit eines 3D-Rasters).
- Repräsentiert das **Innere** eines Körpers, nicht nur die Hülle.
- Typisch für medizinische Bildgebung (MRT, CT, 3D-Ultraschall) oder Spiele wie Minecraft.
- _Nachteil_: Kubisches Speicherwachstum mit steigender Auflösung ($O(n^3)$).

### Punktbasierte Grafik (Surfels)

- Objekte werden als Menge unstrukturierter Punkte der Oberfläche („Surfels“) dargestellt.
- Keine explizite Topologie oder Mesh-Struktur erforderlich.
- Häufig das Ergebnis von 3D-Laserscans.

## Nächste Themen

- [[Kameramodell & Projektion]]
- [[Rasterisierung]]
- [[Licht, Aussehen & Material]]