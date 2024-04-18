---
date: 2024-04-17T16:43
tags:
  - Informatik
  - Datenstruktur
cssclasses:
---
- Behälter für Daten
- Selbstreferenz für Vorgänger, Nachfolger, etc.
- Anwendung in [[Graph]], [[Baum]], [[Binärbaum]], [[Liste]]

## Knoten einer Liste
```java
public class Node<T> {
	
    private Node prev;
    private T data;
    private Node next;
	    
	public Node(T data) { this.data = data; }

	public Node getPrev() { return this.prev; }

	public Node getNext() {	return this.next; }

	public void setPrev(Node prev) { this.prev = prev; }

	public void setNext(Node next) { this.next = next; }

	public T getData() { return this.data; }
}
```
