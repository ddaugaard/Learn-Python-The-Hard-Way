formatter = "%r %r %r"
formatter = "%r %r %r %r"

print formatter % (1, 2, 3)
print formatter % ("one", "two", "three")
print formatter % (True, False, False)
print formatter % (formatter, formatter, formatter)
print formatter1 % ("I had this thing.",
				   "That you could type up right.",
				   "But it didn't sing. So I said goodnight.",
                   "Test"
)