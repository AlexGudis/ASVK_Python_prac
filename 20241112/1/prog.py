import collections

class DivStr(collections.UserString):
    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, by):
        ans = []
        i = 0
        part_len = len(self.data) // by
        while i + part_len <= len(self.data):
            ans.append(DivStr(self.data[i:i+part_len]))
            i += part_len
        return ans
        

    def __mod__(self, by):
        return DivStr(self.data[len(self.data) // by * by:])

import sys
exec(sys.stdin.read())