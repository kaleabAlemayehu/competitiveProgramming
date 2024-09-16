package datastructure

import "fmt"

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
	for node := l.head; node != nil; node = node.next {
		fmt.Print(node.data, ", ")
	}
	fmt.Println()
}
