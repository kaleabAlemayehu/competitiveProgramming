package datastructure

import "fmt"

type Queue struct {
	first *Node
	last  *Node
	size  int
}

func NewQueue() *Queue {
	return &Queue{}
}

func (q *Queue) EnQueue(value int) int {
	newNode := &Node{data: value}
	if q.size == 0 {
		q.first = newNode
		q.last = newNode
	} else {
		q.last.next = newNode
		q.last = newNode
	}
	q.size++
	return q.size
}

func (q *Queue) DeQueue() int {
	removed := q.first
	if q.size == 1 {
		q.first = nil
		q.last = nil
	} else if q.size == 0 {
		return -1
	} else {
		q.first = q.first.next
		removed.next = nil
	}
	q.size--
	return removed.data
}

func (q *Queue) Print() {
	for curr := q.first; curr != nil; curr = curr.next {
		fmt.Printf("%v =>", curr.data)
	}
	fmt.Println()
}
