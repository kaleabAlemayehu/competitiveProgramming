package sort

import "math"

func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := int(math.Floor(float64(len(arr) / 2)))
	left := MergeSort(arr[0:mid])
	right := MergeSort(arr[mid:])
	return *Merge(left, right)
}
