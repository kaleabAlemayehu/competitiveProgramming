package datastructure

import (
	"fmt"
)

type DoublyLinkedList struct {
	head   *Node
	tail   *Node
	length int
}

func New() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (d *DoublyLinkedList) Push(value int) {
	var newNode *Node = &Node{data: value}
	if d.length == 0 {
		d.tail = newNode
		d.head = newNode
	} else {
		newNode.prev = d.tail
		d.tail.next = newNode
		d.tail = newNode
	}
	d.length++
}

func (d *DoublyLinkedList) PrintForward() {
	for cur := d.head; cur != nil; cur = cur.next {
		fmt.Printf("%v ->", cur.data)
	}
	fmt.Println()
}

func (d *DoublyLinkedList) PrintBackward() {
	for cur := d.tail; cur != nil; cur = cur.prev {
		fmt.Printf("%v ->", cur.data)
	}
	fmt.Println()
}
