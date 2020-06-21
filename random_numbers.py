#Name:         Roger Silva Santos Aguiar
#Function:     This class generates and returns an array or random numbers
#Initial date: June 21, 2020
#Last update:  June 21, 2020

#Required modules
import random

class RandomNumbers:
    #This function will be automaticalky called when the object is created
    def __init__(self, quantity, min, max):
        self.quantity = quantity
        self.min = min
        self.max = max

    #This function generates and returns a list with integer random numbers
    def generateRandomNumbers(self):
        #Variables
        count = 0

        #It creates a list
        random_numbers = []

        #It fills the list with random numbers
        while count < self.quantity:
            random_numbers.append(random.randint(self.min, self.max))
            count = count + 1

        #It returns an array with random numbers
        return random_numbers
