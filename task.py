def My_fun():
    pick_up=input("enter your pick-up point: ") #your current location
    where_to=input("enter where you've go: ") #your destination
    distance=int(input("enter the distance from your place: ")) #distance
    options=['Ubergo','UberAuto', 'Premier','UberXL', 'GoSedan']
    i=0
    while i<len(options):
        print((options[i]))
        i+=1
    select_cab=input("Choose your Ride: ")
    confirmation=input("please press confirm: ") #write confirm
    if confirmation=="confirm":
        print("Your cab will reach soon")
        destination=input("did you reach to your destination, press yes: ") 
        if destination=="yes":
            print("You've reached: ")
        total_payment=distance*5
        print("Total amount ",total_payment)
        pay=int(input("please pay: "))
        if pay==total_payment:
            print("thank you")
        give_rate=[1, 2, 3, 4, 5]
        j=0
        while j<len(give_rate):
            print((give_rate[j]), end=" ")
            j+=1
        print("* * * * * * ")
        rate=int(input("enter rate to ride: "))
        k=0
        while k<len(give_rate):
            if rate==give_rate[k]:
                feedback=input("please enter your feedback, How was your journey: ")
                print("Thank You")
            k+=1 
    else:
        print("you have Cancelled")           
My_fun()
def New_function():
    while True:
        again=input("if you want more rides press yes or no: ")
        if again=="yes":
            My_fun()
        break      
New_function()
