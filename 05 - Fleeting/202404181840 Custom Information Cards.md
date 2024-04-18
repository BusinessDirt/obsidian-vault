---
date: 2024-04-18T18:38
tags: []
---
Use yaml to structure the cards and then use a plugin to generate html elements with custom css classes.

Example:
```inforcards
h1:
	bla
```

## Basic Features
- Headers will have an Object as type and the depth determines the heading level
- Paragraphs will have a String as type
- Images might also have a String as its type but will be detected by the String being a link

## Maybe Features
- Per Card css (would probably require each element to be an Object and therefore clutter up the file; could be an optional setting)