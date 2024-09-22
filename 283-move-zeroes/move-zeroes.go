func moveZeroes(nums []int)  {
    var (left = 0; right= 1)
    // iterate with right and check if left value is zero, if then , swap but not increment left if left is zero to not left zeroes behind
    for right < len(nums){
        if nums[left] == 0 && nums[right] != 0{
            temp:= nums[left]
            nums[left] = nums[right]
            nums[right] = temp
        }
        if nums[left] != 0 {
        left++
        }
        right++
    }

}
