def main():
    AskNum() #Go to function Ask

def AskNum():
    howmany = str(input("How many grades you want to average?")) #Ask how many grades to average
    if CheckNum(howmany): #Pass the variable to Checknum
        AskGrade(int(howmany))

def AskGrade(count):
    gradelist = []
    gradesum = 0
    while count != 0:
        grade = float(input("Enter the grade"))
        gradelist.append(grade)
        gradesum += grade
        count -= 1
    average = gradesum / len(gradelist)
    print("The average is:", average)
    return average

def CheckNum(num):
    numlen = len(num) #length of num
    if numlen == 0:
        print("Invalid, please try again")
        AskNum()
        return False
    for i in range(0, numlen):
        ordnum = ord(num[i])
        if ordnum < 48 or ordnum > 57:
            print("Invalid, please try again")
            AskNum()
            return False
    return True

if __name__ == "__main__":
    main()
