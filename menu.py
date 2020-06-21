#Name:         Roger Silva Santos Aguiar
#Function:     This is the menu file, all other files will be executed from here
#Initial date: June 20, 2020
#Last update:  June 21, 2020

#Required modules
import insertion_sort
import random_numbers

class Menu:
    # It creates two tuples
    my_array = [5, 2, 4, 6, 1, 3]
    option = 0

    #This function generates and return an integer random list
    def generate_integer_list(self):
        print("This application generates a list with integer random numbers and sorts this one using Insertion Sort algorithm.")
        print("Enter the following informations:\n")

        #Prompt
        quantity = int(input("Enter the quantity of numbers you want to generate: "))
        min = int(input("Enter the initial number: "))
        max = int(input("Enter the last number: "))

        new_array = random_numbers.RandomNumbers(quantity, min, max)# It creates a new object
        integer_list = new_array.generateRandomNumbers()     # It gets an integer list with random numbers
        return  integer_list                                 # It returns the list

    #This function displays the options to the user
    def display_layout(self, integer_list):
        #Layout
        print("\n**************************************Menu**************************************")
        print("1 - Sort in ascending order")
        print("2 - Sort in descending order")
        print("3 - Exit")

        #It asks the user to choose an option
        option = int(input("Choose an option: "))
        print("\n")
        if option == 1:
            # It sorts the array in ascending order
            insertion_sort.Insertion_sort.insertionSortAsc(integer_list)
        elif option == 2:
            #It sorts the array in descending order
            insertion_sort.Insertion_sort.insertionSortDesc(integer_list)
        else:
            print("End of the application")

#If the application is executed directly, the following code will be executed.
if __name__ == '__main__':
    menu = Menu()#It creates an object
    integer_list = menu.generate_integer_list()
    menu.display_layout(integer_list)


