#this formuala can be used to calculate the area of any triangle(need not to be specific eg. right angle triangle etc.)
x, y, z = map(float,input().split())  #Enter sides of triangle(x y z) in a row

s = (x + y + z) / 2   #s = semi perimeter

area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  #square of area of the triangle whose side is x, y and z respectively

print('The area of the triangle is %0.2f' %area)   #We have to take square root for final answer
