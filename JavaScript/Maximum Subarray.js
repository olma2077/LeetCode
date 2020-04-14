var maxSubArray = function(nums) {
        let a = 0    
        let max_ = nums[0]
        let local = nums[0]
        
        for (let i = 1;  i < nums.length; i++) {            
            if (local < 0 || local + nums[i] < 0) {
                local = nums[i]
            } else {
                local += nums[i]
            }
            if (local > max_) {
                max_ = local
            }
        }
        return max_
}
