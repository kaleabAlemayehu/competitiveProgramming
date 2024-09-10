package main

import (
	"fmt"

	"github.com/kaleabAlemayehu/competitiveProgramming/sort"
)

func main() {
	// array := []int{1, 27, 2, 83, 293, 32, 328, 23, 232, 78293, 29}
	array := []int{10, 2, 3, 13, 7, 8, 9, 11, 12}
	// fmt.Print(*(sort.InsertionSort(array)))
	// arr1 := []int{4, 8, 3, 5, 12, 2, 23, 9, 10 , 6, 7}
	// arr2 := []int{2, 4, 6, 8, 10, 12}
	// fmt.Println(array)
	fmt.Println(sort.Pivot(array, 0, 4))
}
