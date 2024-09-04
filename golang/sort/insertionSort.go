package sort

import "fmt"

func InsertionSort(arr []int) *[]int {
	for i := 1; i < len(arr); i++ {
		var (
			currentValue = arr[i]
			j            = 0
		)
		for j = i - 1; arr[j] > currentValue && j >= 0; j-- {
			arr[j+1] = arr[j]
		}
		fmt.Println(arr)
		fmt.Printf("val %v\n", currentValue)
		arr[j+1] = currentValue
	}
	return &arr
}
