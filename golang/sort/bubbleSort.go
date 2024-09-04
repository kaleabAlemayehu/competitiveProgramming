package sort

func BubbleSort(arr []int) *[]int {

	for i := len(arr) - 1; i > 0; i-- {
		noSwap := true

		for j := 0; j < i; j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				noSwap = false
			}
		}
		if noSwap {
			break
		}
	}

	return &arr
}
