class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s = str(n)
        lst = []
        for i in s:
            lst.append(int(i))
        j = 1
        pro = lst[0]
        while j < len(lst):
            pro *= lst[j]
            j += 1
        sum = lst[0]
        k = 1
        while k < len(lst):
            sum += lst[k]
            k += 1
        res = pro - sum
        return res
            

