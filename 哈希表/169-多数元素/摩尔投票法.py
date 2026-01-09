class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 初始化两个核心变量
        candidate = None  # 当前霸主
        count = 0         # 霸主血量
        
        for num in nums:
            # 1. 如果当前血量为 0，说明之前的霸主死光了
            # 或者是刚开始，当前这个数直接上位
            if count == 0:
                candidate = num
            
            # 2. 判断是敌是友
            if num == candidate:
                # 友军：血量加一
                count += 1
            else:
                # 敌人：同归于尽 (血量减一)
                count -= 1
                
        # 题目保证多数元素一定存在，所以最后剩下的 candidate 一定是它
        return candidate