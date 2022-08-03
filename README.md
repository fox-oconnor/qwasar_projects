This repo contains projects completed while at Qwasar Silicon Valley (http://qwasar.io) 

# Roman Numerals Converter (Python, DS Preseason Track)

## Task
The task is to convert common number entries into roman numerals. The challenge in this project is to split the larger numbers into smaller numbers that correspond with known Roman Numerals.

## Description
To solve the problem I created two different functions within the main function. 
The first function loops over the integer input and breaks it down into smaller numbers in accordance with a dictionary containing major Roman Numerals up to and including 1000.
The second function loops over the output of the first function to concatenate the finished Roman Numeral. 
In addition to these two functions there is also code that ensures the list output from the first function contains only int. 

## Installation
Currently the project is run in the terminal. 

## Usage
A number is input into the main function for conversion. From there, the number is then broken down into smaller numbers that correspond with a dictionary of major roman numerals.
Those smaller numbers are then stored in a list for future use. The list is then checked for non-integers, all of which are assigned an integer value of 0, as they are not of any relevance to the final output.
The list of numbers is then run through a second function which matches the times each roman numeral should be used and concatenates the final output as it loops over the list. 
  
# My Cat (Python, DS Preseason Track)

## Task
The task is to recreate the cat command using python script.

## Description
I imported the sys module in python, then used a for loop to iterate over the input arguments, skipping the first argument as it is the python program itself.


## Installation
Run the program from the command line using python.

## Usage
Using the input in the command line given by the user, the program opens each given file, reads the contents and the adds the contents of the file to an output variable. 
Once each of the files have been read and added to the output variable, the program then prints the contents of the output to the terminal. 

# My First Scraper (Python, DS Preseason Track)

## Task
To write a web scraper in Python that will pull data from github's trending repo page. 
The challenge is finding the correct tags to use to pull data from the website. 

## Description
First I used requests to retrieve the html code from the input URL (github.com/trending). 
Then using BeautifulSoup I isolated the tags that contained the required information, and converted them
to a dictionary containing key-value pairs. Once this was completed I used the io and csv modules to convert
the dictionary to a CSV string.

## Installation
Run the program from the command line interface. 

## Usage
The program first retrieves the html for input website, this is done using the requests module.
This step is shown in the request_github_trending function. 
The second step is to use BeautifulSoup to isolate the articles containing the required data. 
The function extract does this.
The third step is to separate the specific data from each of the article elements, and then return that data
as a list. 
This is done in the transform function. 
The final step is to change the dictionary of key, value pairs into a csv string. 
This is done using the io and csv modules in the final function, format.
