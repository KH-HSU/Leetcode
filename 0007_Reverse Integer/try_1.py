class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x > 0:
            reverse_answer = self.parse(x)
            if reverse_answer > 2**31-1:
                reverse_answer = 0
            return reverse_answer
        if x < 0:
            x = x * (-1) 
            reverse_answer = self.parse(x)
            reverse_answer = reverse_answer * (-1)
            if reverse_answer < -1*(2**31):
                reverse_answer = 0
            return reverse_answer
        
    def parse(self, y):
        y_list = []
        temp = 0
        reverse_sum = 0
        while y != 0:
            y_list.append(y%(10**1))
            y = y // 10
        for i in range(len(y_list)):
            temp = y_list.pop()*10**(i)
            reverse_sum = temp + reverse_sum
        return reverse_sum