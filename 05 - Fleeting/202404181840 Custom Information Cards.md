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

Headers will have an Object as type and Paragraphs a String