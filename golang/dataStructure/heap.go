package datastructure

import (
	"fmt"
)

func InsertHeap(h []int, v int) []int {
	if len(h) != 0 {
		th := append((h), v)
		h = th
		current := len(th) - 1
		var parent int = (current - 1) / 2
		if parent > -1 {
			for th[parent] < th[current] {
				th[parent], th[current] = th[current], th[parent]
				current = parent
				parent = (current - 1) / 2
			}
		}
	} else {
		th := append(h, v)
		h = th
		fmt.Println(h)
	}
	return h
}

func ExtractMax(h []int) int {
	removed := (h)[0]
	(h)[0], (h)[len(h)-1] = (h)[len(h)-1], (h)[0]
	h = h[:len(h)-2]
	current := 0
	left := current*2 + 1
	right := current*2 + 2
	for left < len(h) {
		if (h)[left] > (h)[right] && (h)[left] > (h)[current] {

		}

	}
	return removed
}
