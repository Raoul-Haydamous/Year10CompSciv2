def p1():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    for i in range(len(names)):
        print(names[i],age[i])
def p2():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    for i in names:
        print(i)
def p3():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    search = input('Type a name. ')
    for i in range(len(names)):
        if search in names:
            print(True)
            break
def eg1():
    student = []
    for i in range(0,3):
        student.append(input('Enter a name. '))
    print(student)
def eg2():
    array = ['','','']
    for i in range(3):
        array[i]=input('Enter a name.')
    print(array)
def t1():
    array = [4,6,7,8,10]
    find = int(input('Which num would you like to find? '))
    if find in array:
        print("found!")
def t2():
    game = []
    for i in range(4):
        game.append(input('Enter a game.'))
    print(game)
def t3():
    import random
    number = []
    for i in range(0,30):
        number.append(random.randint(0,1000))
    print(number)
def ext1():
    names = ['','','','','']
    score = []
    for i in range(5):
        names[i]=input('Enter a name. ')
        score.append(input('What is their score? '))
    search = input('Give me a user and ill tell you their score. ')
    if search in names:
        print(names[i-1],score[i-1]) #not sure why or how it works
    if search not in names:
        print('That is not a listed user.')
def ext2():
    