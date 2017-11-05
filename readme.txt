Stackstats application

Author: Dimitris Zafeiris
Date: 04/11/2017
Version: 1.0

This is an application named stackstats that retrieves data from the StackExchange API and calculates some simple statistics.

In order to launch it, just run program stackstats.py.

Description:
We will use requests library to retrive stack exchange data in json format.
To install requests library at your machine, open a cmd and run:
pip list (to see if you laready has it and its version)
pip install requests

We will also use json library to create the output in json format.
Also, heapq library to find top 10 elements of json objects.

#program
Ask user to provide input date/time range for since and until dated, with the correct format.
After that, retrieve answers and comments on answers, from stackexchange with the given date/time range.
Iterate through answers to calculate the total number of accepted answers, the average score for all the accepted answers and the average answer count per question.
Find top 10 scores from all answers with heapq.nlargest and append these answer_ids along with comment_count to a dictionary.
Output all results in a new dictionary.
Create a new json object, with all information of above dictionary.
Print the output of this json object.