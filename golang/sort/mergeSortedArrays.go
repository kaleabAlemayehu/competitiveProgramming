package sort

func Merge(arr1 []int, arr2 []int) *[]int {
	var (
		i   int = 0
		j   int = 0
		arr []int
	)
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] <= arr2[j] {
			arr = append(arr, arr1[i])
			i++
		} else {
			arr = append(arr, arr2[j])
			j++
		}
	}
	if !(i < len(arr1)) && (j < len(arr2)) {
		arr = append(arr, arr2[j:]...)
	}
	if !(j < len(arr2)) && (i < len(arr1)) {
		arr = append(arr, arr1[i:]...)
	}

	return &arr
}
