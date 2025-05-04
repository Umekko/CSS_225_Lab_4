"""
Calculating wait time 
===============================

Author: Chyngyz Mirzamatov
Created on: Sunday, May 5 2025
Last updated on: Sunday, May 5 2025

Program take as input current time and wait time, convert to integer, calculate final time after wait
"""


currentTimeStr = input("What is the current time (in hours 0-23)? ")

waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)

waitTimeInt = int(waitTimeStr)


finalTimeInt = currentTimeInt + waitTimeInt

print(finalTimeInt)
