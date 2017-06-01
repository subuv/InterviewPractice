class hamming_weight(object):
    #Compute the hamming weight of an integer
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Count the number of 1's in the binary format of the integer
        hw = bin(n).count("1")
        #return the hamming weight
        return hw
    
    def main():
        hammingWeight(21)
        hammingWeight(5)
        hammingWeight(344)
    
    main()
