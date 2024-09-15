package sort

import "github.com/kaleabAlemayehu/competitiveProgramming/sort/utilities"

func RadixSort(arr []int) []int {
	maxDigit := utilities.MostDigit(arr)
	for k := 0; k < maxDigit; k++ {
		array := make([][]int, 10)
		for i := 0; i < len(arr); i++ {
			array[utilities.GetDigit(arr[i], k)] = append(array[utilities.GetDigit(arr[i], k)], arr[i])
		}
		arr = []int{}
		for j := 0; j < 10; j++ {
			arr = append(arr, array[j]...)

		}
	}
	return arr
}
