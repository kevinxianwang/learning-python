class Rational:
	def add(self, other):
		pass

	def subtract(self, other):
		pass

	def multiply(self, other):
		pass

	def divide(self, other):
		pass


def main():
	a = Rational(2, 4)
	b = Rational(6, 9)
	print a.add(b)
	print a.subtract(b)
	print a.multiply(b)
	print a.divide(b)
	"""
	Should see the following printed out:
	> 5/6
	> -1/6
	> 1/3
	> 3/4
	"""

if __name__ == '__main__':
	main()