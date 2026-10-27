#Functions used in preparing Guido's gorgeous lasagna.
#Learn about Guido, the creator of the Python language:
#https://en.wikipedia.org/wiki/Guido_van_Rossum
#This is a module docstring, used to describe the functionality
#of a module and its functions and/or classes.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 10


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculates the remaining bake time by subracting the elapsed bake time from the expected bake time constant"""
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return(result)
    
    #Calculate the bake time remaining.

    #Parameters:
        #elapsed_bake_time (int): The baking time already elapsed.

   # Returns:
        #int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

#Function that takes the actual minutes the lasagna has been in the oven as
    #an argument and returns how many minutes the lasagna still needs to bake
    #based on the `EXPECTED_BAKE_TIME`.
    

    


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculates the time to prep, in minutes by multiplying the amount of layers by 2 (two minutes per layer)"""
    result = number_of_layers * 2 
    return(result)

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the elapsed time in minutes by calculating the prep time in minutes (number of layers *2) + the elapsed bake time """
    result = number_of_layers*2 + elapsed_bake_time
    return(result)


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
