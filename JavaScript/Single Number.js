var singleNumber = function(nums) {
    let res = new Set()
    for (let i of nums) {
        if (res.has(i)) res.delete(i)
        else res.add(i)
    }
    return [...res][0]
}
