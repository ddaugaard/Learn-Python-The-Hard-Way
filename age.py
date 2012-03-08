daniels_age = 27
jakubs_age = 29
claudias_age = 24


def calculate(age):
	# Return age in days
	return age * 365

diff = calculate(jakubs_age) - calculate(claudias_age)
print "Jakub is older by", diff, "days than Claudia."