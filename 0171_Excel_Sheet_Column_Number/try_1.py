class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
               "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, 
               "N":14, "O": 15, "P":16, "Q":17, "R":18, "S":19, 
               "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
        column_num = 0
        count = 0
        if len(s) is 1:
            column_num = dic[s]
            return column_num
        else:
            for i in range(len(s), 0, -1):
                if i is 1:
                    column_num = column_num + dic[s[count]]
                else:
                    column_num = 26**(len(s)-count-1)  * dic[s[count]] + column_num
                    count = count + 1
            return column_num