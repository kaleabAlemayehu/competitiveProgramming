package sort

// i guess this one work with frequency counter patter like merge & quick sort use devide and conquer pattern
// and it assume that all the number are positive number including zero
func CountSort(arr []int) []int {
	// find the largest number in the array.
	var large int
	for _, value := range arr {
		if large < value {
			large = value
		}
	}
	// create frequency array by the length of large + 1
	frequencyArray := make([]int, large+1)
	// populate the frequency array
	for _, value := range arr {
		frequencyArray[value]++
	}
	// create empty array to return
	var sortedArray []int
	// populate the array based on the frequency array
	for i := 0; i < len(frequencyArray); i++ {
		if frequencyArray[i] > 0 {
			sortedArray = append(sortedArray, i)
			frequencyArray[i]--
			i--
		}
	}

	return sortedArray
}
