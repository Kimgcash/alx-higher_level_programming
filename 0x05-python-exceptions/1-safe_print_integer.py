#!/usr/bin/python3
def safe_print_integer(value):
	"print an integer with "{:d}".format()"
	try:
		print("{:d}".format(value))
		return True
	except:
		return False
