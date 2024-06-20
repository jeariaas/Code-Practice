def mySqrt(x):
        """
        :type x: int
        :rtype: int

        
        """
        left, right = 0, x
        curr = x//2
        while left <= right:
            curr = (left + right)/2
            if curr*curr == x:
                print(curr)
                return curr
            elif curr*curr < x:
                left = curr
            elif curr*curr > x:
                right = curr

mySqrt(8)