---
date: 2026-07-31
tags:
  - 3D
  - Computergrafik
  - DOF
  - Gizmo
  - Interaktion
  - LMU
  - Raycasting
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Animation]] | Nächstes Thema: [[Alternative Rendering-Pipelines]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu 3D-Interaktion:
> - 2D- vs. 3D-Eingabegeräte & Freiheitsgrade (DOF)
> - 3D-Navigation & Kamerasteuerung (Kanonische Bewegungen & Metaphern)
> - Objektselektion & -manipulation (Ray Casting, Go-Go, Image Plane Interaction)
> - [[3D-Interaktion#3D-Widgets & Gizmos|3D-Widgets & Transformations-Gizmos]]

## Die Lücke: 2D-Eingabe vs. 3D-Szenengraph

Die meisten klassischen Eingabegeräte (Maus, Touchscreen, Grafiktablett) arbeiten primär auf einem **zweidimensionalen Raster** und Bildschirmen. Das Rendering-Ergebnis der [[Pipeline|Grafik-Pipeline]] ist ebenfalls ein 2D-Pixelbild.

> [!warning] Die Interaktions-Herausforderung 
> Interaktionen sollen jedoch Objekte innerhalb der **dreidimensionalen Welt (Szenengraph)** verändern.
> - **Problem**: Abbildung von 2D-Bildschirmkoordinaten $(x, y)$ auf 3D-Transformationen $(x, y, z, \text{Rotation}, \text{Skalierung})$.
> - **Lösung**: Mathematische Mappings, Constraints (Einschränkungen auf Achsen/Ebenen) und räumliche Hilfskonstrukte (Gizmos).

### Freiheitsgrade (Degrees of Freedom - DOF)

Die Anzahl unabhängiger Bewegungsmöglichkeiten eines Objekts im Raum bestimmt seine Freiheitsgrade:

> [!tip] Einteilung der Freiheitsgrade (DOF)
> - **3 DOF (Translation oder Rotation)**:
>     - Reine Position im Raum $(x, y, z)$ **oder** reine Orientierung (Roll, Pitch, Yaw / Wanken, Nicken, Gieren).
> - **6 DOF (Vollständige 3D-Transformation)**:
>     - Kombination aus 3 Translationsachsen $(x, y, z)$ und 3 Rotationsachsen $(\theta_x, \theta_y, \theta_z)$.

## 3D-Eingabegeräte & Sensorik

Um 3D-Welten direkt zu steuern, wurden verschiedene Eingabegeräte entwickelt:

> [!note] Übersicht von Eingabegeräten
> - **2D-Standardgeräte (Maus, Touch)**: Benötigen spezielle Modi oder Modifier-Tasten (z. B. `Shift` + Ziehen), um die dritte Dimension $z$ anzusprechen.
> - **3D-Maus (z. B. 3Dconnexion SpaceNavigator)**: Optoelektronischer Druck-/Zugknopf, der Krafterfassungen in 6 Achsen gleichzeitig ermöglicht (ideal für CAD und Kamerafahrt).
> - **Spatial Tracker & VR-Controller**:
>     - Erfassen Position und Orientierung im Raum via optischem Tracking (Inside-Out / Outside-In), [[Elektromagnetische Strahlung|elektromagnetischen Feldern]] oder Inertialsensoren (IMU: Beschleunigungsmesser & Gyroskop).
> - **Datenhandschuhe (Data Gloves) & Hand-Tracking**:
>     - Erfassung von Fingerbiegungen und Handgesten zur natürlichen Interaktion.
> - **Gamepad & Wiimote**:
>     - Analog-Sticks kombiniert mit Infrarot- oder Bewegungssensoren.

## Navigation in 3D-Szenen

Navigation bezeichnet die gezielte Veränderung des Betrachterstandpunkts (Steuerung der virtuellen Kamera bzw. View-[[Matrix]]).

### Kanonische Kamerabewegungen

> [!info] Die 3 Grundbewegungen der Kamera
> - **Orbit (Rotate / Turntable)**: Drehen der Kamera um einen festgelegten Fokus-/LookAt-Punkt auf einer virtuellen Kugeloberfläche.
> - **Pan (Track / Translate)**: Parallelverschiebung der Kamera quer zur Blickrichtung (entlang der lokalen $X$- und $Y$-Achse der Kamera).
> - **Dolly / Zoom**:
>     - _Dolly_: Physisches Verschieben der Kamera-Position entlang der optischen Achse ($Z$-Achse). Verändert Parallaxe und Perspektive.
>     - _Zoom_: Verändern der Brennweite / des Öffnungswinkels (FOV) bei starrer Kameraposition.

### Navigationsmetaphern

Je nach Anwendungsfall werden unterschiedliche mentale Modelle zur Kamerasteuerung verwendet:

- **Virtual Sphere / Arcball (Eyeball-in-Hand)**:
    Um das Zielobjekt wird gedanklich eine transparente Kugel gelegt. Mausbewegungen auf dem 2D-Bildschirm rotieren diese Kugel.
- **World-in-Hand**:
    Der Nutzer bewegt gedanklich nicht die Kamera, sondern packt und verschiebt die gesamte [[Dimension|3D-Welt]].
- **Flying / First-Person (Fly-through / WASD)**:
    Freie Flug-Steuerung wie in einem Ego-Shooter (Maus steuert Blickrichtung, Tastatur bewegt die Position vor/zurück/seitlich).
- **Walking & Teleportation (VR-Standard)**:
    Boden-gebundenes Gehen oder kurzzeitiges Punkt-zu-Punkt-Springen (Teleport-Strahl), um Reisekrankheit (Motion Sickness) zu vermeiden.

## Selektion & Manipulation von 3D-Objekten

Bevor ein Objekt im [[Dimension|3D-Raum]] transformiert werden kann, muss es ausgewählt (selektiert) werden.

### 1. Direct 3D Manipulation

Greifen von Objekten mit einer virtuellen Hand oder einem 6-DOF-Controller, wenn sich das Objekt in unmittelbarer Reichweite befindet.

### 2. Ray Casting (Laser Pointer Metapher)

Standardverfahren für die Selektion aus der Distanz.

> [!note] Funktionsweise von Ray Casting
> 1. Erzeuge einen virtuellen unendlichen Strahl (Ray), ausgehend von der Kamera/Mausposition oder dem VR-Controller in Blickrichtung:
>     $$\mathbf{r}(t) = \mathbf{o} + t \cdot \mathbf{d} \quad \text{mit } t \ge 0$$
> 2. Berechne Schnittpunkte (Ray-Triangle-Intersections oder Bounding-Box-Tests) mit allen Objekten der Szene.
> 3. Das Objekt mit dem kleinsten positiven Schnittabstand $t_{min}$ wird selektiert.

> [!danger] Problem beim Ray Casting 
> Bei sehr kleinen oder weit entfernten Objekten führt Handzittern (Tremor) dazu, dass das Objekt schwer zu treffen ist.
> - **Lösung**: **Cone Casting / Spotlight** – Verwende einen virtuellen Lichtkegel anstelle eines dünnen Strahls.

### 3. Go-Go-Technik (Non-Linear Arm Extension)

Ermöglicht das Greifen von Objekten außerhalb der physischen Armreichweite durch eine nicht-lineare Skalierung der Armlänge:

- Arme nah am Körper: **1:1 Übersetzung** für präzise Nahinteraktion.
- Arme weiter ausgestreckt: **Überproportionales Wachstum** der virtuellen Hand in die Tiefe ($O(d^2)$).

### 4. Image Plane Interaction (2D-Bildebenen-Interaktion)

Selektion und Manipulation direkt im projizierten [[Dimension|2D-Kamerabild]] (häufig bei HMDs oder Touchscreens):

> [!example] Techniken der Bildebenen-Interaktion
> - **Head Crusher**: Das entfernte 3D-Objekt wird im [[Dimension|2D-Kamerabild]] gedanklich zwischen Daumen und Zeigefinger „zerquetscht“ und dadurch gegriffen.
> - **Sticky Finger**: Platzieren des Fingers auf dem Bildschirm-Imagepunkt des Objekts.
> - **Framing Hands**: Aufspannen eines Rahmens mit beiden Händen zur Objektauswahl.

## 3D-Widgets & Gizmos

3D-Widgets sind visuelle Steuerungselemente, die direkt in die [[Dimension|3D-Szene]] gerendert werden, um komplexe 3D-Transformationen mit einfachen 2D-Mausbewegungen durchzuführen.

> [!tip] Aufbau eines 3D-Transformations-Gizmos
> - **Translations-Pfeile**: 3 farbige Achsenpfeile ($X$=Rot, $Y$=Grün, $Z$=Blau). Klicken und Ziehen schränkt die Bewegung exakt auf diese eine Achse ein.
> - **Ebenen-Quadrate**: Kleine Flächen zwischen zwei Achsen erlauben Verschiebungen parallel zu einer Haupt-Koordinatenebene ($XY, XZ, YZ$).
> - **Rotations-Ringe**: Kreisförmige Ringe um die Objektmitte ermöglichen Rotationen um die jeweilige Achse.
> - **Skalierungs-Boxen**: Würfel an den Achsenenden skalieren das Objekt isotrop oder anisotrop.

```
          Y (Grün)
          ▲
          │  ┌── Ebene YZ
          │ /
          │/
──────────┼──────────► X (Rot)
         /│
        / │
       ▼  ▼
 Z (Blau)
```

## Nächste Themen

- [[Alternative Rendering-Pipelines]]
- [[Virtuelle & Erweiterte Realität]]