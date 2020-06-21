#Name:         Roger Silva Santos Aguiar
#Function:     This is the menu file, all other files will be executed from here
#Initial date: June 20, 2020
#Last update:  June 20, 2020

#Required modules
import insertion_sort

class Menu:
    # It creates two tuples
    my_array = [5, 2, 4, 6, 1, 3]
    option = 0

    #Layout
    print("**************************************Menu**************************************")

    print("1 - Sort in ascending order")
    print("2 - Sort in descending order")
    print("3 - Exit")

    #It asks the user to choose an option
    option = int(input("Choose an option: "))
    print("\n")

    if option == 1:
        #It sorts the array in ascending order
        insertion_sort.Insertion_sort.insertionSortAsc(my_array)
    elif option == 2:
        #It sorts the array in descending order
        insertion_sort.Insertion_sort.insertionSortDesc(my_array)
    else:
        print("End of the application")






