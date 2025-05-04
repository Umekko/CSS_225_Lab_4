"""
Calculating wait time 
===============================

Author: Chyngyz Mirzamatov
Created on: Sunday, May 5 2025
Last updated on: Sunday, May 5 2025

Program take as input current time and wait time, convert to integer, calculate final time after wait
"""


str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
