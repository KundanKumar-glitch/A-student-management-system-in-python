print("======================================")
print("STUDENT MANAGEMENT SYSTEM")
print("======================================")
ch=0
Student = []
def addStudent():
    print("--Enter the following deatils of student--")
    name = input("name: ")
    age = input("Age: ")
    roll = int(input("Roll: "))
    branch = input("Branch: ")
    cgpa = input("cgpa of prev sem: ")
    mobile = input("mobile no: ")

    Student.append({
        "name":name,
        "age":age,
        "roll":roll,
        "branch":branch,
        "cgpa":cgpa,
        "mobile no":mobile 
    })
    print("STUDENT ADDED SUCCESSFULLY")

def viewStudent():
    op = input("do you want to view all Student (yes/no)").lower()
    if op=="no":
        rn = int(input("enter the roll of student"))
        for i in Student:
            if i["roll"]==rn:
                print("name\n",i["name"],
                        "age\n",i["age"],
                        "roll\n",i["roll"],
                        "branch\n",i["branch"],
                        "cgpa\n",i["cgpa"],
                        "mobile",i["mobile no"]
                        )
        
    elif op=="yes":
        print(Student)
    else:
        print("invalid !")

def searchStudent():
    rn = int(input("Enter the roll of student"))
    for i in Student:
        if i["roll"]==rn:
            print("student exists in our data")
            print("go and select the 2nd option to view the Student details")
        else:
            print("student not found!")


def updateStudent():
    chh=0
    rn = int(input("Enter student roll no:"))
    for i in Student:
        if i["roll"]==rn:
            while(chh!=6):
                chh = int(input("1.change name\n2.change age\n3.change branch\n4.change cgpa\n5.change mobile no\n6.exit"))                       
                match (chh):
                    case 1:
                        i["name"] = input("enter other name:")
                        print("name changed success!")
                        
                    case 2:
                        i["age"] = input("enter other age:")
                        print("age changed success!")
                        
                    case 3:
                        i["branch"] = input("enter other branch:")
                        print("branch changed success!")
    
                    case 4:
                        i["cgpa"] = input("enter other cgpa:")
                        print("cgpa changed success!")
                        
                    case 5:
                        i["mobile no"] = input("enter other mobile no: ")
                        print("mobile changed success!")
                        

                    case 6:
                        print("-- exiting --")
                        return
                        
        else:
            print("student not found!")

                        
def deleteStudent():
    chh=0
    rn = int(input("Enter student roll no:"))
    for i in Student:
        if i["roll"] == rn:
            print("Student named", i["name"], "deleted successfully!")
            Student.remove(i)
            return
        else:
            print("student doesn't exists!!")


        
def marksResult():
    
    rn = int(input("Enter student roll no:"))
    for i in Student:
        if i["roll"]==rn:
            print( i["cgpa"])
        else:
            print("student doesn't exists!!")
        

          
def attendence():
    rn = int(input("enter student roll no:"))
    for i in Student:
        if i["roll"]==rn:
            print("attendence==")
        else:
            print("student doesn't exists!!")





                    

while(ch!=8):
    print("1.Add Student\n2.View Student\n3.Search student\n4.Update Student\n5.Delete Student\n6.Marks & Result\n7.Attendence\n8.Exit")
    ch = int(input("enter your choice: "))
    if (ch<=8 and ch>0):
        match (ch):
            case 1:
                print("Add Student")
                addStudent()
                
            case 2:
                print("View Studeent")
                viewStudent()
                
            case 3:
                print("Search Student")
                searchStudent()
                
            case 4:
                print("Update Student")
                updateStudent()
                
            case 5:
                print("Delete Student")
                deleteStudent()
                
            case 6:
                print("Marks & Result")
                marksResult()
                
            case 7:
                print("Attendence")
                attendence()
                
            
            case 8:
                print("exiting program")
                break
    else:
        print("invalid choice!")


            