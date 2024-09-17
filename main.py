# Programmer: Andrew Leimbach
# Course:  CS151, Dr. Zee
# Due Date: 9/18/2024
# Programming Assignment: PA0
# Problem Statement:  Calculating the average of three test scores
# Data In: The three scores on the tests as percentages
# Data Out:  The average score of all three test scores as a percentage

Score_1 = float(input("Enter Score 1: ")) #Prompts user to input their first score
Score_2 = float(input("Enter Score 2: ")) #Prompts user to input their second score
Score_3 = float(input("Enter Score 3: ")) #Prompts user to input their third score

Average_Score = (Score_1 + Score_2 + Score_3) / 3 #Calculates the average score of all three test scores imported in by user

print(f"This is the average score of all three test scores: {Average_Score:.2f}") #Outputs the users average test score