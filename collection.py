# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

"""
Authors and their death dates
===============================

Author: Chyngyz Mirzamatov
Created on: Sunday, May 5 2025
Last updated on: Sunday, May 5 2025

This programm shows authors and their death year
"""



authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889,
}

for author, date in authors.items():
    print(f"{author} died in {date}")


"""
    Problems was with naming of variable
    Also incorrect naming in FOR function
    Incorrect formatin in print() function
"""
