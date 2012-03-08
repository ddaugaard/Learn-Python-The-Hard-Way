my_name = 'Daniel G. Daugaard'
my_age = 27 # close to 28 :(
my_height = 175 # cm.
my_weight = 67 # kilos
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Light Brown'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight) 



template = "If I add {age}, {height}, and {weight} I get {total}."
print template.format(
	age=my_age,
	height=my_height,
	weight=my_weight,
	total=my_age + my_height + my_weight
)   
    