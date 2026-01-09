class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1. 初始化哈希表
        # Key: 前缀和, Value: 这个前缀和出现的次数
        # 必须预设 {0: 1}，用来处理“从头开始累加刚好等于k”的情况
        prefix_map = {0: 1}
        
        curr_sum = 0
        count = 0
        
        # 2. 遍历数组
        for num in nums:
            curr_sum += num  # 计算当前前缀和
            
            # 3. 核心公式：寻找满足 (curr_sum - old_sum = k) 的 old_sum
            target = curr_sum - k
            
            # 如果历史记录里有这个 target，说明中间有一段和为 k
            if target in prefix_map:
                count += prefix_map[target]
            
            # 4. 把当前的前缀和记录下来
            # 相当于在账本上写一笔：总金额 curr_sum 又出现了一次
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
            
        return count