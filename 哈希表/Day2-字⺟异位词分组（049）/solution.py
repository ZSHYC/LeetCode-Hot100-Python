from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 引入 defaultdict，它可以自动初始化不存在的 key，避免手动判断 if key in map
        from collections import defaultdict
        
        # 定义哈希表，默认的值是一个空列表 []
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. 制作“身份证”：将字符串排序
            # 注意：sorted(s) 返回的是列表 ['a','e','t']，无法作为字典的 key
            # 所以必须用 "".join() 把它转回字符串 "aet" (或者用 tuple)
            key = "".join(sorted(s))
            
            # 2. 归类：直接把原单词 s 追加到对应的 key 列表中
            anagram_map[key].append(s)
        
        # 3. 返回所有分组（只取字典的 value 部分）
        return list(anagram_map.values())