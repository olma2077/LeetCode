/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    while (n !== 1) {
        let x = 0
        for (let c of String(n)) {
            x += (Number(c) ** 2)
        }
        if (x === 4) return false
        n = x
    }
    return true
}
