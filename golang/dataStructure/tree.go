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
	mytree.Inorder()

	/*
					       2
				          8        10
				        0   80   30      22
				   101        55    13 44
		[2, 8, 10, 0, 80, 30, 22, 101, 55, 13, 44]
		[2, 8, 10, 0, 80, 30, 22, 101, 55, 13, 44]
		preorder - 2 8 0 101 80 55 10 30 13 22 44
			       2 8 0 101 80 55 10 30 13 22 44
		postorder  101 0 55 80 8 13 30 44 22 10 2
				   101 0 8 80 55 2 30 13 10 44 22
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

func preorderHelper(node *treeNode, nodes *[]int) *[]int {
	currentNode := append(*nodes, node.data)
	if node.left != nil {
		currentNode = *(preorderHelper(node.left, &currentNode))
	}
	if node.right != nil {
		currentNode = *(preorderHelper(node.right, &currentNode))
	}
	return &currentNode
}

func (q *tree) Preorder() {
	current := q.Root
	nodes := []int{}
	fmt.Println("nodes", preorderHelper(current, &nodes))
}

func postorderHelper(node *treeNode, nodes *[]int) *[]int {
	currentNode := []int{}
	if node.left != nil {
		currentNode = append(currentNode, *(postorderHelper(node.left, &currentNode))...)
	}
	if node.right != nil {
		currentNode = append(currentNode, *(postorderHelper(node.right, &currentNode))...)
	}
	currentNode = append(currentNode, node.data)
	return &currentNode
}

func (q *tree) Postorder() {
	current := q.Root
	nodes := []int{}
	fmt.Println("nodes", postorderHelper(current, &nodes))
}

func inorderHelper(node *treeNode, nodes *[]int) *[]int {
	currentNode := []int{}
	if node.left != nil {
		currentNode = append(currentNode, *(inorderHelper(node.left, &currentNode))...)
	}
	currentNode = append(currentNode, node.data)
	if node.right != nil {
		currentNode = append(currentNode, *(inorderHelper(node.right, &currentNode))...)
	}
	return &currentNode
}

func (q *tree) Inorder() {
	current := q.Root
	nodes := []int{}
	fmt.Println("nodes", inorderHelper(current, &nodes))
}
