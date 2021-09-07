print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print("\n")
#test If statements
if counties[1] == "Denver":
    print(counties[1])
if counties[2] != "Jefferson":
    print(counties[2])
print("\n")
#Test operators 
if "El Paso" in counties:
    print("El Paso is in the list")
else: 
    print("El Paso is not in the list")
print("\n")
#Test for loops
for county in counties:
    print(county)
print("\n")
print("Test Loop with Index")
#test for loop with range 
for i in range(len(counties)):
    print(counties[i])
print("\n")
print("Test Loop with TUPLE")
counties_tuple = ("Arapahoe", "Denver", "Jeffereson")
#test for loop with range 
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
print("\n")
print("Dictionary & Keys")
#keys of dict
counties_dict = {"Arapahoe": 422829, "Denver": 463343, "Jefferson": 432438}
for county in counties_dict:
    print(county)
print("\n")
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
print("\n")
for county, voters in counties_dict.items():
    print(county, voters)
for county, voters in counties_dict.items():
    print(str(county) + " has " +str(voters) + " voters")
print("\n")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("\n")
#assign a vairable for the file to load and the path 
file_to_load = 'Resources/election_results.csv'
#open the election results and read the file
election_data = open(file_to_load, 'r')
#Do analysis

#close the file 
election_data.close()

#Open election results and read file 
with open(file_to_load) as election_data:
    #here is where the rest of analysis is 
    print(election_data)
print("\n")
print("os.path.join")
import csv
import os
# Assing a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Create the file name to save results in 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file 
with open(file_to_load) as election_data:
    #To do: read and analyze the data here 
    #Read the file object with the reader function 
    file_reader = csv.reader(election_data)
    #Print just header row in the CSV file 
    headers = next(file_reader)
    print(headers)



    print(election_data)
print("\n")

#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #Add to file
    txt_file.write("Counties in the Election \n")
    txt_file.write("-------------------------- \n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

