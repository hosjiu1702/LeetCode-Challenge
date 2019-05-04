import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root_area = math.sqrt(area)
        # Square case
        if math.floor(root_area) == math.ceil(root_area):
            L = W = int(root_area)
            return [L, W]
        # Rectangular case
        else:
            root_area = int(math.floor(root_area))
            while(root_area > 0):
                temp = area % root_area
                if temp == 0:
                    a = int(area / root_area)
                    b = int(area / a)
                    if a >= b:
                        L = a
                        W = b
                    else:
                        L = b
                        W = a
                    return [L, W]
                root_area = root_area - 1
                                    