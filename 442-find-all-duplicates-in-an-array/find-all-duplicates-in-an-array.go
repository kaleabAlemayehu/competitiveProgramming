func findDuplicates(nums []int) []int {
    // sort them with cyclic sort
    var i int
    for i < len(nums){
        correct:= nums[i] -1
        if nums[i] != nums[correct]{
            temp:= nums[i]
            nums[i] = nums[correct]
            nums[correct] = temp
        }else{
            i++
        }
    }
    var result []int

    for j:= 0; j < len(nums); j++{
        if j != (nums[j]-1){
            result = append(result, nums[j])
        }
    }
    return result
}