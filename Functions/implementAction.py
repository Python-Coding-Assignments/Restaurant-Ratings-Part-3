from Functions import displayRestaurants, displayRestRatings, validIndex, amendRatings, displayIndexRating

def implementAction(restaurants, action):
    """This function determines who the flow of the program will run based on the user's menu selection.  This function takes in two arguments into its parameter list: restaurants and action."""

    #declaration and initialization of variables
    index = 0
    ratingIndex = 0

    #conditional statement which checks if user's input is either "a" or "A"
    if action == "a" or action == "A":
        #calling displayRestaurants function to display all the restaurants in the system
        displayRestaurants.displayRestaurants(restaurants)

    #conditional statement which checks if user's input is either "b" or "B"    
    elif action == "b" or action == "B":
        print("\nDisplay all ratings for a restaurant...")
        #getting a valid restaurant index from user by calling validIndex function
        index = validIndex.validIndex(restaurants, "length of restaurant")   
        #calling displayRestaurants function to display all the restaurant's in the system          
        displayRestRatings.displayRestRatings(restaurants[index])  

    #conditional statement which checks if user's input is either "c" or "C"
    elif action == "c" or action == "C":
        print("\nAdd a rating to a restaurant...")
        #getting a valid restaurant index from user by calling validIndex function
        index = validIndex.validIndex(restaurants, "length of restaurant")
        #calling addRating function to add a rating to the specified restaurant
        amendRatings.amendRatings(restaurants[index])

    #conditional statement which checks if user's input is either "d", "D", "e", or "E"
    elif action == "d" or action == "D" or action == "e" or action == "E":
        print()
        #getting a valid restaurant index from user by calling validIndex function
        index = validIndex.validIndex(restaurants, "length of restaurant")
        #getting a valid rating index from the user by calling validIndex function 
        ratingIndex = validIndex.validIndex(restaurants[index], "number of ratings") 
        #calling displayIndexRating function to display a rating at the specified restaurant and at the specified index
        displayIndexRating.displayIndexRating(restaurants[index], ratingIndex)
        if action == "e" or action == "E":
            #calling addRating function to add a rating to the specified restaurant
            amendRatings.amendRatings(restaurants[index], ratingIndex)     
        
