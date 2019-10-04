
import random
import csv


with open('words.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

print ('Here are 5 words')
print(random.sample(data,k=5))


  
