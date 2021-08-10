# ## ----變量字典---- ##
# from typing import List
import math


FData={
    "posX": 0,"posY": 0,"nowRGB": (0, 0 ,0 ),
    "fromX": 0,"fromY": 0,"toX": 0,"toY": 0,

    "LDplayer": (-16, -16),"FBtn": (286, 184),"Auto": (290,150),
    
    "Loading": (160,122),"LoadingRadius": 8,"LoadingPPN":12,

    "barStart": (90,70),"barEnd": (250,70),
    "barPPN": 5, #PickPointNumber#
    "barBlueOn": (0,162,255),"barGreenOn": (107,243,173),"barRadOn": 0,
    "barBlueOff": (0,81,123),"barGreenOff": (49,127,82),"barRadOff": (82,16,0)
      }

barPointList = [(1,2),(3,4),(5,6)]
my_new_barPointList = [barPointList[i]*5 for i in barPointList]

sinMathList = [0.00, 0.31, 0.59, 0.81, 0.95, 1.00, 0.95, 0.81, 0.59, 0.31, 0.00, -0.31, -0.59, -0.81, -0.95, -1.00, -0.95, -0.81, -0.59, -0.31]
cosMathList = [1.00, 0.95, 0.81, 0.59, 0.31, 0.00, -0.31, -0.59, -0.81, -0.95, -1.00, -0.95, -0.81, -0.59, -0.31, 0.00, 0.31, 0.59, 0.81, 0.95]

loadingChickPos = [for i in sinMathList:]


print(my_new_barPointList)

import math
a = math.cos(math.pi)    #求cos(180°)
b = math.sin(math.pi/2)  #求sin(90°）
print(a,b)

c= math.radians(180)
d= math.degrees(math.pi)
print(c,d)

e = math.sin(math.radians(360/FData["LoadingPPN"]))
print(round(e))

"""
输出：
-1.0  1.0  
"""


# # def pickPos(x,n):
# #     mylist = x
# #     i=0
# #     while i>=n :
# #         a = mylist[i]
# #         i = i+1
# #     return a

# # def pickPos(x, n):
# #     for i in x:
# #         if i == n:
# #             break
# #     print(i)
# #     return i

# # print(pickPos(FData["RGBLoad"],0))

# print(FData["RGBLoad"])
# a = FData["RGBLoad"]
# print(a[1])

# List = ['a','b','c','d','e','f','g','h']


# for i in List:
#     if i == 2:
#         break
# print(i)

# i = 1
# while i <= 2:
#     print(List, end=" ")
#     i = i + 1


# print("\n\n")
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j == 9:
#             print(i*j,"\t",) # j == 9時，換行
#         else:
#             print(i*j, "\t", end = '') # j < 9時，不換行