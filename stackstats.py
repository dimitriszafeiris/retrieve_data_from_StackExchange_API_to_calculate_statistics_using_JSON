#Author: Dimitris Zafeiris
#Date: 04/11/2017
#Version: 1.0

#Import requets library, to retrieve stack exchange data in json format
import requests

#Import json library to create the output in json format
import json

#Import heapq library to find top 10 elements of json objects
import heapq

print ("Welcome to Stackstats application")
since = input("Please provide date/time range for since (YYYY-MM-DD HH:MM:SS):")
until = input("Please provide date/time range for until (YYYY-MM-DD HH:MM:SS):")

#Retrieve answers from stackexchange, giving as input date/time that user provided before
answers = requests.get('https://api.stackexchange.com/docs/answers',fromdate=since,todate=until).json()

#Retrieve comments from stackexchange, for the same time period provided by user
comments = requests.get('https://api.stackexchange.com/docs/comments-on-answers',fromdate=since,todate=until).json()

#Initialize variables
accepted_counter = 0
all_counter = 0
total_accepted_score = 0
total_reputation = 0

#Iterate through answers json object to calculate count of accepted answers and average of these ones
for i in answers:
    # now song is a dictionary
    if (answers[i]["is_accepted"] == 'true'):
		accepted_counter++
		#Add to average only if this is an accepted answer
		total_accepted_score = total_accepted_score + answers[i]["score"]
	
	#For all answers, find reputation to calculate average answer count per question.
	all_counter++
	#add total reputation for all answers
	total_reputation = total_reputation + answers[i]["reputation"]
	
#Calculate average score of accepted answers, as well as total reputation af all answers
avg_acc_score = total_accepted_score/accepted_counter
avg_all_reputation = total_reputation/all_counter

#Print results
print ("Acceptred answers are:",accepted_counter)
print ("Average score of accepted answers is:",avg_acc_score)
print ("Average reputation of all answers is:",avg_all_reputation)

#Initialize comment counter variable
top_ten_score_comments = 0

#Find 10 answers with the highest score
top_ten_score = heapq.nlargest(10, answers[score])

#Iterate again through answers json object
for i in answers:
	#Iterate through top 10 score answers
	for x in top_ten_score
		if answers[i].score == x:
			#If this answer is among top 10 highest score, add answer id and comment count to a dictionary
			dic.update({answer[i].answer_id:answer[i].comment_count})
			
#Print results			
for i in dic:
    print i, dic[i]
	
#Now that we have everything, we will create our output in json format
#Let's store our output at a dictionary, called data_dict
data_dict = {
	"total_accepted_answers": accepted_counter,
	"accepted_answers_average_score": avg_acc_score,
	"average_answers_per_question": avg_all_reputation,
	"top_ten_answers_comment_count": {dic}
}

#Create a json object with our output
json_output = json.dumps(data_dict)

#Print our outupt
print json.dumps(json_output)