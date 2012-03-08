
# Greeting function, it takes three arguments
# and creates a greeting from them and prints
# it.
def greet(greeting, person):
	message = '%s, %s' % (greeting, person)
	print message



# Ask the user about details for the greeting
greeting = raw_input('Greeting: ')
person = raw_input('Person: ')


# Use the user-provided greeting details
# and invoke our "greet" function with
# them.
greet(greeting, person)

