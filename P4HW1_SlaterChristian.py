# CTI-110
# P4HW2 - Score list
# Christian Slater
# 11/15/2023

# Prompt the user to enter the number of scores they would like to enter
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Initialize an empty list to store the scores
scores = []

# Loop to collect the number of scores the user wants to enter
for i in range(num_scores):
    while True:
        try:
            # Ask the user to enter a score
            score = int(input(f"Enter score {i+1}: "))
            # Check if the score is valid (between 0 and 100)
            if 0 <= score <= 100:
                # Add the valid score to the list
                scores.append(score)
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid score.")

# Display the lowest score entered
print(f"Lowest score entered: {min(scores)}")

# Remove the lowest score from the list
modified_scores = scores.copy()
modified_scores.remove(min(scores))

# Display the modified score list after dropping the lowest score
print(f"Score List after dropping lowest score: {modified_scores}")

# Calculate the average of scores in the modified list
average_score = sum(modified_scores) / len(modified_scores)
print(f"Average score: {average_score}")

# Determine the letter grade for the calculated average
if average_score >= 90:
    print("Letter Grade: A")
elif average_score >= 80:
    print("Letter Grade: B")
elif average_score >= 70:
    print("Letter Grade: C")
elif average_score >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
