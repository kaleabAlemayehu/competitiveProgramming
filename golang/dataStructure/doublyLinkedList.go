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

func (d *DoublyLinkedList) Set(index, value int) bool {
	if index <= (d.length-1)/2 {
		for curr, i := d.head, 0; curr != nil; i++ {
			if index == i {
				curr.data = value
				return true
			}
			curr = curr.next
		}
	} else {
		for curr, i := d.tail, d.length-1; curr != nil; i-- {
			if index == i {
				curr.data = value
				return true
			}
			curr = curr.next
		}
	}
	return false
}

func (d *DoublyLinkedList) Insert(index, value int) bool {
	if index <= (d.length-1)/2 {
		for curr, i := d.head, 0; curr != nil; i++ {
			if index == i {
				newNode := &Node{data: value}
				if index != 0 {
					curr.prev.next = newNode
				} else {
					d.head = newNode
				}
				newNode.next = curr
				newNode.prev = curr.prev
				curr.prev = newNode
				d.length++
				return true
			}
			curr = curr.next
		}
	} else {
		for curr, i := d.tail, d.length-1; curr != nil; i-- {
			if index == i {
				newNode := &Node{data: value}
				curr.prev.next = newNode
				newNode.next = curr
				newNode.prev = curr.prev
				curr.prev = newNode
				d.length++
				return true
			}
			curr = curr.prev
		}
	}
	return false
}

func (d *DoublyLinkedList) Remove(index int) bool {
	if index <= (d.length-1)/2 {
		for curr, i := d.head, 0; curr != nil; i++ {
			if index == i {
				if index != 0 {
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					curr.next = nil
					curr.prev = nil
				} else {
					curr.next.prev = curr.prev
					d.head = curr.next
					curr.next = nil
					curr.prev = nil
				}
				d.length--
				return true
			}
			curr = curr.next
		}
	} else {
		for curr, i := d.tail, d.length-1; curr != nil; i-- {
			fmt.Println("current", curr.data)
			if index == i {
				if index != d.length-1 {
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					curr.next = nil
					curr.prev = nil
				} else {
					curr.prev.next = nil
					curr.prev = nil
					d.tail = curr.prev
				}
				d.length--
				return true
			}
			curr = curr.prev
		}
	}
	return false
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
