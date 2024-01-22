def displayRestRatings(restaurant):
    """This function prints each rating for a specified restaurant.  This function takes in one mutable argument, which is an object of type Restaurant."""

    print("\nRatings for " + restaurant.getName())
    #for loop which iterates over each restaurant rating
    for i in range(0, restaurant.getRatingsSize()):
        #printing each restaurant rating to the user
        print("Rating Index: " + str(i))
        restaurant.getRatings(i).printRating()