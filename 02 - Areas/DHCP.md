---
date: 2025-07-24T15:01
aliases:
tags:
  - Biologie
  - DHCP-Server
  - DHCPv6
  - Dynamic Host Configuration Protocol
  - Informatik
  - Internet
  - Linguistik
  - OSI-Schicht-5
  - OSI-Schicht-6
  - OSI-Schicht-7
  - Protocol
  - Rechnernetze
---

> **DHCP** ist ein Protokoll zur **automatischen Zuweisung von [[IP]]-Adressen und weiteren Netzwerkeinstellungen** (z.B. Gateway, [[DNS|DNS-Server]]) an Geräte im Netzwerk
> Wird in **[[IP#IPv4|IPv4]]-Netzwerken** und in fast jeden Heimnetz verwendet

## Funktion
1. Gerät startet, hat keine IP-Adresse
2. Sendet eine **DHCP Discover**-Nachricht (Broadcast)
3. DHCP-Server antwortet mit **DHCP Offer**
4. Gerät sendet **DHCP Request**, um Angebot anzunehmen
5. Server bestätigt mit **DHCP Acknowledgement**
→ Danach hat das Gerät eine IP-Adresse, Subnetzmaske, Gateway, DNS usw.

## DHCPv6

> Pendant zu DHCP für **[[IP#IPv6|IPv6]]**
> Funktioniert ähnlich, aber mit ein paar Unterschieden

### Varianten
| Modus     | Beschreibung                                                         |
| :-------- | :------------------------------------------------------------------- |
| Stateful  | DHCPv6 vergibt vollständige IPv6-Adressen (wie bei IPv4-DHCP)        |
| Stateless | Gerät erhält Adresse per **[[SLAAC]]**, aber z.B. DNS per DHCPv6 |
> Ob ein Gerät DHCPv6 oder SLAAC verwendet, entscheidet der **[[Router]]** über Flags im [[Router#Router Advertisement (RA)|Router-Advertisements (RA)]]:
> **”M-Flag” = Managed (nutze DHCPv6 für Adressvergabe)**
> **”O-Flag” = Other (nutze DHCPv6 nur für andere Infos, z.B. DNS**

