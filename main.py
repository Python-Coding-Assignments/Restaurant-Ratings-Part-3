from Functions import initRestaurants, promptAction, implementAction

#declaration and initialization of variables
restaurants = []
flag = False
userAction = ""

#welcoming user and initializing default restaurants
print("Welcome to my Restaurant Ratings App!\n")
initRestaurants(restaurants)

#while loop which runs until the user decides to quit the program
while flag == False:
    #getting user menu selection input
    userAction = promptAction()

    #determining how the program should run based on user's input
    implementAction(restaurants, userAction)

    #conditional statement checking if user's menu selection is either "q" or "Q"
    if userAction == "q" or userAction == "Q":
        flag = True