def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)

        def recurse(index):
            #need a base case
            if digits[index] + 1 != 10: #if the digit[index] + 1 != 10
                digits[index] +=1
                return
            
            if index > 0: #if the digit before exists and digit[index] + 1 == 10
                digits[index] = 0
                recurse(index-1)
            else:
                digits[0] = 1
                digits.append(0)
                return
                
        
        recurse(length-1)

        print(digits)

plusOne([9,9,9])