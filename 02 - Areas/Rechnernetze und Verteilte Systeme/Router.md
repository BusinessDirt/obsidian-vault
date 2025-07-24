---
date: 2025-07-24T16:22
tags:
  - Rechnernetze
  - Informatik
  - Internet
---
> Ein **Router** ist ein Netzwerkgerät, das **Datenpakete zwischen Netzwerken weiterleitet**
> Er sorgt dafür, dass ein [[IP]]-Paket **vom Absender zum Empfänger gelangt**, auch wenn sie sich in völlig unterschiedlichen Netzwerken befinden


## [[IP]] Routing
1. **Ein Paket wird verschickt**: Dein PC will z.B. mit `142.251.37.4` (Google) kommunizieren
2. **Zieladresse wird geprüft**: Dein PC sieht: Die [[IP]] gehört **nicht** zum lokalen Netzwerk
3. **Standardgateway (Router) wird verwendet**: Das Paket wird an den **Router** weitergeleitet
4. **Router entscheidet den nächsten Schritt**: Der Router schaut in seine **Routing-Tabelle** und fragt sich: “Über welches Interface/Netz muss ich dieses Paket weiterschicken, um es näher ans Ziel zu bringen?”

# Router Advertisement (RA)