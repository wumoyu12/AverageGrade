def main():
    AskNum()  # Entry point of the program, calls AskNum() to start the process

def AskNum():
    howmany = str(input("How many grades you want to average?"))  # Prompt user for the number of grades to average
    if CheckNum(howmany):  # Validate the input number
        AskGrade(int(howmany))  # If valid, proceed to ask for grades

def AskGrade(count):
    gradelist = []  # Initialize an empty list to store grades
    while count != 0:  # Loop until all grades are collected
        grade = str(input("Enter the grade"))  # Prompt user for a grade
        if CheckGrade(grade):  # Validate the grade input
            grade = float(grade)  # Convert valid grade to float
            gradelist.append(grade)  # Add grade to the list
            count -= 1  # Decrement remaining grade count
    
    gradesum = 0  # Initialize sum of grades
    for grade in gradelist:  # Iterate through the grade list
        gradesum += grade  # Accumulate the sum of grades
    
    average = gradesum / len(gradelist)  # Calculate the average
    print("The average is:", average)  # Display the average
    return average  # Return the average value

def CheckNum(num):
    numlen = len(num)  # Get the length of the input string
    if numlen == 0:  # Check if input is empty
        print("Invalid, please try again")
        AskNum()  # Restart the number input process
        return False  # Return validation failure
    for i in range(0, numlen):  # Iterate through each character
        ordnum = ord(num[i])  # Get ASCII value of the character
        if ordnum < 49 or ordnum > 57:  # Check if character is not a digit (1-9)
            print("Invalid, please try again")
            AskNum()  # Restart the number input process
            return False  # Return validation failure
    return True  # Return validation success

def CheckGrade(grade):
    grade = grade.strip()  # Remove leading/trailing whitespace
    if len(grade) == 0:  # Check if input is empty after stripping
        print("Empty input, please try again")
        return False  # Return validation failure
    
    dotCount = 0  # Track the number of decimal points
    for i in range(0, len(grade)):  # Iterate through each character
        ordnum = ord(grade[i])  # Get ASCII value of the character
        if ordnum == 46:  # Check if character is a decimal point
            dotCount += 1  # Increment decimal point count
            if dotCount > 1:  # Check for multiple decimal points
                print("Invalid number format, please try again")
                return False  # Return validation failure
        elif ordnum < 48 or ordnum > 57:  # Check if character is not a digit or decimal point
            print("Invalid character, please try again")
            return False  # Return validation failure
    
    gradeNum = float(grade)  # Convert valid input to float
    if gradeNum < 0 or gradeNum > 100:  # Check if grade is within valid range (0-100)
        print("Grade must be between 0 and 100, please try again")
        return False  # Return validation failure
    
    return True  # Return validation success

if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly
