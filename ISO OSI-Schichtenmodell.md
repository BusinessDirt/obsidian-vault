---
date: 2025-07-24T15:01
tags:
  - Informatik
  - Rechnernetze
  - Internet
---
<table class="wikitable" style="text-align:center">
	<tbody>
		<tr>
			<th colspan="2">OSI-Schicht</th>
			<th>Einordnung</th>
			<th><a href="/wiki/Internetprotokollfamilie#TCP/IP-Referenzmodell" title="Internetprotokollfamilie">TCP/IP-Referenzmodell</a></th>
			<th>Einordnung
			</th>
			<th>Protokollbeispiele
			</th>
			<th>Einheiten
			</th>
			<th>Kopplungselemente
			</th>
		</tr>
	<tr>
	<td class="hintergrundfarbe3">7
	</td>
	<td class="hintergrundfarbe3">Anwendung<br>(Application)
	</td>
	<td rowspan="3" class="hintergrundfarbe3">Anwendungs-<br>orientiert
	</td>
	<td rowspan="3" class="hintergrundfarbe8">Anwendung
	</td>
	<td rowspan="5" class="notheme hintergrundfarbe8">Ende zu<br>Ende<br>(<a href="/wiki/Direktverbindung" title="Direktverbindung">Multihop</a>)
	</td>
	<td rowspan="3"><a href="/wiki/Dynamic_Host_Configuration_Protocol" title="Dynamic Host Configuration Protocol">DHCP</a><br><a href="/wiki/Domain_Name_System" title="Domain Name System">DNS</a><br><a href="/wiki/File_Transfer_Protocol" title="File Transfer Protocol">FTP</a><br><a href="/wiki/Hypertext_Transfer_Protocol" title="Hypertext Transfer Protocol">HTTP</a><br><a href="/wiki/Hypertext_Transfer_Protocol_Secure" title="Hypertext Transfer Protocol Secure">HTTPS</a><br><a href="/wiki/Lightweight_Directory_Access_Protocol" title="Lightweight Directory Access Protocol">LDAP</a><br><a href="/wiki/MQTT" title="MQTT">MQTT</a><br><a href="/wiki/NetWare_Core_Protocol" title="NetWare Core Protocol">NCP</a><br><a href="/wiki/Real-Time_Transport_Protocol" title="Real-Time Transport Protocol">RTP</a><br><a href="/wiki/Simple_Mail_Transfer_Protocol" title="Simple Mail Transfer Protocol">SMTP</a><br><a href="/wiki/Extensible_Messaging_and_Presence_Protocol" title="Extensible Messaging and Presence Protocol">XMPP</a>
	</td>
	<td rowspan="3">Daten
	</td>
	<td rowspan="4" class="notheme hintergrundfarbe9"><a href="/wiki/Gateway_(Informatik)" title="Gateway (Informatik)">Gateway</a>, <a href="/wiki/Lastverteilung_(Informatik)" title="Lastverteilung (Informatik)">Content-Switch</a>, <a href="/wiki/Proxy_(Rechnernetz)" title="Proxy (Rechnernetz)">Proxy</a>, Layer-4-7-Switch
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">6
	</td>
	<td class="hintergrundfarbe3">Darstellung<br>(Presentation)
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">5
	</td>
	<td class="hintergrundfarbe3">Sitzung<br>(Session)
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">4
	</td>
	<td class="hintergrundfarbe3">Transport<br>(Transport)
	</td>
	<td rowspan="4" class="hintergrundfarbe3">Transport-<br>orientiert
	</td>
	<td class="hintergrundfarbe8">Transport
	</td>
	<td><a href="/wiki/Transmission_Control_Protocol" title="Transmission Control Protocol">TCP</a><br><a href="/wiki/User_Datagram_Protocol" title="User Datagram Protocol">UDP</a><br><a href="/wiki/Stream_Control_Transmission_Protocol" title="Stream Control Transmission Protocol">SCTP</a><br><a href="/wiki/Sequenced_Packet_Exchange" title="Sequenced Packet Exchange">SPX</a>
	</td>
	<td><a class="mw-selflink-fragment" href="#Schicht_4_–_Transportschicht">TCP = Segmente</a><br><a href="/wiki/Datagramm" title="Datagramm">UDP = Datagramme</a>
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">3
	</td>
	<td class="hintergrundfarbe3">Vermittlung-/Paket<br>(Network)
	</td>
	<td class="hintergrundfarbe8">Internet
	</td>
	<td><a href="/wiki/Internet_Control_Message_Protocol" title="Internet Control Message Protocol">ICMP</a><br><a href="/wiki/Internet_Group_Management_Protocol" title="Internet Group Management Protocol">IGMP</a><br><a href="/wiki/Internet_Protocol" title="Internet Protocol">IP</a><br><a href="/wiki/IPsec" title="IPsec">IPsec</a><br><a href="/wiki/Internetwork_Packet_Exchange" title="Internetwork Packet Exchange">IPX</a>
	</td>
	<td><a href="/wiki/Datenpaket" title="Datenpaket">Pakete</a>
	</td>
	<td class="notheme hintergrundfarbe9"><a href="/wiki/Router" title="Router">Router</a>, <a href="/wiki/Layer-3-Switch" title="Layer-3-Switch">Layer-3-Switch</a>
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">2
	</td>
	<td class="hintergrundfarbe3">Sicherung<br>(Data Link)
	</td>
	<td rowspan="2" class="hintergrundfarbe8">Netzzugriff
	</td>
	<td rowspan="2" class="notheme hintergrundfarbe8"><a href="/wiki/Direktverbindung" title="Direktverbindung">Punkt zu<br>Punkt</a>
	</td>
	<td>IEEE 802.3 <a href="/wiki/Ethernet" title="Ethernet">Ethernet</a><br><a href="/wiki/IEEE_802.11" title="IEEE 802.11">IEEE 802.11</a> WLAN<br><a href="/wiki/TokenTalk_Link_Access_Protocol" title="TokenTalk Link Access Protocol">TLAP</a><br><a href="/wiki/Fiber_Distributed_Data_Interface" title="Fiber Distributed Data Interface">FDDI</a><br><a href="/wiki/Media_Access_Control" title="Media Access Control">MAC</a><br><a href="/wiki/Token_Ring" title="Token Ring">Token Ring</a><br><a href="/wiki/ARCNET" title="ARCNET">ARCNET</a>
	</td>
	<td>Rahmen (<a href="/wiki/Datenframe" title="Datenframe">Frames</a>)
	</td>
	<td class="notheme hintergrundfarbe9"><a href="/wiki/Bridge_(Netzwerk)" title="Bridge (Netzwerk)">Bridge</a>, <a href="/wiki/Switch_(Netzwerktechnik)" title="Switch (Netzwerktechnik)">Layer-2-Switch</a>, <a href="/wiki/Wireless_Access_Point" title="Wireless Access Point">Wireless Access Point</a>
	</td></tr>
	<tr>
	<td class="hintergrundfarbe3">1
	</td>
	<td class="hintergrundfarbe3">Bitübertragung<br>(Physical)
	</td>
	<td><a href="/wiki/Ethernet#Gigabit-Ethernet" title="Ethernet">1000BASE-T</a><br><a href="/wiki/Token_Ring" title="Token Ring">Token Ring</a><br><a href="/wiki/ARCNET" title="ARCNET">ARCNET</a>
	</td>
	<td><a href="/wiki/Bit" title="Bit">Bits</a>, <a href="/wiki/Symbol_(Nachrichtentechnik)" title="Symbol (Nachrichtentechnik)">Symbole</a>
	</td>
	<td class="notheme hintergrundfarbe9"><a href="/wiki/Patchkabel" title="Patchkabel">Netzwerkkabel</a>, <a href="/wiki/Repeater" title="Repeater">Repeater</a>, <a href="/wiki/Hub_(Netzwerktechnik)" title="Hub (Netzwerktechnik)">Hub</a>, <a href="/wiki/Antenne" title="Antenne">Antenne</a>, <a href="/wiki/Wireless_Local_Area_Network" title="Wireless Local Area Network">Äther</a>
</td></tr></tbody></table>
