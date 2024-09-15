package sort

import "github.com/kaleabAlemayehu/competitiveProgramming/sort/utilities"

func QuickSort(arr []int, left int, right int) []int {
	if left < right {
		pivot := utilities.Pivot(arr, left, right)
		// left
		QuickSort(arr, 0, pivot-1)
		// right
		QuickSort(arr, pivot+1, right)
	}
	return arr
}
