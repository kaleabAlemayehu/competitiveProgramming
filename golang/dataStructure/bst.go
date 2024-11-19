package datastructure

type BST struct {
	Root *Bstnode
}

func NewBST() *BST {
	return &BST{}
}

func (b *BST) Insert(value int) *BST {
	newNode := &Bstnode{Data: value}
	if b.Root == nil {
		b.Root = newNode
	} else {
		current := b.Root
		for {
			// ignore duplicate dataes
			if value == current.Data {
				return nil
			}
			if current.Data > value {
				if current.Left == nil {
					current.Left = newNode
					break
				}
				current = current.Left
			} else {
				if current.Right == nil {
					current.Right = newNode
					break
				}
				current = current.Right
			}
		}
	}
	return b
}
