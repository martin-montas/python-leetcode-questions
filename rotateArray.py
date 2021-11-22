class Solution:
    def rotate(self, arr: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #   the algorithm will try to print the current to the next
        #   and the enext to the current k times for moving the numbers
        #   of the array to its currect position
        curr = arr[0]
        for iters in range(0,k):        #   will do this k times
            i = 0
            curr = arr[0]
            while i < len(arr) :
                if i == len(arr) -1:    #   if the index is at the last step and it needs to be to 0

                    _temp = arr[0]

                    arr[0]= curr
                    curr = _temp

                    i +=  1
                elif i != len(arr) - 1:

                    _temp  =  arr[i +1]
                    arr[i +1] = curr

                    curr = _temp
                    i =  1
            del curr
        return (arr)


