---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Schicht-7
  - OSI-Schicht-6
  - OSI-Schicht-5
aliases:
  - Domain Name System
  - DNS-Server
---
> **Telefonbuch** des Internets
> Statt sich [[IP|IP-Adressen]] wie `142.251.37.4` zu merken, nutzt man **Domainnamen** wie `www.google.com` 
> Der DNS-Dienst sorgt dafür, dass dieser Name in die passende [[IP|IP-Adresse]] übersetzt wird - und umgekehrt

## Funktion
1. Du gibst `www.example.com` im Browser ein
2. Dein Computer fragt den **lokalen DNS-Server** (meist beim Internetanbieter)
3. Wenn der Server die IP nicht kennt, **fragt er andere Server im Internet**:
	1. Root-Server (`.`) → sagt, wo die `.com`-Server sind
	2. Top-Level-Domain-Server (`.com`) → sagt, wo `www.example.com` verwaltet wird
	3. Authoritative DNS-Server für `example.com` → sagt: `www.example.com -> 23.215.0.138`
4. Sobald die [[IP|IP-Adresse]] gefunden wurde, bekommst du sie zurück.
5. Dein PC verbindet sich mit dem Server über die IP