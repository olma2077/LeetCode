/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let zero = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            nums[zero] = nums[i]
            zero += 1
        }
    }
    for (; zero < nums.length; zero++) {
        nums[zero] = 0
    }
}
