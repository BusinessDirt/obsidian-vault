---
date: 2024-04-18T18:38
tags: []
---
Use json to structure the cards and then use a plugin to generate html elements with custom css classes.

Example:
```json
{
	"h1": {
		"p": "bla",
		"h2": {
			"p": "bla 2"
		}
	}
}
```

## Basic Features
- Headers will have an Object as type and the depth determines the heading level
- Paragraphs will have a String as type
- Images might also have a String as its type but will be detected by the String being a link

## Maybe Features
- Per Card css (would probably require each element to be an Object and therefore clutter up the file; could be an optional setting)