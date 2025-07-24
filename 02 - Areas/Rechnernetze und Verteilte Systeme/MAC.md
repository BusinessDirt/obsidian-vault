---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Schicht-2
aliases:
  - Media Access Control
  - MAC-Adresse
---
>  Eine MAC-Adresse (**Media Access Control**) ist eine physikalische Adresse, die einem Netzwerkadapter fest zugewiesen ist.
>  Sie ist weltweit eindeutig (meist in die Hardware eingebrannt) und besteht aus 48 Bit, dargestellt in 6 Gruppen zu je 2 Hex-Zeichen. Beispiel: <code>00:1A:2B:3C:4D:5E</code>
>  MAC-Adressen gelten nur bis zum nächsten Router oder Gateway, also im lokalen Netz

## Funktion
In einem lokalen Netzwerk laufen die Dinge ungefähr so ab:

a) Sender kennt MAC-Adresse des Empfängers
- Sender fügt beide Adressen (Sender und Empfänger) in den Ethernet-Frame ein
- Netzwerk Switch liest den Frame und leitet ihn gezielt weiter
b) Sender kennt nur IP-Adresse
- ARP (Address Resolution Protocol) wird verwendet
- Sender fragt: “Wer hat IP-Adresse X? Sag mir deine MAC-Adresse!”
- Das Gerät mit der IP Antwortet mit der MAC-Adresse → Sender speichert sie in seiner ARP-Tabelle

