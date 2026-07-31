---
date: 2026-07-31
tags: []
---
# 🔄 Transformationen & Szenengraph

#computergrafik #lmu #transformationen #szenengraph

> [!abstract] Navigation & MOC Zurück zur Hauptübersicht: [[MOC - Computergrafik 1]] Vorheriges Thema: [[Einführung & Grundlagen]]

> [!info] Themenüberblick Diese Notiz behandelt alle Kernkonzepte zu Transformationen und Szenengraphen:
> 
> - 2D- und 3D-Geometrische Transformationen
>     
> - Homogene Koordinaten und 4x4-Matrizen
>     
> - Kombinieren & Verkapseln von Transformationen
>     
> - Konzept, Aufbau und Traversierung des Szenengraphen
>     

## 📐 Geometric Transformations

Transformations sind mathematische Operationen, die Position, Orientierung oder Form von geometrischen Objekten im Raum verändern.

> [!note] Fundamentale Eigenschaften
> 
> - **Kombinierbarkeit**: Mehrere Transformationen können zu einer einzigen zusammengefasst werden.
>     
> - **Invertierbarkeit**: Jede reguläre Transformation besitzt eine Umkehrtransformation (Ausnahme: Skalierung mit Faktor $0$).
>     
> - **Affine Transformationen**: Parallele Linien bleiben nach der Transformation parallel. Punkte, Geraden und Ebenen bleiben erhalten.
>     

### Grundtypen der Transformationen

- **Translation (Verschiebung)**: Verschiebt alle Punkte um einen festen Vektor $\mathbf{t}$.
    
- **Skalierung (Scaling)**:
    
    - _Isotrop (uniform)_: Gleichmäßige Vergrößerung/Verkleinerung in allen Achsen mit dem gleichen Faktor $s$.
        
    - _Anisotrop (non-uniform)_: Unterschiedliche Skalierungsfaktoren ($s_x, s_y, s_z$) je Achse.
        
- **Rotation (Drehung)**: Drehung von Punkten um eine Achse mit einem Winkel $\theta$.
    
- **Scherung (Shear)**: Verschiebung von Koordinaten proportional zu anderen Koordinatenachsen (verzerrt Winkel).
    
- **Spiegelung (Reflection)**: Invertierung von Objektkoordinaten an einer Achse oder Ebene.
    

## 🧮 Homogene Koordinaten

In kartesischen Koordinaten lässt sich eine Skalierung oder Rotation als Matrizenmultiplikation $M \cdot \mathbf{p}$darstellen, eine Translation jedoch nur als Vektoraddition $\mathbf{p} + \mathbf{t}$. Dies verhindert das einfache Zusammenfassen aller Transformationsschritte in eine einzige Matrix.

> [!warning] Klausurrelevanz: Warum homogene Koordinaten? Homogene Koordinaten betten $n$-dimensionale Punkte in einen $(n+1)$-dimensionalen Raum ein.
> 
> - **Einheitliche Darstellung**: Translation wird ebenfalls als Matrizenmultiplikation darstellbar.
>     
> - **Effizienz**: Beliebig viele Transformationen (Translation, Rotation, Skalierung) können zu **einer einzigen Gesamtmatrix** multipliziert werden.
>     
> - **Unterscheidung Punkt vs. Vektor**:
>     
>     - Punkt im 3D-Raum: $\mathbf{p} = \begin{pmatrix} x & y & z & 1 \end{pmatrix}^T$ (wird verschoben)
>         
>     - Vektor (Richtung): $\mathbf{v} = \begin{pmatrix} x & y & z & 0 \end{pmatrix}^T$ (wird durch Translation nicht verändert)
>         

### Die wichtigsten 4x4 Transformationsmatrizen

#### Translation Matrix

$$\mathbf{T}(t_x, t_y, t_z) = \begin{pmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

#### Scaling Matrix

$$\mathbf{S}(s_x, s_y, s_z) = \begin{pmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

#### Rotationsmatrizen um die Hauptachsen

Rotation um die **X-Achse**:

$$\mathbf{R}_x(\theta) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Rotation um die **Y-Achse**:

$$\mathbf{R}_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Rotation um die **Z-Achse**:

$$\mathbf{R}_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

## 🔀 Kombinieren von Transformationen

Da Matrizenmultiplikation **nicht kommutativ** ist ($A \cdot B \neq B \cdot A$), ist die Reihenfolge der Anwendung entscheidend!

> [!danger] Wichtig für Aufgabenstellungen Die Transformationen werden mathematisch von **rechts nach links** auf den Vektor angewendet:
> 
> $$\mathbf{p}' = \mathbf{M}_{ges} \cdot \mathbf{p} = (\mathbf{M}_n \cdot \dots \cdot \mathbf{M}_2 \cdot \mathbf{M}_1) \cdot \mathbf{p}$$
> 
> - Zuerst wird $\mathbf{M}_1$ ausgeführt, danach $\mathbf{M}_2$, bis schlussendlich $\mathbf{M}_n$ angewendet wird.
>     

> [!example] Transformation um einen beliebigen Pivot-Punkt $P$ Möchte man ein Objekt nicht um den Koordinatenursprung, sondern um einen Punkt $P$ rotieren:
> 
> 1. Verschiebe den Punkt $P$ in den Ursprung: $\mathbf{T}(-P)$
>     
> 2. Führe die gewünschte Rotation aus: $\mathbf{R}(\theta)$
>     
> 3. Verschiebe das Objekt zurück: $\mathbf{T}(P)$
>     
> 
> $$\mathbf{M}_{ges} = \mathbf{T}(P) \cdot \mathbf{R}(\theta) \cdot \mathbf{T}(-P)$$

## 🌳 Der Szenengraph (Scene Graph)

Ein Szenengraph ist eine baumförmige Datenstruktur (DAG – Directed Acyclic Graph), die logische und räumliche Beziehungen zwischen Objekten einer 3D-Szene repräsentiert.

> [!tip] Vorteile eines Szenengraphen
> 
> - **Hierarchische Transformationen**: Unterobjekte (Child-Nodes) erben automatisch die Transformationen ihrer Elternknoten (Parent-Nodes).
>     
> - **Wiederverwendbarkeit**: Komplexe Objekte können definiert und an verschiedenen Stellen der Szene instanziiert werden.
>     
> - **Strukturierung**: Abstraktion von hardwarenahen OpenGL/WebGL-Aufrufen auf ein objektorientiertes Modell.
>     

### Was speichert ein Szenengraph?

Ein Szenengraph besteht aus verschiedenen Knotenarten:

- **Transformations-Knoten**: Entspricht einer Matrizen-Transformation für den darunterliegenden Teilbaum.
    
- **Geometrie- / Objekt-Knoten**: Reale 3D-Formen (Polygon-Meshes, Primitive).
    
- **Material- / Appearance-Knoten**: Farb-, Textur- und Shaderinformationen.
    
- **Kamera- & Licht-Knoten**: Position und Parameter von Betrachtungspunkten und Beleuchtung.
    

```
       [ Root Node ]
             │
     ┌───────┴───────┐
     ▼               ▼
[Trans: T1]     [Trans: T2]
     │               │
     ▼               ▼
[ Body Mesh ]   [ Arm Group ]
                     │
             ┌───────┴───────┐
             ▼               ▼
        [Trans: T3]     [Trans: T4]
             │               │
             ▼               ▼
       [ Hand Mesh ]   [ Finger Mesh ]
```

### Traversierung & Matrix-Stack

Beim Rendering wird der Szenengraph per **Tiefensuche (Depth-First Search)** durchlaufen.

> [!note] Funktionsweise des Matrix-Stacks
> 
> 1. Beim Abstieg zu einem Kindknoten wird die aktuelle Transformationsmatrix dupliziert und auf den **Stack gelegt (Push)**.
>     
> 2. Die lokale Transformation des Kindknotens wird auf die bestehende Matrix aufmultipliziert.
>     
> 3. Nach dem Rendern des Teilbaums wird der Ursprungszustand vom Stack wieder **wiederhergestellt (Pop)**.
>     

### Praktische Szenengraph-Bibliotheken

- **Three.js** (JavaScript/WebGL): Sehr verbreitet im Web-Bereich (`THREE.Scene`, `THREE.Group`, `THREE.Mesh`).
    
- **Game Engines**: Unity (Transform-Hierarchie), jMonkeyEngine.
    
- **Historische / Standards**: VRML / X3D, OpenInventor, Open Scene Graph (OSG).
    

## 🔗 Nächste Themen

- [[3D-Geometrie & Modellierung]]
    
- [[Kameramodell & Projektion]]
    
- [[Rasterisierung]]