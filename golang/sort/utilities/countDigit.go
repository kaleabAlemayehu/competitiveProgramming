package utilities

import "math"

func CountDigit(num int) (digit int) {
	if num == 0 {
		digit = 1
		return
	}
	digit = int(math.Ceil(math.Log10(float64(num))))
	return
}
