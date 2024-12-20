package main

import (
	"fmt"

	datastructure "github.com/kaleabAlemayehu/competitiveProgramming/dataStructure"
)

func main() {
	var heap []int = []int{}
	h := datastructure.InsertHeap(heap, 10)
	h = datastructure.InsertHeap(h, 20)
	h = datastructure.InsertHeap(h, 30)
	h = datastructure.InsertHeap(h, 300)
	h = datastructure.InsertHeap(h, 900)
	h = datastructure.InsertHeap(h, 90)
	h = datastructure.InsertHeap(h, 80)
	h = datastructure.InsertHeap(h, 70)
	h = datastructure.InsertHeap(h, 77)
	h = datastructure.InsertHeap(h, 7)
	h = datastructure.InsertHeap(h, 7000)
	max := datastructure.ExtractMax(h)
	fmt.Printf("Max: %d\n", max)
	for i, v := range h {
		fmt.Printf("index: %d, value: %d\n", i, v)
	}

}
