import sys


def getBits(num):
	""" Returns: int, bitcount of num. """

	total = 0
	while(num):
		total += num & 0b1
		num = num >> 1

	return total


def main():
	""" Returns: None.  Counts bits in sys.argv[-1] """

	numInput = sys.argv[-1]

	try:
		bits = int(numInput)
	except ValueError:
		print >> sys.stderr, "Give me a number, please, not this: %s" % numInput

	bitTotal = getBits(bits)

	print "%d bits in %d"  % (bitTotal, bits)

if __name__ == '__main__':
	sys.exit(main())
