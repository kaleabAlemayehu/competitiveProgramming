package datastructure

import "fmt"

type treeNode struct {
	data  int
	next  *treeNode
	left  *treeNode
	right *treeNode
}

type treeQueue struct {
	first *treeNode
	last  *treeNode
	size  int
}

type tree struct {
	Root *treeNode
}

func NewTree() *tree {
	return &tree{}
}

func NewTreeQueue() *treeQueue {
	return &treeQueue{}
}

func (q *treeQueue) EnQueue(value treeNode) int {
	newNode := &value
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

func (q *treeQueue) DeQueue() *treeNode {
	removed := q.first
	if q.size == 1 {
		q.first = nil
		q.last = nil
	} else if q.size == 0 {
		return nil
	} else {
		q.first = q.first.next
		removed.next = nil
	}
	q.size--
	return removed
}

func Run() {
	mytree := NewTree()
	mytree.Root = &treeNode{data: 2}
	mytree.Root.left = &treeNode{data: 8}
	mytree.Root.right = &treeNode{data: 10}
	mytree.Root.right.left = &treeNode{data: 30}
	mytree.Root.left.left = &treeNode{data: 0}
	mytree.Root.left.right = &treeNode{data: 80}
	mytree.Root.right.right = &treeNode{data: 22}
	mytree.Root.right.left.right = &treeNode{data: 13}
	mytree.Root.left.left.left = &treeNode{data: 101}
	mytree.Root.left.right.right = &treeNode{data: 55}
	mytree.Root.right.right.left = &treeNode{data: 44}
	fmt.Println("bfs-value", mytree.bfs())
	/*
					   2
				      8        10
				   0   80   30      22
				101     55    13   44
		[2, 8, 10, 0, 80, 30, 22, 101, 55, 13, 44]
		[2, 8, 10, 0, 80, 30, 22, 101, 55, 13, 44]
	*/
}

func (q *tree) bfs() []int {
	nodes := []int{}
	queue := NewTreeQueue()
	queue.EnQueue(*q.Root)
	for queue.size != 0 {
		dnode := queue.DeQueue()
		nodes = append(nodes, dnode.data)
		if dnode.left != nil {
			queue.EnQueue(*dnode.left)
		}
		if dnode.right != nil {
			queue.EnQueue(*dnode.right)
		}
	}
	return nodes
}