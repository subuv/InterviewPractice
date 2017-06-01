class hamming_distance(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #Compute the hamming distance between two numbers as xor of the binary values
        hd = bin(x^y).count('1')
        #return the hamming distance
        return hd
    
    def main():
        hammingDistance(4, 5)
        hammingDistance(106, 255)
        hammingDistance(32, 56)
        
    main()
