class Solution:
    def trap(self, h: List[int]) -> int:
        left,right = 0,len(h)-1
        water = 0
        max_left,max_right = 0,0

        while left<right:
            if h[left]<h[right]:
                if h[left]>=max_left:
                    max_left = h[left]
                else:
                    water += max_left - h[left]
                left += 1
            else:
                if h[right]>=max_right:
                    max_right = h[right]
                else:
                    water += max_right - h[right]
                right -= 1
            
        return water