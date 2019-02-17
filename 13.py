
#Author: Konstantinos Gialantzis
#Last update: 17/02/2019

def mxDist(dist, num):
num = input()
    print type(num)
    while(isinstance(num, int) != True and num < 0):
        print("The number you typed wasn't an integer\nPlease enter a positive integer number:")
        num = input()
    print("Okey! Let's give the list of the distances you want:")
    dist = raw_input()
    distList = []
    distList.append(dist)
    #print dist
    #print distList


#i parousa askisi den einai oute kan misi!
