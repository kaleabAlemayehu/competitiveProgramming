package sort

func QuickSort(arr []int, left int, right int) []int {
	if left < right {
		pivot := Pivot(arr, left, right)
		// left
		QuickSort(arr, 0, pivot-1)
		// right
		QuickSort(arr, pivot+1, right)
	}
	return arr
}
