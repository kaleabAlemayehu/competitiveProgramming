package sort

func Pivot(arr []int, start int, end int) int {
	var (
		pivot = start
	)
	for i := start; i < len(arr); i++ {
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
	return pivot
}
