---
date: 2026-04-09 11:02
tags:
  - PHPC
  - Latenz
  - Bandbreite
  - Durchmesser
  - Bisektionsbandbreite
  - Hypercube
  - Mesh
  - Torus
  - Fat-Tree
links: "[[MPI - Grundlagen & P2P]]"
---
## 1. Netzwerkeigenschaften & Bewertungsmetriken

Das Interconnection Network verbindet die einzelnen Knoten eines HPC-Clusters. Die Güte wird anhand folgender Kennzahlen bewertet:

* **Latenz ($\tau$):** Zeitverzögerung bis zum Eintreffen des ersten Bits beim Empfänger.
* **Bandbreite ($b$):** Datenmenge, die pro Zeiteinheit übertragen werden kann (Bytes/s).
* **Durchmesser (Diameter $D$):** Maximale Anzahl von Kanten auf dem kürzesten Pfad zwischen zwei beliebigen Knoten im Netzwerk.
* **Knotengrad (Degree $d$):** Anzahl der direkten Netzwerklinks pro Knoten.
* **Bisektionsbandbreite (Bisection Bandwidth):** Minimale Bandbreite, die getrennt werden muss, um das Netzwerk in zwei genau gleich große Hälften zu schneiden.

---

## 2. Netzwerktopologien im Vergleich

| Topologie | Knotenanzahl $N$ | Durchmesser $D$ | Knotengrad $d$ | Bisektionsbreite | Bewertung / Einsatz |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bus** | $N$ | $1$ | $1$ | $1$ | Nicht skalierbar. |
| **Crossbar** | $N$ | $1$ | $N$ | $N / 2$ | Perfekt, aber quadratische Kosten $O(N^2)$. |
| **2D Mesh** | $k^2$ | $2(k-1)$ | $4$ | $k$ | Einfach, hohe Latenz bei großen $N$. |
| **2D Torus** | $k^2$ | $2 \lfloor k/2 \rfloor$ | $4$ | $2k$ | Mesh mit Randecken-Verbindung. |
| **n-Hypercube** | $2^n$ | $n = \log_2 N$ | $n = \log_2 N$ | $N / 2$ | Sehr kleiner Durchmesser, hoher Verkabelungsaufwand. |
| **Fat-Tree** | Variabel | $2 \times \text{Höhe}$ | Konstant | Konstant hoch | **Standard in modernen HPC-Clustern (InfiniBand)**. |

---

## 3. Details zu wichtigen Topologien

### n-Dimensionaler Hypercube
Ein $n$-dimensionaler Hypercube verbindet $N = 2^n$ Knoten. Zwei Knoten sind genau dann verbunden, wenn sich ihre binären Adressen in genau einem Bit unterscheiden (Hamming-Distanz = 1).

> [!TIP] Vorteil des Hypercube
> Der Durchmesser wächst nur logarithmisch mit der Knotenanzahl ($D = \log_2 N$), und die Bisektionsbandbreite skaliert hervorragend ($N/2$).

### Fat-Tree Topologie
In einem Fat-Tree nimmt die Bandbreite der Netzwerkverbindungen von den Blättern (Rechenknoten) nach oben zur Wurzel (Core Switches) hin zu. Dies verhindert Engpässe (Bottlenecks) an den oberen Switches bei All-to-All-Kommunikation.

---

## 4. Routing-Mechanismen

* **Store-and-Forward Routing:** Eine Nachricht wird an jedem Zwischenknoten vollständig empfangen und zwischengespeichert, bevor sie weitergeleitet wird. (Latenz skaliert proportional zur Hop-Anzahl).
* **Wormhole Routing:** Nachrichten werden in winzige Flusskontrolleinheiten (**Flits**) zerlegt. Der Header-Flit bahnt den Weg durch die Switches; nachfolgende Flits folgen pipelined. (Latenz ist nahezu unabhängig von der Distanz!).
