---
date: 2024-04-18T18:38
tags: []
---
Use yaml to structure the cards and then use a plugin to generate html elements with custom css classes.

Example:
```infocards
{
	"Strukturformel": {
		"img": "insert link here"
	},
	"Allgemeines": {
		"Name": "Isocyansäure",
		"Summenformel": "HNCO",
		"Kurzbeschreibung": "oberhalb von 0°C wenig beständige Flüssigkeit, die zur Polymerisation neigt."
	},
	"Externe Identifikatoren / Datenbanken": {
		"CAS-Nummer": "75-13-8"
	},
	"Eigenschaften": {
		"Molare Masse": "43,03 g*mol^-1",
		"Aggregatszustand": "flüssig",
		"Schmelzpunkt": "-86°C",
		"Siedepunkt": "23,5°C",
		"pK_s-Wert": "3,92"
	}
}
```

## Basic Features
- Headers will have an Object as type and the depth determines the heading level
- Paragraphs will have a String as type
- Images might also have a String as its type but will be detected by the String being a link

## Maybe Features
- Per Card css (would probably require each element to be an Object and therefore clutter up the file; could be an optional setting)