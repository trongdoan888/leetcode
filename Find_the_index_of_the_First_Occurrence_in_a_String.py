"""Cho hai chuỗi needlevà haystack, hãy trả về chỉ số của lần xuất hiện đầu tiên của needletrong haystack, hoặc trả về -1nếu needlekhông phải là một phần của haystack."""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)