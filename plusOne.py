class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits) -1, -1,-1):
            if(digits[i] < 9):
                digits[i] += 1
                break

            elif(i != 0  and digits[i] == 9):
                digits[i] = 0

            elif( i == 0):
                if(i == 0 and digits[i] < 9):
                    digits[i] += 1
                    break

                if(i == 0):
                    digits[0] = 0
                    digits.insert(0,1)
                    break


        return(digits)
