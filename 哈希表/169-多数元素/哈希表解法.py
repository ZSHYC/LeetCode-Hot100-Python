class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. 准备一个哈希表 (字典)
        counts = {}
        
        # 2. 计算出“多数”的门槛 (向下取整)
        target = len(nums) // 2
        
        # 3. 遍历每个数字
        for num in nums:
            # 技巧：counts.get(num, 0) 
            # 意思是：尝试获取 num 的值，如果 num 不在字典里，就默认返回 0
            # dict.get(key, default)：如果 key 存在于字典中，则返回对应的值；如果 key 不存在，则返回 default 值
            counts[num] = counts.get(num, 0) + 1
            
            # 4. 剪枝：一旦发现当前数字超过一半，立刻返回
            # 这样不用等遍历完整个数组
            if counts[num] > target:
                return num
                
        return 0 # 理论上不会走到这，因为题目保证存在多数元素