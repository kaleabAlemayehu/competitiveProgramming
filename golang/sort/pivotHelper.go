package sort

import "fmt"

func Pivot(arr []int, start int, end int) int {
	var (
		pivot = 0
	)
	for i := 0; i < len(arr); i++ {
		if arr[start] > arr[i] {
			pivot++
			temp := arr[i]
			arr[i] = arr[pivot]
			arr[pivot] = temp
		}
	}
	temp := arr[start]
	arr[start] = arr[pivot]
	arr[pivot] = temp
	fmt.Println(arr)
	return pivot
}
