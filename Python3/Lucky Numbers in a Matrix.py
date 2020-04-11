class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        nums = []
        for row in matrix:
            num = min(row)
            i = row.index(num)
            if num == max([line[i] for line in matrix]):
                nums.append(num)
        return nums
        
