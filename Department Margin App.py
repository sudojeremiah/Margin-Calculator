# -*- coding: utf-8 -*-
import numpy as np

Dictionary = {"bake off":.4, "baked goods":.36, "prep foods":.50, 
              "specialty":.51, "coffee bar":.76, "sandwiches":.56, 
              "packaged":.42, "bulk":.49, "frozen":.33, "refrigerated":.31, 
              "beer":.26, "wine":.33, "produce":.38, "meat":.30, "supplements":.43, 
              "body care":.43, "mercantile":.45}

for key in Dictionary:
    print(key," - ", Dictionary[key])
    
Cost = float(input("Please enter cost: "))

Department = input("Please enter department name: ")

Price = Cost/(Dictionary[Department] -1)*-1

Price_round = np.round(Price,2)

print("Price at margin is:", Price_round)