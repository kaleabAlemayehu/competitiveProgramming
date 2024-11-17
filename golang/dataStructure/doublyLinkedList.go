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

func (d *DoublyLinkedList) Pop() int {
	var val int = d.tail.data
	if d.length == 0 {
		return -1
	}
	if d.length != 0 && d.length != 1 {
		d.tail = d.tail.prev
		d.tail.next.prev = nil
		d.tail.next = nil
		d.length--
	}
	if d.length == 1 {
		d.head = nil
		d.tail = nil
		d.length--
	}
	return val
}

func (d *DoublyLinkedList) Shift() int {
	var val int = d.head.data
	if d.length == 0 {
		return -1
	}
	if d.length != 0 && d.length != 1 {
		d.head = d.head.next
		d.head.prev.next = nil
		d.head.prev = nil
		d.length--
	}
	if d.length == 1 {
		d.head = nil
		d.tail = nil
		d.length--
	}
	return val
}

func (d *DoublyLinkedList) Unshift(value int) {
	newNode := &Node{data: value}
	if d.length == 0 {
		d.head = newNode
		d.tail = newNode
	} else {
		d.head.prev = newNode
		newNode.next = d.head
		d.head = newNode
		d.length++
	}
}

func (d *DoublyLinkedList) Get(value int) int {
	if value <= (d.length-1)/2 {
		for curr, i := d.head, 0; curr != nil; i++ {
			if value == i {
				return curr.data
			}
			curr = curr.next
		}
	} else {
		for curr, i := d.tail, d.length-1; curr != nil; i-- {
			if value == i {
				return curr.data
			}
			curr = curr.prev
		}
	}
	return -1
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
