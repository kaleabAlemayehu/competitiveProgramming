package sort

// cyclic sort assumes that numbers should be conseqeutive for examle 1 to n , 0 to n, then it try to evaluate relation between the values and indexs

func CyclicSort(arr []int) []int {
	i := 0

	for i < len(arr) {
		// this current use to identify and set the relation between values and index values
		current := arr[i] - 1
		if arr[i] != arr[current] {
			// swap to set to the correct index
			temp := arr[i]
			arr[i] = arr[current]
			arr[current] = temp
		} else {
			i++
		}
	}

	return arr
}
