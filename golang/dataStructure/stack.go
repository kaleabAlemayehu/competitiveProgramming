package datastructure

import "fmt"

type Stack struct {
	first *Node
	last  *Node
	size  int
}

func NewStack() *Stack {
	return &Stack{}
}

func (s *Stack) Push(value int) int {
	newNode := &Node{data: value}
	if s.size == 0 {
		s.first = newNode
		s.last = newNode
	} else {
		newNode.next = s.last
		s.last = newNode
	}
	s.size++
	return s.size
}

func (s *Stack) Pop() int {
	deletingNode := s.last
	if s.size == 0 {
		return -1
	} else {
		if s.first == s.last {
			s.last = nil
			s.size--
			return deletingNode.data
		}
		s.last = s.last.next
		deletingNode.next = nil
	}
	s.size--
	return deletingNode.data
}

func (s *Stack) Print() {

	for curr, i := s.last, 0; i < s.size; i++ {

		fmt.Printf("%v =>", curr.data)
		curr = curr.next
	}
	fmt.Println()
}
