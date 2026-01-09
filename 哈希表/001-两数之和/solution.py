from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 创建一个哈希表（字典）
        # 用于存储已经遍历过的数字及其下标
        # 格式: { 数字值: 下标 }
        prev_map = {} 
        
        # 2. 遍历数组
        # 使用 enumerate 同时拿到 下标(i) 和 数字(num)
        # 这是 Python 最优雅的遍历方式
        for i, num in enumerate(nums):
            
            # 3. 计算我们需要找的“另一半”
            diff = target - num
            
            # 4. 关键点：回头看
            # 检查“另一半”是不是已经在我们的哈希表里了
            if diff in prev_map:
                # 5. 如果在，说明之前见过它，直接返回结果
                # prev_map[diff] 是之前那个数的下标
                # i 是当前数的下标
                return [prev_map[diff], i]
            
            # 6. 如果没找到，就把当前这个数存进去，等待后面的人来找它
            prev_map[num] = i
            
        # 题目保证一定有解，所以这里不需要写 return