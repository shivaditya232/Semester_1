number_1=int(input("Enter a number"))
number_2=int(input("Enter a number"))
choice=input("Enter your choice(+ or - or * or /): ")

while(True):

    if(choice=="+"):
        print("You have chosen addition")
        result=number_1+number_2
    elif(choice=="-"):
        result=number_1-number_2
    elif(choice=="*"):
        result=number_1*number_2
    elif(choice=="/"):
        result=number_1/number_2
    else:
        print("you have not chosen proper arithmetic operation")
    print(result)

