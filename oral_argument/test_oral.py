import os
import csv
import random

# path = "/Users/Nicole/Documents/oTree/oral_argument/static/oral_argument"
# collection = os.listdir(path)
# print(collection)
#
#
# with open('female.csv', 'w') as csvfile:
#     file = csv.writer(csvfile)
#     file.writerow(collection)
#


mylist = [1, 2, 3, 4, 5, 6, 7]
mylist2 = random.sample(mylist, 3)
print(mylist2)