---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Schicht-4
aliases:
  - Transmission Control Protocol
---
## Eigenschaften
- **Verbindungsorientiert**: Es wird zuerst eine Verbindung zwischen Sender und Empfänger aufgebaut (Handshake)
- **Zuverlässig**: Pakete werden in der richtigen Reihenfolge und vollständig übergeben
- **Fehlererkennung & -korrektur**: Bestätigungen (ACKs) und Wiederholungen bei Paketverlust
- **Datenstrom-orientiert**: Die Daten werden als fortlaufender Strom von Bytes übertragen.

## Anwendungsbeispiele
- **Web** ([[HTTP|HTTP/HTTPS]])
- **E-Mail** ([[SMTP]], [[IMAP]], [[POP3]])
- **Dateiübertragung** ([[FTP]])

## Funktion
1. **Handshake**: Sender und Empfänger bauen eine Verbindung auf (3-Wege-Handshake)
2. **Datenübertragung**: Daten werden gesendet, Empfang wird bestätigt
3. **Verbindung beenden**: Beide Seiten schließen die Verbindung kontrolliert