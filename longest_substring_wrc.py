"""Cho một chuỗi ký tự s, hãy tìm độ dài của chuỗi dài nhất. chuỗi con không có ký tự trùng lặp."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s = s
        max_count_char = 0 

        for i, ch1 in enumerate(s):
            list_location = []
            list_location.append(ch1)

            for j in range(i + 1, len(s)):         
                if ch1 not in s[j]:
                    list_location.append(s[j])   
                else:
                    break

            if len(list_location) > max_count_char:
                max_count_char = len(list_location)
        
        return max_count_char 
                    
                    

if __name__ == "__main__":
    sol = Solution()

    str1 = "au"
    count_char = sol.lengthOfLongestSubstring(str1)
    print(count_char)
                
        
    