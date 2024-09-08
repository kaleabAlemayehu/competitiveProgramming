package main

import (
	"fmt"

	"github.com/kaleabAlemayehu/competitiveProgramming/sort"
)

func main() {
	array := []int{1, 27, 2, 83, 293, 32, 328, 23, 232, 78293, 29}
	// array := []int{8, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	// fmt.Print(*(sort.InsertionSort(array)))
	// arr1 := []int{1, 3, 5, 6, 7}
	// arr2 := []int{2, 4, 6, 8, 10, 12}
	fmt.Println(array)
	fmt.Println(sort.MergeSort(array))
}
