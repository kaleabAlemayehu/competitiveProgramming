package sort

import "math"

func CountDigit(num int) (digit int) {
	if num == 0 {
		return 1
	}
	return int(math.Ceil(math.Log10(float64(num))))
}
