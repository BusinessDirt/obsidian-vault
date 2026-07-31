---
date: 2026-07-31
tags: []
---
# 🤖 Alternative Rendering-Pipelines

#computergrafik #lmu #nerf #gaussiansplatting #3dgs #rendering #novelviewsynthesis

> [!abstract] Navigation & MOC Zurück zur Hauptübersicht: [[MOC - Computergrafik 1]] Vorheriges Thema: [[3D-Interaktion]]

> [!info] Themenüberblick Diese Notiz behandelt moderne, KI- und punktbasierte Rendering-Methoden zur Erzeugung fotorealistischer 3D-Szenen aus 2D-Fotos:
> 
> - Paradigmenwechsel: Von Polygonen zu impliziten & expliziten Volumendarstellungen
>     
> - Neural Radiance Fields (NeRFs) & Volume Rendering
>     
> - 3D Gaussian Splatting (3DGS) – Erfassung, Repräsentation, Rendering & Optimierung
>     
> - Neuartige Erweiterungen & Ausblick (GaussianAvatars, Triangle Splatting)
>     

## 🔄 Paradigmenwechsel: Novel View Synthesis

Klassische Grafik-Pipelines setzen voraus, dass 3D-Szenen als explizite Polygonnetze (Meshes) vorliegen und von Hand modelliert oder aufwendig gescannt wurden.

> [!warning] Das Problem klassischer Rekonstruktion Versucht man real existierende Objekte oder Umgebungen aus Kamerafotos in Dreiecks-Meshes umzuwandeln, entstehen oft Artefakte, fehlerhafte Löcher und Probleme bei spiegelnden, feinen oder transparenten Strukturen (z. B. Haare, Glas, Rauch).

> [!tip] Das Ziel: Novel View Synthesis (NVS) Rekonstruiere aus einer Reihe von 2D-Fotos einer echten Szene eine Repräsentation, aus der die Szene aus **beliebigen neuen Kameraperspektiven** fotorealistisch gerendert werden kann.

## 🧠 Neural Radiance Fields (NeRFs)

Eingeführt von Mildenhall et al. (2020), revolutionierten NeRFs die Bildsynthese durch die Nutzung künstlicher neuronaler Netze als implizite Szenendarstellung.

> [!note] Funktionsweise eines NeRF Ein NeRF speichert eine Szene nicht als Geometrie, sondern repräsentiert sie als eine kontinuierliche Funktion innerhalb eines geschulten neuronalen Netzes (eines mehrschichtigen Perzeptrons / MLP).
> 
> - **Eingabe (5D-Vektor)**:
>     
>     - 3D-Raumkoordinaten $\mathbf{x} = (x, y, z)$
>         
>     - 2D-Blickrichtung $\mathbf{d} = (\theta, \phi)$
>         
> - **Ausgabe**:
>     
>     - Volumendichte $\sigma$ (Wie dicht/undurchsichtig ist der Raum an dieser Stelle?)
>         
>     - Emittierte Farbe $\mathbf{c} = (r, g, b)$ (Richtungsabhängige Radianz)
>         

```
(x, y, z, θ, ϕ) ──► [ Multilayer Perceptron (MLP) ] ──► (r, g, b, σ)
```

### Rendering via Volume Ray Marching

Um ein Pixel zu berechnen, wird ein Sehstrahl durch die Szene geschossen und entlang des Strahls an diskreten Punkten das neuronale Netz abgefragt. Die Farb- und Dichtewerte werden entlang des Strahls aufintegriert:

$$C(\mathbf{r}) = \int_{t_{near}}^{t_{far}} T(t) \cdot \sigma(\mathbf{r}(t)) \cdot \mathbf{c}(\mathbf{r}(t), \mathbf{d}) \, dt$$

wobei $T(t) = \exp\left(-\int_{t_{near}}^{t} \sigma(\mathbf{r}(s)) \, ds\right)$ die Kumulierte Transmission (Transparenz) beschreibt.

> [!tip] Meilensteine & Weiterentwicklungen
> 
> - **NeRF in the Wild (2021)**: Verarbeitet unstrukturierte Internet- und Touristennamen-Fotos mit wechselnden Lichtverhältnissen und vorübergehenden Störfaktoren (Passanten).
>     
> - **Instant-NGP / NVIDIA (2022)**: Ersetzt das reine MLP durch multiresolutionale Hash-Tabellen. Reduziert die Trainingszeit von mehreren Stunden auf **wenige Sekunden** und ermöglicht Echtzeit-Auswertung.
>     

> [!danger] Grenzen von NeRFs
> 
> - Implizites Blackbox-Modell: Die Szene enthält keine greifbaren Geometrieschichten, was die Nachbearbeitung (Editing, Animation) erschwert.
>     
> - Hoher Rechenaufwand beim Ray Marching, da für jedes Pixel Dutzende Netz-Evaluierungen nötig sind.
>     

## 🟢 3D Gaussian Splatting (3DGS)

Eingeführt von Kerbl et al. (2023), verbindet 3D Gaussian Splatting die fotorealistische Qualität von NeRFs mit der extremen Rendering-Geschwindigkeit klassischer Rasterisierung ($> 100 \text{ fps}$).

> [!note] Die Kernidee von 3DGS Anstelle eines neuronalen Netzes wird die Szene als eine riesige Menge (Hunderte Tausende bis Millionen) von flexiblen, dreidimensionalen **Gauß-Ellipsoiden (Splats)**repräsentiert.

### Der Ablauf der 3DGS-Pipeline

```
[ 2D-Kamerafotos ] ──► [ Structure from Motion (SfM) ] ──► [ Initialpunkte & Kameras ]
                                                                   │
                                                                   ▼
[ Finales Raster-Bild ] ◄── [ Tile-basiertes Rendering ] ◄── [ 3D Gaussians (Splats) ]
                                                                   ▲
                                                                   │ (Gradienten-Loss)
                                                       [ Adaptives Optimieren ]
```

#### 1. Szenenerfassung (Scene Acquisition via SfM)

Mithilfe von **Structure from Motion (SfM)** (z. B. COLMAP) werden aus den Eingabefotos automatisch die exakten Kamerapositionen berechnet und eine spärliche 3D-Punktwolke (Sparse Point Cloud) erzeugt.

#### 2. Szenenrepräsentation (Splat-Parameter)

Jedes 3D-Gauß-Primitiv besitzt folgende optimierbare Attribute:

- **Position (Center** $\mathbf{\mu}$**)**: 3D-Koordinaten $(x, y, z)$.
    
- **Kovarianzmatrix** $\mathbf{\Sigma}$: Bestimmt Form und Ausrichtung im Raum. Um mathematische Gültigkeit zu garantieren, wird sie zerlegt in:
    
    - **Skalierung** $\mathbf{S}$: Ausdehnung in 3 Achsen.
        
    - **Rotation** $\mathbf{R}$: Orientierung im Raum (gespeichert als Quaternion).
        
        $$\mathbf{\Sigma} = \mathbf{R} \mathbf{S} \mathbf{S}^T \mathbf{R}^T$$
- **Opazität** $\alpha$: Transparenzwert.
    
- **Farbe**: Dargestellt über **Spherical Harmonics (SH)**, um richtungsabhängige Reflexionen und Glanzlichter abzubilden.
    

#### 3. Scene Rendering (Splatting)

1. **Projektion**: Die 3D-Gauß-Ellipsoide werden in die 2D-Bildebene der Zielkamera projiziert (EWA-Splatting).
    
2. **Tile-based Sorting**: Das Bild wird in $16 \times 16$ Pixel große Kacheln (Tiles) unterteilt. Die Splats werden extrem schnell nach ihrer Tiefe ($z$-Abstand) auf der GPU sortiert.
    
3. $\alpha$**-Blending**: Zeilenweises Aufakkumulieren der Farben pro Pixel von vorne nach hinten:
    
    $$C = \sum_{i \in N} c_i \alpha_i' \prod_{j=1}^{i-1} (1 - \alpha_j')$$

#### 4. Datenoptimierung (Adaptive Control)

Während des Trainings vergleichen Verlustfunktionen (Loss: $L_1$ + D-SSIM) das gerenderte Bild mit den Originalfotos:

- **Densification (Verdichtung)**:
    
    - _Clone_: Große Bildfehler bei kleinen Splats $\rightarrow$ Duplizieren.
        
    - _Split_: Große Bildfehler bei zu großen Splats $\rightarrow$ Aufspalten in zwei kleinere Splats.
        
- **Pruning (Ausdünnen)**: Entfernen von Splats mit fast transparenter Opazität ($\alpha \approx 0$).
    

> [!tip] Vorteile von 3D Gaussian Splatting
> 
> - **Echtzeit-Rendering**: Extrem schnelle Rasterisierung dank direkter GPU-Sortierung.
>     
> - **Explizite Datenstruktur**: Splats können direkt im 3D-Raum verschoben, skaliert, gecullt oder mit klassischer Geometrie kombiniert werden.
>     

## 🔮 Neuartige Anwendungen & Triangle Splatting

Da 3DGS eine explizite Punktstruktur nutzt, lässt es sich ideal mit Animationen und Rigs kombinieren.

> [!example] Aktuelle Forschungsfelder
> 
> - **GaussianAvatars & Avat3r**: Kopplung von 3D-Gauß-Splats an ein elastisches Bewegungsskelett zur Erzeugung fotorealistischer, animierbarer digitaler Menschen und Gesichter.
>     
> - **Triangle Splatting (2025)**: Übertragung der differentiablen Splatting-Idee von Gauß-Ellipsoiden zurück auf **flache Dreiecks-Primitive**, um bessere Schnittstellen zu klassischen Physik- und Grafik-Pipelines zu schaffen.
>     

## 🔗 Nächste Themen

- [[Virtuelle & Erweiterte Realität]]