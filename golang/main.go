package main

import (
	"fmt"

	"github.com/kaleabAlemayehu/competitiveProgramming/sort"
)

func main() {
	array := []int{1, 27, 2, 83, 29, 293, 32, 328, 2, 23, 232, 78293, 29}
	fmt.Print(*(sort.BubbleSort(array)))
}
