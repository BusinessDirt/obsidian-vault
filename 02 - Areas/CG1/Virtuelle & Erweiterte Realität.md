---
date: 2026-07-31
tags: []
---
# 🕶️ Virtuelle & Erweiterte Realität

#computergrafik #lmu #vr #ar #tracking #hmd #immersion #milgram

> [!abstract] Navigation & MOC Zurück zur Hauptübersicht: [[MOC - Computergrafik 1]] Vorheriges Thema: [[Alternative Rendering-Pipelines]]

> [!info] Themenüberblick Diese Notiz behandelt die Grundlagen, Hardware-Komponenten, Tracking-Verfahren und Interaktionskonzepte von Virtual Reality (VR) und Augmented Reality (AR):
> 
> - Das Reality-Virtuality-Continuum (Milgram et al.)
>     
> - Virtual Reality (VR): Meilensteine, Immersion vs. Präsenz, Hardware & Displays
>     
> - Stereo-Rendering, Motion-to-Photon Latency & Motion Sickness
>     
> - Augmented Reality (AR): Definition, Optical See-Through vs. Video See-Through, Handheld AR
>     
> - Tracking-Technologien: 3-DOF vs. 6-DOF, Marker-basiertes Tracking & SLAM
>     
> - UI- & Interaktionskonzepte in AR (Personal Interaction Panel, Emmie)
>     

## 🌌 Das Reality-Virtuality-Continuum

Paul Milgram und Fumio Kishino (1994) definierten das kontinuierliche Spektrum zwischen rein realer und rein virtueller Umgebung, das als **Mixed Reality (MR)** zusammengefasst wird.

```
[ Reale Umwelt ] ──► [ Augmented Reality (AR) ] ──► [ Augmented Virtuality (AV) ] ──► [ Virtuelle Umwelt (VR) ]
└───────────────────────────────────── Mixed Reality (MR) ─────────────────────────────────────┘
```

> [!tip] Einordnung der Begriffe
> 
> - **Reale Umwelt**: Die ungefilterte physikalische Welt ohne digitale Überlagerung.
>     
> - **Augmented Reality (AR)**: Reale Welt dominiert; digitale 3D-Inhalte werden in Echtzeit passgenau eingeblendet.
>     
> - **Augmented Virtuality (AV)**: Virtuelle Welt dominiert; reale Objekte (z. B. Live-Videostreams der eigenen Hände) werden eingebunden.
>     
> - **Virtual Reality (VR)**: Vollständig computergenerierte Welt; die reale Umgebung wird ausgeblendet.
>     

## 🥽 Virtual Reality (VR)

Virtual Reality bezeichnet eine interaktive, computergenerierte Umgebung, in die der Nutzer visuell und akustisch eintaucht.

### Historische Meilensteine

> [!note] Pionierarbeiten der VR-Forschung
> 
> - **Ivan Sutherland's „Sword of Damocles“ (späte 1960er)**:
>     
>     - Erstes historisch bekanntes Head-Mounted Display (HMD).
>         
>     - Mechanisches/ultraschallbasiertes Kopftracking, stereoskopische Drahtgitter-Grafik (Optical See-Through).
>         
> - **Myron Krueger's „Videoplace“ (1989)**:
>     
>     - Begründete das Konzept der „Artificial Reality“.
>         
>     - Kamerabasierte 2D-Schattensimulation: Nutzer interagierten über Projektionen mit virtuellen Objekten und anderen Nutzern.
>         

### Immersion vs. Präsenz (Presence)

> [!warning] Wichtige begriffliche Unterscheidung
> 
> - **Immersion (Objektiv / Technisch)**: Beschreibt das Ausmaß, in dem ein System sensorische Reize der realen Welt ausblendet und durch synthetische Reize ersetzt (z. B. hohes FOV, hohe Auflösung, Head-Tracking, Raumklang).
>     
> - **Präsenz / Presence (Subjektiv / Psychologisch)**: Das mentale Gefühl des Nutzers, sich tatsächlich „an diesem virtuellen Ort zu befinden“ („Being there“).
>     

### VR-Hardware & Display-Technologien

#### 1. Head-Mounted Displays (HMDs)

Tragbare Headsets mit zwei getrennten Displays oder einem geteilten Screen für beide Augen.

- **Stereo-Rendering**: Generierung von zwei perspektivisch korrekten Bildern mit einem leicht versetzten Kameraabstand (Stereobasis / Interpupillardistanz $\approx 6.3 \text{ cm}$).
    
- **Optische Linsenverzerrung (Distortion Correction)**: Die Linsen im Headset verzerren das Licht optisch (Kissenverzerrung). Die Grafik-Pipeline muss das Bild vorab umgekehrt tonnenförmig verzerren (**Barrel Distortion**), damit es das Auge korrekt wahrnimmt.
    

#### 2. CAVE (Cave Automatic Virtual Environment)

Ein kubischer Raum, bei dem 3 bis 6 Wände (inkl. Boden/Decke) von außen mit stereoskopischen Projektoren bespielt werden. Der Nutzer trägt eine Shutter-Brille mit Tracking.

### Motion-to-Photon Latency & Motion Sickness

> [!danger] Das Latenz-Problem **Motion-to-Photon Latency** beschreibt die Zeitverzögerung zwischen der physischen Kopfbewegung des Nutzers und dem fertigen neuen Pixelbild auf dem Display.
> 
> - **Grenzwert**: Muss unter $20 \text{ ms}$ liegen!
>     
> - **Folge bei zu hoher Latenz**: Vokabulärer Widerspruch zwischen dem Gleichgewichtssinn (Vestibuläres System) und dem visuellen System führt zu **Simulator Sickness** (Übelkeit, Schwindel, Kopfschmerzen).
>     

## 👓 Augmented Reality (AR)

Nach Ronald Azuma (1997) ist Augmented Reality durch drei Hauptkriterien definiert:

1. Kombiniert reale und virtuelle Inhalte.
    
2. Interaktiv in Echtzeit.
    
3. Dreidimensional registriert (passgenaue räumliche Verankerung in der realen Welt).
    

### Display-Klassen in AR

> [!note] Visualisierungstechniken in AR
> 
> - **Optical See-Through (OST)**:
>     
>     - Der Nutzer blickt durch halbdurchlässige Spiegel/Gläser direkt auf die reale Welt. Virtuelle Grafiken werden über Projektoren ins Auge reflektiert (z. B. Microsoft HoloLens, Magic Leap).
>         
>     - _Vorteil_: Unverzögerte Wahrnehmung der Realität, volle Augenauflösung.
>         
>     - _Nachteil_: Schwarze/dunkle Farben können nicht projiziert werden; geringes Sichtfeld (FOV).
>         
> - **Video See-Through (VST)**:
>     
>     - Kameras an der Vorderseite eines undurchsichtigen Headsets erfassen die Welt. Das Kamerabild wird mit Grafiken überlagert auf Screens angezeigt (z. B. Apple Vision Pro, Meta Quest Pass-Through).
>         
>     - _Vorteil_: Perfekte Verdeckungsrechnung (Occlusion) möglich, unbegrenztes virtuelles FOV.
>         
>     - _Nachteil_: Kamera-Latenz und eingeschränkte Kameraauflösung.
>         
> - **Handheld AR**:
>     
>     - Nutzung von Alltagsgeräten wie Smartphones oder Tablets (z. B. Pokémon GO, Möbel-Visualisierung).
>         
> - **Spatial AR (Projection-based AR)**:
>     
>     - Direkte Projektion von Licht/Texturen auf physikalische Objekte im Raum.
>         

## 🎯 Tracking in VR & AR

Tracking ist das kontinuierliche Messen der Position und Orientierung von Objekten, Headsets oder Eingabegeräten im Raum.

> [!tip] Freiheitsgrade im Tracking
> 
> - **3-DOF (Degrees of Freedom)**: Erfasst nur Orientierung/Rotation (Roll, Pitch, Yaw / Nicken, Gieren, Wanken). Z. B. einfache Smartphone-VR (Google Cardboard).
>     
> - **6-DOF**: Erfasst 3D-Position $(x, y, z)$ **und** 3D-Orientierung. Unerlässlich für Raum-Skalierte VR/AR.
>     

### Tracking-Verfahren & Sensorik

- **Outside-In Tracking**: Externe Sensoren/Kameras im Raum tracken Marker am Headset (z. B. HTC Vive Base Stations, OptiTrack).
    
- **Inside-Out Tracking**: Kameras am Headset selbst analysieren die Umgebung und berechnen die eigene Bewegung.
    
- **Inertial Measurement Unit (IMU)**: Kombination aus Beschleunigungssensoren (Accelerometer) und Gyroskopen für hochfrequente Rotationsdaten.
    

### AR-Spezifisches Tracking: Marker vs. SLAM

> [!warning] Raum-Registrierung in AR
> 
> - **Marker-basiertes Tracking (z. B. ARToolKit, QR-Codes)**:
>     
>     - Sucht nach bekannten visuellen Mustern mit starkem Kontrast.
>         
>     - Berechnet die exakte Kamera-Pose relativ zum quadratischen Marker aus der Verzerrung der Ecken.
>         
> - **Markerloses Tracking / SLAM (Simultaneous Localization and Mapping)**:
>     
>     - Erfasst unbekannte Räume in Echtzeit.
>         
>     - Erkennt charakteristische Merkmalspunkte (Feature Points) in Videobildern, berechnet eine spärliche 3D-Punktwolke des Raums und schätzt zeitgleich die Bewegung der Kamera.
>         

## 🖐️ UI- & Interaktionskonzepte in AR

Da klassische 2D-WIMP-Interfaces (Windows, Icons, Menus, Pointer) in AR-Umgebungen ungeeignet sind, wurden spezialisierte Räumliche UI-Konzepte erforscht:

> [!example] Bekannte AR-UI-Systeme aus der Forschung
> 
> - **Personal Interaction Panel (PIP / Studierstube)**:
>     
>     - Kombiniert eine echte handgehaltene Holz-Palette mit einem Stift.
>         
>     - Über die Palette wird ein virtuelles 3D-Menü projiziert. Der Nutzer spürt beim Tippen auf das Menü den physischen Widerstand des Brettes (Propriozeption / Haptisches Feedback).
>         
> - **Emmie UI Konzept (1999)**:
>     
>     - Kollaboratives AR-Environment: Nutzer teilen sich Informationsfenster im 3D-Raum, die als virtuelle Widgets an realen Orten oder Personen verankert werden können.
>         
> - **Tangible User Interfaces (TUI)**:
>     
>     - Kopplung von virtuellen Daten an physische Objekte (Greifbare Interaktion), z. B. Drehen eines physischen Würfels zur Steuerung eines 3D-Modells.


