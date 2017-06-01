class reverse_bits:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #convert a 32 bit unsigned integer to its binary format and reverse it
        reversed_bits = int(bin(n)[2:].zfill(32)[::-1], 2)
        #return the integer of the reversed binary
        return reversed_bits
    
    def main():
        reversed_bits(32)
        reversed_bits(4)
        reversed_bits(287)
    
    main()
