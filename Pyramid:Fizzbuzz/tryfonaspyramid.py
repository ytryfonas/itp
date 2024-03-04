stack = int(input("stack: "))
x = 9                             
y = 1
z = '#'
l = ' '
if 0 < stack <= 8:
    for i in range(stack):
        print(x * l,y * z, )
        y += 1
        x -= 1
else:
    print('stack has to be between 1 and 8.')

