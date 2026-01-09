class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. 将数组转换为集合，实现 O(1) 的查找，并去重
        num_set = set(nums)
        longest_streak = 0
        
        # 2. 遍历集合中的每个数
        for num in num_set:
            # 3. 核心剪枝：只有当 num-1 不在集合中时，num 才是一个序列的起点
            # 如果 num-1 存在，说明 num 已经被包含在以 num-1 (或更小) 开头的序列里了
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 4. 从起点开始不断向后寻找连续的数字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # 5. 更新最大长度
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak