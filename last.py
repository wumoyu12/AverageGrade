def main():
    AskNum()

def AskNum():
    howmany = str(input("How many grades you want to average?"))
    if CheckNum(howmany):
        AskGrade(int(howmany))

def AskGrade(count):
    gradelist = []
    while count != 0:
        grade = str(input("Enter the grade"))
        if CheckGrade(grade):
            grade = float(grade)
            gradelist.append(grade)
            count -= 1
    
    gradesum = 0
    for grade in gradelist:
        gradesum += grade
    
    average = gradesum / len(gradelist)
    print("The average is:", average)
    return average

def CheckNum(num):
    numlen = len(num)
    if numlen == 0:
        print("Invalid, please try again")
        AskNum()
        return False
    for i in range(0, numlen):
        ordnum = ord(num[i])
        if ordnum < 49 or ordnum > 57:
            print("Invalid, please try again")
            AskNum()
            return False
    return True

def CheckGrade(grade):
    grade = grade.strip()
    if len(grade) == 0:
        print("Empty input, please try again")
        return False
    
    
    dotCount = 0
    for i in range(0, len(grade)):
        ordnum = ord(grade[i])
        if ordnum == 46:
            dotCount += 1
            if dotCount > 1:
                print("Invalid number format, please try again")
                return False
        elif ordnum < 48 or ordnum > 57:
            print("Invalid character, please try again")
            return False
    
    gradeNum = float(grade)
    if gradeNum < 0 or gradeNum > 100:
        print("Grade must be between 0 and 100, please try again")
        return False
    
    return True

if __name__ == "__main__":
    main()
