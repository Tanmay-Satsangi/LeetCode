#Area of Rectangle = Length * Width

# https://www.youtube.com/watch?v=eR4-vf6m8H4

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaR1 = (ax2 - ax1) * (ay2 - ay1) # length * width
        areaR2 = (bx2 - bx1) * (by2 - by1) 

        #Find the co - ordinates of common area
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min (ax2, bx2)
        cy2 = min(ay2, by2)

        cl = cy2 - cy1
        cw = cx2 - cx1 # width of common rectangle
       

        #Find common area
        cArea = 0

        if ( cl > 0 and cw > 0):
            cArea = cl * cw

        return areaR1 + areaR2 - cArea

        

        