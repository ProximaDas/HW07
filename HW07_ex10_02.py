# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
# Imports
import types
# Global elements
# elements = []

def capitalize_nested(list_):
	# global elements
	for idx in range(len(list_)):
		if type(list_[idx]) is types.ListType:
			capitalize_nested(list_[idx])
		elif type(list_[idx]) is types.StringType:
			list_[idx] = list_[idx].upper()
	
	return list_

def main():
	pass
	# print capitalize_nested(["apple",["bear","orange"],["name",["bob","harry"]]])
	# print capitalize_nested(["apple",["bear","orange"],["name",["bob","harry",["banana","pear"]]]])
	# print capitalize_nested(["apple",["bear","orange"],["name",["bob","harry",["banana","pear"],["imo","etc",["any","more"]]]]])

if __name__ == '__main__':
	main()