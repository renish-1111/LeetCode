class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        n = len(s)
        i,j=0,0
        feed = 0

        for j in range(0,n):
            if g[i]<=s[j]:
                feed+=1
                i+=1
                if i == len(g):
                    return feed
            

        return feed
