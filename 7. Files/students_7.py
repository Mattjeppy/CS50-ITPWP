import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("CS50 ITPWP/7. Files/csv files/students_2.csv", "a") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow([name, home])