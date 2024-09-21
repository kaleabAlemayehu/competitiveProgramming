package datastructure

import (
	"fmt"
)

type SinglyLinkedList struct {
	head *Node
	tail *Node
}

func (l *SinglyLinkedList) Push(val int) {
	node := &Node{data: val}
	if l.head == nil {
		l.head = node
		l.tail = node
	} else {
		l.tail.next = node
		l.tail = node
	}
}

func (l *SinglyLinkedList) Print() {
	fmt.Print("the list is: ")
	for node := l.head; node != nil; node = node.next {
		fmt.Print(node.data, ", ")
	}
	fmt.Println()
}

func (l *SinglyLinkedList) Pop() int {
	if l.head == nil {
		return -1
	}
	current := l.head
	pre := &Node{}

	for current.next != nil {
		pre = current
		current = current.next
	}
	if l.tail == l.head {
		l.head = nil
		l.tail = nil
	}

	pre.next = nil
	l.tail = pre
	return current.data

}
