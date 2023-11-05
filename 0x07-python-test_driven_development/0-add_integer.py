#!/usr/bin/python3
""" Function to add two integers """

def add_integer(a, b=98):
	"""Add two integers

	Args:
		a (_type_): _description_
		b (int, optional): _description_. Defaults to 98.

	Returns:
		integer: Addition
	"""
	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))
