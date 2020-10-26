class CartesianSet:
    def __init__(self, x, y):
            self.x = x
            self.y = y

#print "Enter number of points you want: \n"
#number_of_points = input()
list = []
#for i in range(0, number_of_points):
#    print "\nEnter x coordinate: \n"
#    x = input()
#    print "\nEnter y coordinate: \n"
#    y = input()
#
#    cartesian_set = CartesianSet(x, y)
#    list.append(cartesian_set)

for i in range(0, 4):
    for j in range(0, 3):
        cartesian_set = CartesianSet(i, j)
        list.append(cartesian_set)



for i in list:
    print ("x: " + str(i.x) + " y: " + str(i.y) + "\n")

count = 0
answer = 0

for point in list:

    for point2 in list:

        if point.x == point2.x and point.y < point2.y:
            answer+=count
            count+=1
print "\n" + str(count)



