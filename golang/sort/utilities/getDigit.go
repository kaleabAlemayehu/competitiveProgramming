package utilities

import "math"

func GetDigit(num int, index int) int {

	return int(math.Abs(float64(num))/math.Pow(10, float64(index))) % 10
}
