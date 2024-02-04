![video_poster_1](https://github.com/Python-Coding-Assignments/Restaurant-Ratings-Part-1/assets/154717520/f187d60f-69a1-456e-a825-24bcd4ab554b)

<details>
<summary>Table of Contents</summary>
<ol>
  <li>
    <a href='#about-the-project'>About the Project</a>
  </li>
  <li>
    <a href='#getting-started'>Getting Started</a>
  </li>
  <li>
    <a href='#Contact'>Contact</a>
  </li>  
</ol>
</details>

## About the Project
This project simulates a simple application where information about a restaurant is made available to the user.  The user can do any of the following: print all restaurants (including information about each restaurant), print all ratings for a restaurant specified by the user, add more ratings to a restaurant he or she specifies, print a specified restaurant's rating, and lastly edit a specified restaurant's rating.

The objective of this program is to demonstrate the following: 
* show a basic understanding of classes and how they work, including the init constructor, setters, and getters
* utilize packages to organize classes and functions in different directories
* introduce the concept of encapsulation in this simple program and work with attributes that are made private to the user

In this program, the user can enter anything, even when prompted with entering an integer menu selection, and the program will still function as intended. 

## Getting Started
To run the program, download the contents of the project and simply run make in the terminal.

Once the project is open, you will be prompted with a menu display different menu options. To continue, you will need to enter a letter that corresponds to one of the menu options; otherwise, an error message will be displayed.

For some menu options, the program requests a restaurant index and rating index input from the user. The restaurant/rating index that the program is requesting is the index in which the user's chosen restaurant/rating appears in the already initialized list. Recall, in a list, the first element is at index zero, the second element is at index one, and so forth. To see which restaurants are at which restaurant index, you can input the character "A" for the menu selection, and then a list of the restaurants at their specified index is printed to the screen.

For menu options D and E, the program will request the restaurant index from the user, which we just went over above.  Then, the program will request the rating index from the user.  The logic regarding the ratings indices parallels that of the restaurant indices; however, there is no menu option to print all of the ratings a given restaurant has.  Each restaurant that has been initialized by the program begins with two ratings; therefore, if no ratings have been added to a restaurant at a specified index, then the only valid inputs for menu option D are "0" and "1".  Once new ratings have been added to a restaurant, then valid rating index inputs will contain more strings than simply "0" and "1", such as "2", "3", and so forth.

## Contact
Name: Garrett Ellis\
Project Link: [https://github.com/Python-Coding-Assignments/Restaurant-Ratings-Part-3]()
