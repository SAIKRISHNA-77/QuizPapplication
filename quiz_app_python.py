# This is a command prompt test
# Importing libraries
import random
import json
import sys

f = open('data.json') # Reading data of questions and answers file
data = json.load(f) # returns JSON object as a dictionary

original_questions = data["original_questions"] # Questions dict
answers = data["answers"] # Answers dict used for validation
ans_mapping = data["ans_mapping"] # Answers mapping to numerical index

qns_list = list(original_questions.keys()) # getting all question numbers for shuffling
random.shuffle(qns_list) #shuffling the questions

#Test starts here
option_dict = {} #Answers stored in this dict
qns_cnt=1 # Question counting

# Test Instructions
print ("\n\t*************** Please choose one option from the provided options.******************\n"
	   "****** If you enter any invalid option which is not present in the options , then TEST WILL EXIT *****\n\n")
for qns in qns_list:
	print("{}.What is {}? ".format(qns_cnt, original_questions[qns]["qns"]))
	print ("a.{} b.{} c.{} d.{}".format(original_questions[qns]["ans"][0], original_questions[qns]["ans"][1],
										original_questions[qns]["ans"][2], original_questions[qns]["ans"][3]))
	option = input("Please enter your answer:  ")
	if option not in ["a", "b", "c", "d"]:
		print ("\n########  Exited: Inputted invalid option  ###########")
		sys.exit()
	option_dict[qns] = option
	qns_cnt +=1
	print ("\n")

# Score calculation
score = 0
print ("-------------------Quiz RESULTS --------------------")
for qns in option_dict:
	option_mapped = ans_mapping[option_dict[qns]]
	correct_ans = ans_mapping[answers[qns]]
	print ("Q:What is {},      Your ans: {},     Correct ans: {}".format(original_questions[qns]['qns'],original_questions[qns]['ans'][option_mapped],
							 original_questions[qns]['ans'][correct_ans]))
	if option_dict[qns] == answers[qns]:
		score += 1
print ("\nThank you for taking Test and Your have Scored: {}/10".format(score))
