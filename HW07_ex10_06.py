# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
def is_sorted(list_):
	nlist = all([True if list_[i]<list_[i+1] else False for i in range(len(list_)-1)])
	return nlist

def main():
	pass
	# is_sorted([1,3,2])

if __name__ == '__main__':
	main()