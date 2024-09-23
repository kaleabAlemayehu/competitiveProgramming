func sortArray(nums []int) []int {
    if len(nums) <= 1 {
		return nums
	}
    mid:= int(len(nums)/2)
    left:= sortArray(nums[0:mid])
    right:= sortArray(nums[mid:])
    return merge(left, right)
}


func merge(leftArray []int, rightArray[]int) []int{
    i:=0
    j:=0
    var arr []int

    for i < len(leftArray) && j < len(rightArray){
        if leftArray[i] < rightArray[j] {
            arr = append(arr, leftArray[i])
            i++
        }else{
            arr = append(arr, rightArray[j])
            j++
        }
    }

    if !(i < len(leftArray)) && j < len(rightArray){
        arr = append(arr, rightArray[j:]...)
    }
    if !(j< len(rightArray)) && i < len(leftArray){
        arr = append(arr, leftArray[i:]...)
    }
    return arr
}