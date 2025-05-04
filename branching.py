# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

"""
Time traveler greeting
===============================

Author: Chyngyz Mirzamatov
Created on: Sunday, May 5 2025
Last updated on: Sunday, May 5 2025

This programm will greet with you depends what year you are giving as input
"""



# year == int.input("Greetings! What is your year of origin? ')) --> old version
                  
year = int(input("Greetings! What is your year of origin? "))

# if year <= 1900 --> old version
if year <= 1900:
    # print ('Woah, that's the past!') --> old version
    print ("Woah, that's the past!")
# elif year > 1900 && year < 2020: --> old version
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
# elif: --> old version
else:
    print ("Far out, that's the future!!")
