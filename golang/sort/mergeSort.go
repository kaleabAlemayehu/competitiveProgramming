package sort

import (
	"github.com/kaleabAlemayehu/competitiveProgramming/sort/utilities"
)

func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := int(float64(len(arr) / 2))
	left := MergeSort(arr[0:mid])
	right := MergeSort(arr[mid:])
	return *utilities.Merge(left, right)
}
