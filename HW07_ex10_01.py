# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
# Imports
import types
# Global elements
elements = []

def nested_sum(list_):
	global elements
	for item in list_:
		if type(item) is types.ListType:
			sum_nest(item)
		elif type(item) is types.IntType:
			elements.append(item)

	return sum(elements)

def main():
	pass
	# print sum_nest([1,2,[3,4],[5,[1,2]]])

if __name__ == '__main__':
	main()