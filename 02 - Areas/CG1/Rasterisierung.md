---
date: 2026-07-31
tags:
  - Antialiasing
  - Bresenham
  - Clipping
  - Computergrafik
  - LMU
  - Rasterisierung
  - Scanline
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Kameramodell & Projektion]] | Nächstes Thema: [[Licht, Aussehen & Material]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu Rasterisierung:
> - Aufgabe & Prinzip der [[Rasterisierung]]
> - [[Rasterisierung#Clipping (Beschneidung)|Clipping]]-Algorithmen (Cohen-Sutherland für Linien, Sutherland-Hodgman für Polygone)
> - Linienrasterisierung (DDA-Algorithmus, [[Rasterisierung#2. Bresenham-Algorithmus (Midpoint Line Algorithm)|Bresenham-Algorithmus]])
> - Polygonfüllung ([[Rasterisierung#Flächenfüllen (Filling Areas)|Scanline-Algorithmus]] & Paritätsregel)
> - [[Rasterisierung#Antialiasing (Kantenglättung)|Antialiasing]] & Supersampling

## Was ist Rasterisierung?

Die Rasterisierung bildet die Brücke zwischen kontinuierlicher Vektorgeometrie (Punkte, Linien, Polygone im 2D/[[Dimension|3D-Raum]]) und dem diskreten Pixelraster eines Bildschirms.

> [!note] Kernaufgabe 
> Bestimme für jedes geometrische Primitiv (z. B. ein projiziertes 2D-Dreieck in Viewport-Koordinaten), welche Pixel des Framebuffers davon überdeckt werden und welche Farb- bzw. Tiefenwerte diese Pixel erhalten.

## Clipping (Beschneidung)

Geometrie, die sich außerhalb des sichtbaren Bildschirmfensters (Viewport / Clipping Rectangle) befindet, muss vor der Rasterisierung abgeschnitten oder verworfen werden.

> [!tip] Warum Clipping?
> - **Effizienz**: Vermeidet unnötige Rasterisierungsberechnungen für nicht sichtbare Objekte.
> - **Fehlervermeidung**: Verhindert Speicherzugriffsfehler (Out-of-Bounds) beim Schreiben in den Framebuffer.

### 1. Cohen-Sutherland-Algorithmus (Line Clipping)

Der Cohen-Sutherland-Algorithmus teilt den 2D-Raum durch das Clipping-Rechteck in 9 Regionen ein und weist jedem Endpunkt $P$ einer Linie einen **4-Bit-Outcode** `[Top, Bottom, Right, Left]` zu:

- `10xx`: Punkt liegt **oberhalb** des Rechtecks.
- `01xx`: Punkt liegt **unterhalb** des Rechtecks.
- `xx10`: Punkt liegt **rechts** vom Rechteck.
- `xx01`: Punkt liegt **links** vom Rechteck.
- `0000`: Punkt liegt **innerhalb** des Rechtecks.

> [!warning] Fallunterscheidung mit bitweisen Operationen Für die Endpunkte $P$ und $Q$ einer Linie gilt:
> - **Trivial Accept (**$P \text{ OR } Q == 0000$**)**: Die Linie liegt vollständig innerhalb des Rechtecks $\rightarrow$ **Unverändert zeichnen**.
> - **Trivial Reject (**$P \text{ AND } Q \neq 0000$**)**: Beide Punkte liegen auf derselben äußeren Seite des Rechtecks $\rightarrow$ **Komplett verwerfen**.
> - **Sonst**: Die Linie schneidet mindestens eine Kante. Berechne den Schnittpunkt mit der Kante und wende den Algorithmus rekursiv auf die gekürzten Segmente an.

### 2. Sutherland-Hodgman-Algorithmus (Polygon Clipping)

Beschneidet ein gesamtes Polygon nacheinander an den vier Begrenzungskanten eines konvexen Clipping-Fensters.

> [!note] Die 4 Fälle beim Ablaufen der Kanten $V_i \rightarrow V_{i+1}$
> 1. **Drinnen** $\rightarrow$ **Drinnen**: Speichere Endpunkt $V_{i+1}$.
> 2. **Drinnen** $\rightarrow$ **Draußen**: Berechne Schnittpunkt $I$ mit der Kante und speichere nur $I$.
> 3. **Draußen** $\rightarrow$ **Draußen**: Speichere keinen Punkt.
> 4. **Draußen** $\rightarrow$ **Drinnen**: Berechne Schnittpunkt $I$, speichere $I$ und den Endpunkt $V_{i+1}$.

## Linienrasterisierung (Drawing Lines)

Eine mathematische Linie $y = m \cdot x + b$ muss auf eine Folge diskreter Rasterpixel $(x, y) \in \mathbb{Z}^2$abgebildet werden.

### 1. DDA-Algorithmus (Digital Differential Analyzer)

Inkrementeller Ansatz: Gehe in Einzelsschritten entlang der Hauptachse ($\Delta x = 1$ für $\vert{}m\vert{} \le 1$) und berechne den neuen $y$-Wert kontinuierlich durch Addition der Steigung $m$.

$$x_{k+1} = x_k + 1, \quad y_{k+1} = y_k + m$$

> [!danger] Nachteil des DDA 
> Erfordert in jeder Iteration **Gleitkomma-Additionen** und Rundungsoperationen (`round(y)`), was auf Hardware langsam ist.

### 2. Bresenham-Algorithmus (Midpoint Line Algorithm)

Der Bresenham-Algorithmus löst das Problem rein mittels **Ganzzahlarithmetik (Integer Arithmetic)**.

> [!tip] Funktionsprinzip 
> Angenommen, der Pixel $(x_k, y_k)$ wurde gezeichnet. Für den nächsten Schritt $x_k + 1$ kommen nur zwei Nachbarpixel infrage:
> - Östlicher Nachbar $E = (x_k + 1, y_k)$
> - Nord-östlicher Nachbar $NE = (x_k + 1, y_k + 1)$
>
> Der Algorithmus prüft über eine **Ganzzahl-Entscheidungsvariable** $d$, ob die reale mathematische Linie oberhalb oder unterhalb des Mittelpunkts $M$ zwischen $E$ und $NE$ verläuft.

> [!note] Vorteile des Bresenham-Algorithmus
> - Keine Gleitkomma-Operationen (kein `float`, keine Multiplikation, keine Division im Haupt-Loop).
> - Nur Additionen, Subtraktionen und Bit-Shifts (`<< 1` für Multiplikation mit 2).
> - Extrem effizient direkt in Grafikhardware (GPUs) umsetzbar.

## Flächenfüllen (Filling Areas)

Das Füllen von geschlossenen 2D-Polygonen erfolgt standardmäßig über den **Scanline-Algorithmus**.

### Scanline-Algorithmus & Paritätsregel (Even-Odd Rule)

Der Algorithmus tastet das Bildelement zeilenweise von oben nach unten (oder unten nach oben) ab.

> [!tip] Bestimmung der Innen-/Außenbereiche (Parität) 
> Um zu entscheiden, ob ein Pixel $(x, y)$ innerhalb des Polygons liegt:
> 1. Sende einen gedanklichen Strahl vom Pixel ins Unendliche.
> 2. Zähle die Anzahl der Schnittpunkte des Strahls mit den Polygonkanten.
> 3. **Parität 0 (Gerade Anzahl)**: Pixel liegt **außerhalb** (Even) $\rightarrow$ Nicht zeichnen.
> 4. **Parität 1 (Ungerade Anzahl)**: Pixel liegt **innerhalb** (Odd) $\rightarrow$ Pixel füllen.

```
Scanline y ───►  [Außen (0)] ──| Edge 1 |──► [Innen (1)] ──| Edge 2 |──► [Außen (0)]
```

> [!note] Optimierung mittels Edge Tables 
> Um nicht in jeder Zeile alle Kanten prüfen zu müssen, verwaltet der Algorithmus eine **Edge Table (ET)** und eine **Active Edge Table (AET)**. Letztere enthält nur diejenigen Kanten, die die aktuelle Scanline kreuzen, sortiert nach ihren $x$-Schnittpunkten.

## Antialiasing (Kantenglättung)

Da Pixel diskrete Quadrate sind, führen harte Übergänge an Polygonkanten zu störenden Treppeneffekten (Jaggies / Aliasing).

> [!warning] Abtasttheorem (Nyquist-Shannon) Hard Edges entsprechen unendlich hohen Raumfrequenzen im Bildsignal. Wird die Abtastfrequenz des Pixelrasters unterschritten, entsteht Aliasing.

### Supersampling (SSAA - Supersample Anti-Aliasing)

Die grundlegendste und qualitativ hochwertige Technik zur Kantenglättung.

> [!example] Funktionsweise von Supersampling
> 1. Rendere das Bild intern mit einer deutlich höheren Auflösung (z. B. $2\times2 = 4$ Subpixel pro Bildpixel).
> 2. Berechne für jeden Subpixel Farbe und Sichtbarkeit.
> 3. Skaliere das Bild auf die Zielauflösung herunter, indem der Farbwert eines Pixels durch den **Mittelwert seiner Subpixel** gebildet wird (Tiefpassfilterung).
>
## Nächste Themen

- [[Licht, Aussehen & Material]]
- [[Shading & Rendering]]