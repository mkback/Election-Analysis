# Election Analysis

##Overview of Project
###Seth and Tom have data on a congressional election in Colorado. We have been tasked to summarize and give the results of this election. We do this by using Python.  

## Election Results 

#####Here are the results we found: 
* 369,711 votes were cast in this congressional election
	* Jefferson county votes: 38,555 votes at 10.5% of the total votes
	* Denver county votes: 306,055 votes at 82.8% of the total votes 
	* Arapahoe county votes: 24,801 votes at 6.7% of the total votes
* Denver had the largest number of votes
* Three candidates: 
	* Charles Casper Stockham received 85,213 votes which was 23%
	* Diana DeGette received 272,892 votes which was 73.8%
	* Raymon Anthony Doane received 11,606 votes which was 3.1%
* Diana DeGette won the election with 272,892 votes and 73.8% of the total votes


##Election Summary 

#####The Python script used in this project can be modified and used for any future elections. This can be done with a few modifications. The first would be updating the data file. This script currently looks to “election_results.csv” so we would update this file path to be that of another election. The second modification is ensuring we pull in the correct candidate and county from the csv. In this example, county was the second row and candidates were the third row, so in the Python script we pulled from these rows. If future elections have more rows of information, we would need to modify so it pulls the correct ones.  