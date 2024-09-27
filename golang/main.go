package main

import (
	datastructure "github.com/kaleabAlemayehu/competitiveProgramming/dataStructure"
)

func main() {
	// arr := []int{5, 6, 9, 10, 202, 9, 8, 7, 4, 2, 3, 1}
	// fmt.Println(sort.CountSort(arr))
	sll := &datastructure.SinglyLinkedList{}
	sll.Push(10)
	sll.Push(12)
	sll.Push(232)
	sll.Push(1)
	sll.Push(122)
	// sll.Unshift(23)

	sll.Print()
	sll.Reverse()
	sll.Print()
	sll.Reverse()
	sll.Print()
	// // sll.Insert(3, 100)
	// sll.Remove(3)
	// // sll.Insert(3, 100)
	// sll.Remove(3)
	// sll.Print()
	// sll.Remove(0)
	// sll.Print()
	// // sll.Set()
	// fmt.Println("value:", sll.Get(1))
	// fmt.Println("shift", sll.Shift())
	// sll.Print()
	// fmt.Println("shift", sll.Shift())
	// sll.Print()
	// fmt.Println("shift", sll.Shift())
	// sll.Print()
	// fmt.Println("shift", sll.Shift())
	// sll.Print()

	// fmt.Println(sll.Pop())
	// sll.Print()
	// fmt.Println(sll.Pop())
	// sll.Print()
	// fmt.Println(sll.Pop())
	// sll.Print()
	// fmt.Println(sll.Pop())
	// sll.Print()
	// array := []int{1, 27, 2, 83, 293, 32, 328, 22328323, 232, 78293, 29}
	// array := []int{-2, 0, -100, 100, 10, 2, 3, 13, 7, 8, 9, 11, 12}
	// fmt.Print(*(sort.InsertionSort(array)))
	// arr1 := []int{4, 8, 3, 5, 12, 2, 23, 9, 10 , 6, 7}
	// arr2 := []int{2, 4, 6, 8, 10, 12}
	// fmt.Println(array)
	// fmt.Println(sort.QuickSort(array, 0, len(array)-1))
	// fmt.Println("pivoted", sort.Pivot(array, 3, len(array)-1))
	// fmt.Println(sort.MostDigit([]int{}))
	// fmt.Println(array)
	// fmt.Printf("sorted: %v\n", sort.RadixSort(array))
}
