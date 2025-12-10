def percent(name, marks):
    a = 0
    for i in range (len(marks)):
        a+=marks[i]
    b = 80 * len(marks)
    print("Student name is", name)
    print("Average:", (a/len(marks)))
    print("Percentage:", (100*(a/b)), "%")

andrew = [77, 72, 80, 79, 69, 73, 80]
percent("Andrew", andrew)

