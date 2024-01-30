class Solution(object):
    def complexNumberMultiply(self, n1, n2):
        a1,b1=n1.split('+')
        a1=int(a1)
        b1=int(b1[:-1])
        a2,b2=n2.split('+')
        a2=int(a2)
        b2=int(b2[:-1])
        return str(a1*a2-b1*b2)+'+'+str(a1*b2+a2*b1)+'i'