package sort

func MostDigit(arr []int) (maxDigit int) {
	for i := 0; i < len(arr); i++ {
		if CountDigit(arr[i]) > maxDigit {
			maxDigit = CountDigit(arr[i])
		}
	}
	return
}
