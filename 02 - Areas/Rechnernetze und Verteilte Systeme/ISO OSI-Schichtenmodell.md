---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
  - OSI-Modell
---
| OSI-Schicht | Bezeichnung (Deutsch / Englisch) | OSI-Einordnung        | TCP/IP-Schicht | Protokollbeispiele                                                       | Einheiten                        |
| ----------- | -------------------------------- | --------------------- | -------------- | ------------------------------------------------------------------------ | -------------------------------- |
| 7           | Anwendung (Application)          | Anwendungs-orientiert | Anwendung      | DHCP, DNS, [[HTTP]], [[HTTP#HTTPS\|HTTPS]], [[SMTP]], [[POP3]], [[IMAP]] | Daten                            |
| 6           | Darstellung (Presentation)       | Anwendungs-orientiert | Anwendung      | DHCP, DNS, [[HTTP]], [[HTTP#HTTPS\|HTTPS]], [[SMTP]], [[POP3]]           | Daten                            |
| 5           | Sitzung (Session)                | Anwendungs-orientiert | Anwendung      | DHCP, DNS, [[HTTP]], [[HTTP#HTTPS\|HTTPS]], [[SMTP]], [[POP3]]           | Daten                            |
| 4           | Transport (Transport)            | Transport-orientiert  | Transport      | [[TCP]], [[UDP]]                                                         | TCP = Segmente, UDP = Datagramme |
| 3           | Vermittlung / Paket (Network)    | Transport-orientiert  | Internet       | [[IP]]                                                                   | Pakete                           |
| 2           | Sicherung (Data Link)            | Transport-orientiert  | Netzzugriff    | Ethernet, WLAN , [[MAC]], Token Ring, ARCNET                             | Rahmen (Frames)                  |
| 1           | Bitübertragung (Physical)        | Transport-orientiert  | Netzzugriff    | 1000BASE-T, Token Ring, ARCNET                                           | Bits, Symbole                    |

