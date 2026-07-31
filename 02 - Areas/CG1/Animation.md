---
date: 2026-07-31
tags:
  - Animation
  - Computergrafik
  - Disney
  - Keyframing
  - Kinematik
  - LMU
  - MoCap
  - Simulation
---
> [!abstract] Navigation & MOC
> Zurück zur Hauptübersicht: [[Computergrafik 1]]
> Vorheriges Thema: [[Shading & Rendering]] | Nächstes Thema: [[3D-Interaktion]]

> [!info] Themenüberblick
> Diese Notiz behandelt alle Kernkonzepte zu Animation:
> - Grundlagen & Geschichte der [[Animation]]
> - [[Animation#Keyframing & Interpolation|Keyframing]] & Parameter-Interpolation
> - [[Animation#Skelettanimation & Motion Capture|Skelettanimation]] (Rigging, Forward vs. Inverse Kinematics) & Motion Capture
> - [[Animation#Physikalische Simulation|Physikalische Simulation]] (Partikel, Masse-Feder-Systeme, Rigid Bodies)
> - Die [[Animation#Die 12 Prinzipien der Animation (Disney)|12 klassischen Prinzipien der Animation]] (Disney)

## ⏱ Grundlagen der Animation

Das Wort Animation stammt vom lateinischen _animare_ („zum Leben erwecken“). Es bezeichnet die Erzeugung der Illusion von Bewegung durch die schnelle Abfolge von statischen Einzelbildern (Frames).

> [!note] Wahrnehmungsphysiologie & Bildraten
> - **Nachbildwirkung (Trägheit des Auges)**: Das menschliche Auge behält ein Bild für einen kurzen Moment auf der Netzhaut.
> - **Bewegungseindruck**: Setzt ab ca. $6 \text{ bis } 10 \text{ Frames pro Sekunde (fps)}$ ein.
> - **Klassische Bildraten**:
>     - Kinofilm: $24 \text{ fps}$
>     - Fernsehen (PAL/NTSC): $25 \text{ / } 30 \text{ fps}$
>     - Interaktive [[Dimension|3D-Grafik]] / Gaming: $60 \text{ bis } 144+ \text{ fps}$ für flüssige Interaktion.
>
## Keyframing & Interpolation

In der klassischen Zeichentrick-Herstellung zeichneten Chefzeichner nur die wichtigsten Hauptbilder (**Keyframes**), während Assistenten die Zwischenbilder (**Inbetweens**) anfertigten. In der Computergrafik übernimmt der Computer die Rolle des Inbetweeners.

> [!tip] Prinzip des digitalen Keyframings
> 1. Der Animator legt zu bestimmten Zeitpunkten $t_0, t_1, \dots$ Schlüsselwerte für Objektparameter fest (z. B. Position, Rotation, Skalierung, Farbe, Kamera-FOV).
> 2. Die Grafiksoftware berechnet für alle Frames dazwischen automatisch die Werte mittels mathematischer **Interpolationsfunktionen**.
>
```
[ Keyframe t0 ] ──────── Interpolationskurve (Spline) ────────► [ Keyframe t1 ]
  (Pos: x0, y0)                                                   (Pos: x1, y1)
```

### Interpolationsarten

- **Lineare Interpolation**:

    $$P(t) = (1 - t) \cdot P_0 + t \cdot P_1 \quad \text{mit } t \in [0, 1]$$

    Erzeugt abrupte, unnatürliche Richtungswechsel und Geschwindigkeitsänderungen an den Keyframes (Ecken in der Bewegung).

- **Spline- / Bézier-Interpolation**: Verwendet kubische Kurven zur sanften Überblendung. Ermöglicht **Ease-In**(sanftes Anfahren/Beschleunigen) und **Ease-Out** (sanftes Abbremsen).

## Skelettanimation & Motion Capture

Um komplexe organische Charaktere (Menschen, Tiere, Monster) realistisch zu bewegen, nutzt man eine Trennung von Oberflächengeometrie und Bewegungsstruktur.

### Rigging & Skinning

- **Rigging**: Erstellung eines inneren virtuellen Skeletts aus miteinander verknüpften Knochen (Bones/Joints) in einer Baumhierarchie.
- **Skinning / Weighting**: Verknüpfung der äußeren Mesh-[[Knoten|Vertices]] mit den Knochen. Jeder Vertex erhält Gewichtungsfaktoren (Weights), die angeben, zu wie viel Prozent er der Bewegung welches Knochens folgt.

### Forward vs. Inverse Kinematics (FK vs. IK)

> [!warning] Klausurrelevanz: FK vs. IK
> - **Forward Kinematics (FK - Vorwärtskinematik)**:
>     - Steuerung erfolgt **von oben nach unten** in der Hierarchie.
>     - Der Animator rotiert die Gelenke einzeln (z. B. Schulter $\rightarrow$ Ellbogen $\rightarrow$Handgelenk).
>     - Die Position der Hand (Endeffektor) ergibt sich aus der Aufmultiplikation der Transformationsmatrizen.
> - **Inverse Kinematics (IK - Inverse Kinematik)**:
>     - Steuerung erfolgt **von unten nach oben**.
>     - Der Animator gibt nur die gewünschte Zielposition der Hand (Endeffektor) vor.
>     - Der Algorithmus berechnet mathematisch die dafür notwendigen Rotationswinkel aller übergeordneten Gelenke (Schulter und Ellbogen).
>
### Motion Capture (MoCap)

Erfassung der Bewegungen realer Darsteller mithilfe von Sensoren oder Markern (optisch, magnetisch, exskelettal) und Übertragung der 3D-Koordinaten auf das virtuelle Rig des Charakters.

## Physikalische Simulation

Für Phänomene mit extrem vielen Freiheitsgraden ist manuelle Keyframe-Animation unpraktisch. Hier kommen physikalische Gesetzmäßigkeiten (Newton'sche Mechanik) zum Einsatz.

> [!note] Simulationsverfahren
> - **Partikelsysteme (Particle Systems)**: Erzeugung großer Mengen einfacher Partikel mit Masse, Lebensdauer und Geschwindigkeit zur Simulation von Feuer, Rauch, Funken, Wasserfällen oder Schnee.
> - **Masse-Feder-Systeme (Mass-Spring Systems)**: Punkte im Raum werden durch elastische Federn verbunden. Dient zur Simulation flexibler Textilien (Cloth Simulation), Seilen und weichen Körpern.
> - **Rigid Body Dynamics (Körperdynamik)**: Berechnung von Kollisionen, Reibung und [[Impuls|Impulserhaltung]] unformbarer [[Dimension|3D-Körper]] (z. B. einstürzende Mauern, Würfel).
>
## Die 12 Prinzipien der Animation (Disney)

Von Frank Thomas und Ollie Johnston (Disney-Animatoren) in den 1980ern formuliert, bilden diese Regeln die Basis für ausdrucksstarke und glaubwürdige Bewegungen.

> [!example] Übersicht der 12 Animationsprinzipien
> 1. **Squash & Stretch (Stauchen & Dehnen)**: Vermittelt Flexibilität, Materialhärte und Masse. _Wichtig_: Das Gesamtvolumen des Objekts muss konstant bleiben!
> 2. **Anticipation (Ausholbewegung / Vorbereitung)**: Bereitet den Betrachter auf eine bevorstehende Aktion vor (z. B. In-die-Knie-Gehen vor einem Sprung).
> 3. **Staging (Inszenierung)**: Anordnung von Objekten, Kamera und Aktionen, um die Haupthandlung unmissverständlich und klar zu vermitteln (Maximierung der Silhouette).
> 4. **Straight Ahead Action vs. Pose to Pose**:
>     - _Straight Ahead_: Bild für Bild fortlaufend zeichnen (spontan, dynamisch, z. B. für Feuer).
>     - _Pose to Pose_: Zuerst Hauptposen (Keyframes) setzen, dann Zwischenbilder auffüllen (kontrolliert, strukturiert).
> 5. **Follow Through & Overlapping Action (Nachlaufende & versetzte Bewegung)**:
>     - _Follow Through_: Lose Teile (Haare, Mantel, Ohren) bewegen sich nach dem Stoppen des Körpers noch weiter.
>     - _Overlapping Action_: Verschiedene Körperteile bewegen sich zu leicht unterschiedlichen Zeiten.
> 6. **Slow In & Slow Out**: Bewegung beschleunigt sanft beim Start und bremst vor dem Ziel ab (Verwendung von Spline-Interpolation).
> 7. **Arcs (Bewegungsbögen)**: Natürliche Bewegungen von Lebewesen folgen fast immer geschwungenen Kreisbögen statt starrer gerader Linien.
> 8. **Secondary Action (Sekundäraktion)**: Zusätzliche untergeordnete Bewegungen, die die Hauptaktion unterstützen und verstärken (z. B. Pfeifen oder Armschwingen beim Gehen).
> 9. **Timing**: Die Anzahl der Frames für eine Aktion bestimmt deren Geschwindigkeit, Wirkung und gefühltes Gewicht.
> 10. **Exaggeration (Übertreibung)**: Maßvolle Überhöhung von Bewegungen und Mimik zur Steigerung der Dramatik und des emotionalen Ausdrucks.
> 11. **Solid Drawing / Weight (Glaubwürdige Anatomie & Gewicht)**: Beachtung von 3D-Volumen, Gewicht, Balance und physikalischen Dichteunterschieden.
> 12. **Appeal (Ausstrahlung / Charme)**: Ansprechende Gestaltung und Konsistenz von Charakteren und deren Persönlichkeit.
>
## Nächste Themen

- [[3D-Interaktion]]
- [[Alternative Rendering-Pipelines]]
- [[Virtuelle & Erweiterte Realität]]