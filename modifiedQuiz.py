#importing python built in functions

# datetime function used to acess the current time 



from datetime import datetime
# obtaining the current UTC time from the imported datetime function
d = datetime.utcnow()
#Accessing the current UTC hour
hour = d.hour







#function to determine time of day and give appropraite greeting using UTC hour obtained above
#inputs = hour
#output = " Good evening, Good morning, Good afternoon depending on time of the day"
def time_of_day():
	hour = d.hour
	if hour > 18:
		return "Good evening "
	if hour > 12:
		return "Good afternoon "
	if hour > 0:
		return "Good morning "
	pass







#list of blanks in the quizes
blanks = ['___1___','___2___','___3___','___4___','___5___']






#quizes 1 through 3 with the blanks.

quiz_1 ="One fine day queen ___1___ invited the three bears to dinner at her ice castle.\
\nThey had baerly began to eat when ___2___ in boots rushed in with ___3___'s glass slipper,\
\n'hurry, hurry we need to go help put ___4___ dumpty back together, cos all the ___5___'s men cant."

quiz_2 ="In fine arts; red, yellow and blue are ___1___ colours.\
\nThese colours can be combined to form ___2___ colours. \
\nRed + yellow yeilds ___3___ , blue + yellow yeilds ___4___ , and blue + red yeilds ___5___."

quiz_3 = "In the command line you use the mkdir command to make a new ___1___ and the touch command to make a new ___2___ .\
\nIn python mutation is supported by ___3___ but not by ___4___). \
\nIn python the def keyword is required to define a ___5___ which is otherwise called a function). "






# answers to the blanks in the quizes above. the answers are all presented in arrays
answer_1 = ["elsa", "puss", "cinderella", "humpty", "king"]

answer_2 = ["primary", "secondary", "orange", "green", "purple"]

answer_3 = [ "directory", "file", "arrays", "strings", "procedure"] 







#Greetings to the user, a bit of aesthetics and global variables that would be used by other functions


print "---------------------------------------------------------------------------------------------------------------------------------------\n" #top border
print " A QUIZ PROJECT - PART OF MY IPND NANODEGREE\n".center(150, ' ') # telling th user what the quiz is an using the center method to cventer the text
name = raw_input("What is your name ? ")
print "\n"+ time_of_day() + name + ", welcome to this quiz \n"
#asking user to  choose the level they would like to play and converting the value to an int for futher manipulation
levels= int(raw_input ("Please choose  your level; 1 for level 1, 2 for level 2 and 3 for level 3: "))







def level_choice(levels):
#procedure to return the appropriate quiz and answer based on level chosen by user
#inputs = levels from line 72 above 
#outputs = quiz and answer list relevant to chosen level, error message.
#if the user chooses anything other 1, 2 or 3 there is an error message and the game exits.
			
		if levels == 1:
			return quiz_1 ,answer_1
		if levels == 2:
			return quiz_2, answer_2
		if levels == 3:
			return quiz_3, answer_3
		else:
			print "I'm sorry "+ name + ", that is not a valid level please restart the game and type in either the digit 1, 2 or 3." 
		exit()







def soln(step):
# procedure to get the users answers and convert the answers to lower case to allow for easy comparision to the answers
#inputs = step which is a counter variable, raw_input from the user
#output = the users raw input
	user_soln = raw_input("\nEnter your answer for {} : ".format(step)).lower()
	return user_soln







def ans(step, answer): 
# Procedure to check if users aswer is correct
#inputs = step, answer
	user_ans = soln(blanks[step])
	if user_ans == answer[step]: # comparing the users answer against the answer for the specific blank for the specific quiz.
		print "\nThats right.\n \n" 
		return "yes"
#print out the chosen quiz with the users answer filling the appropriate blank
		
	


		

def guess_left(guesses):
#procedure to check how many guesses are left and if the user can continue the game
# The users answer was wrong and they are out of guesses the game is over
			if guesses ==0:
				print "\n \nGame over"
				return "x"
# The user still has guesses but the answer was wrong
			else:
				return "q"







# actual quiz
def quiz(): 
#inputs = levels, blanks 
#outputs = chosen_level
	chosen_level, answer = level_choice(levels) #assign chosen_level and answer to the quiz and answer specifically related to the chosen level respectively
	guesses = int(raw_input ( "\n \nHow many guesses would you like per quiz?, each quiz has 5 questions.( please pick an integer value) : "))# asking the user for the number of guesse they would like per quiz and converts that input to an integer
	#Telling the user how many guesses he has based on his choice and printing the relevant quiz
	print "\nYou have " + str(guesses) + " guess(es) in total for this quiz\n \n" + chosen_level
	step = 0 # initialising the counter variable
# while loop that iterates over each blank in the specific quiz 
	while step<len(blanks):
		if ans(step, answer)=="yes": #calling function ans to check user-ans is correct
			chosen_level = chosen_level.replace(blanks[step], answer[step])# if user_ans correct the quiz is filled with the correct answer for the current blank
			print chosen_level # the quiz with the filled blank is printed out
			step += 1 #change the counter step by +1 to move to the next blank
#if the users answer is wrong  error message and incomplete quiz is displayed, and the number of guesses is reduced by 1.
		else:
			print "\nSorry wrong answer \n \n" + chosen_level
			guesses -=1
# The users answer was wrong and they are out of guesses the game is over
			if guess_left(guesses) =="x": #function call to gues to check if any guesess are left, in this instance no more guesses left
				break
# The user still has guesses but the answer was wrong
			else:
				if guess_left(guesses) =="q": #function call to gues to check if any guesess are left, in this instance some guesses left
					print "\nTry again.\n \nYou have " + str(guesses) + " guess(es) left."
	print "\nThanks for playing. \n"
 
	
			





# calling the function quiz to run the game.
quiz()



'''
i drew some inspiration from some example code, and documentation i found '''













