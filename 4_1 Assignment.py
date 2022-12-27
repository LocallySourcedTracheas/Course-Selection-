#Vanessa Junco
#COP2500 002
#Assignment: 4.1
#11/4/2022

def create_list(x):
    arr = x.split(",")
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
        arr[i] =arr[i].capitalize()

    return arr

def print_courses(courses):
    print("Current courses:\n")
    for i in range(0, len(courses)):
        print(str(i+1) + ". " + str(courses[i]))

def main():
    print("Courses not being taken:\n")

    courses = []

    while(len(courses) != 5):
        if(len(courses) < 5):
            user_courses = input("Add course:\n")
            user_list = create_list(user_courses)
            for i in range(len(user_list)):
                courses.append(user_list[i])
        else:
            user_drop_courses = input("Drop course:\n")
            user_drop_list = create_list(user_drop_courses)
            for i in range(len(user_drop_list)):
                courses.remove(user_drop_list[i])

        print_courses(courses)

    print("Done!")
    

main()
