#Name:         Roger Silva Santos Aguiar
#Function:     Insertion Sort algorithm implementation
#Initial date: June 18, 2020
#Last update:  June 21, 2020

class Insertion_sort:

    #This method runs the insertionSort method to sort an
    #array in ascending order
    def insertionSortAsc(my_array):
        # Variables
        i = 1  # Index of the array

        print("Insertion sort in ascending order")

        # It displays the beginning array
        print(my_array)

        #It sorts the array
        while i < len(my_array):
            key = my_array[i] #It gets the key
            j = i - 1         #It gets the index - 1

            #It compares the key with the previous element
            while j > -1:
                if(key < my_array[j]):    #It checks if the key is less than the previous element
                    aux = my_array[j]     #It puts the element in an auxiliary variable
                    my_array[j] = key     #It changes the element
                    my_array[j + 1] = aux #It puts the element in the new position
                    key = my_array[j]     #It gets a new key

                j = j - 1 #It decreases the index j

            #It prints the array after an interaciont
            print(my_array)

            #It decreases the index i
            i = i + 1

    #*********************************************************************************
    # This method runs the insertionSort method to sort an
    # array in ascending order
    def insertionSortDesc(my_array):
        # Variables
        i = 1  # Index of the array
        key = 0  # Key to be serached in the array
        aux = 0  # It gets the element to be chenged

        print("Insertion Sort in descending order")
        # It displays the beginning array
        print(my_array)

        # It sorts the array
        while i < len(my_array):
            key = my_array[i]  # It gets the key
            j = i - 1  # It gets the index - 1

            # It compares the key with the previous element
            while j > -1:
                if (key > my_array[j]):  # It checks if the key is less than the previous element
                    aux = my_array[j]  # It puts the element in an auxiliary variable
                    my_array[j] = key  # It changes the element
                    my_array[j + 1] = aux  # It puts the element in the new position
                    key = my_array[j]  # It gets a new key

                j = j - 1  # It decreases the index j

            # It prints the array after an interaciont
            print(my_array)

            # It decreases the index i
            i = i + 1

