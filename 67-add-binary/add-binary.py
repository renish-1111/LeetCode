class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n,m = len(a),len(b)
        result = ""

        if n>m:
            b = b.zfill(n)
        else:
            a = a.zfill(m)

        n = len(a)-1

        for i in range(0,n+1):
            bit = int(a[n-i]) + int(b[n-i]) + carry
            
            if bit == 3:
                carry = 1
                bit = 1
            elif bit == 2:
                carry = 1
                bit = 0
            elif bit == 1:
                carry = 0

            result = str(bit) + result
        
        if carry == 1:
            result ="1" + result

        return result
