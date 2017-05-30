def multiply(x,y,z=1):
    product = float(x) * float(y) * float(z)
    return product

print
print "Part A: Three values"
print "3.124, 22.5, 6"
print multiply(3.124, 22.5, 6)

print
print "Part B: Three named arguments"
x = 3.124
y = 22.5
z= 6
print multiply(x,y,z)

print
print "Part C: A mix of three named and positional values"
print "z = 12"
print multiply(x,y,z=12)

print
print "Part D: Two arguments and use default z (1)"
print multiply(x,y)
