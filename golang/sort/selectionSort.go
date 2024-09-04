package sort

func SelectionSort(arr []int) *[]int {
	for i := 0; i < len(arr)-1; i++ {
		min := i
		for j := i + 1; j < len(arr); j++ {
			if arr[min] > arr[j] {
				min = j
			}
		}
		if i != min {
			temp := arr[i]
			arr[i] = arr[min]
			arr[min] = temp
		}
	}
	return &arr
}
