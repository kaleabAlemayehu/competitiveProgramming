package datastructure

import (
	"fmt"
)

type SinglyLinkedList struct {
	head   *Node
	tail   *Node
	length int
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
	l.length++
}

func (l *SinglyLinkedList) Print() {
	fmt.Print("the list is: ")
	for node := l.head; node != nil; node = node.next {
		fmt.Print(node.data, ", ")
	}
	fmt.Println()
	fmt.Println("length: ", l.length)
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
	l.length--
	return current.data

}

func (l *SinglyLinkedList) Shift() int {
	if l.head == nil {
		return -1
	}
	val := l.head.data
	l.head = l.head.next
	if l.head == nil {
		l.tail = nil
	}
	l.length--
	return val
}

func (l *SinglyLinkedList) Unshift(val int) {
	node := &Node{data: val}
	node.next = l.head
	l.head = node
	if l.tail == nil {
		l.tail = node
	}
	l.length++
}

func (l *SinglyLinkedList) Get(index int) *Node {
	if index >= l.length || index < 0 {
		return nil
	}
	i := 0
	node := l.head
	for i != index {
		node = node.next
		i++
	}
	return node
}
func (l *SinglyLinkedList) Insert(index int, value int) bool {
	if index > l.length || index < 0 {
		return false
	}
	if index == l.length {
		l.Push(value)
		return true
	}
	if index == 0 {
		l.Unshift(value)
		return true
	}
	node := l.Get(index - 1)
	newNode := &Node{data: value}
	newNode.next = node.next
	node.next = newNode
	l.length++
	return true

}

func (l *SinglyLinkedList) Set(index int, value int) bool {
	node := l.Get(index)
	if node != nil {
		node.data = value
		return true
	}
	return false
}

func (l *SinglyLinkedList) Remove(index int) bool {
	if index >= l.length || index < 0 {
		return false
	}
	if index == 0 {
		l.Shift()
		return true
	}
	if index == l.length-1 {
		l.Pop()
		return true
	}
	prev := l.Get(index - 1)
	prev.next = prev.next.next
	l.length--
	return true
}
