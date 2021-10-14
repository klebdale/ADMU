#Optimus Prime
#given a number, would return if it’s prime or not
#prime numbers are whole numbers greater than 1, that have only two factors – 1 and the number itself.

#Steps
#create is_prime function that gets the input_number
#iterate all the numbers starting from 2 until the input_number and divide it
#if there is a number (other than the input_number itself) that can divide it, then not prime
#If after all numbers are exhausted (input_number == factor), then it is prime
#Early filtering: prime numbers are always greater than 1


def is_prime(number, divisor):
    if number > 1: #prime numbers are greater than 1, else not prime
    
        if number == divisor: #Base case: If divisor reached the number already without finding any factor
            return True

        if number % divisor == 0: #If it has a divisor other than itself then not prime
            return False

        return(is_prime(number,divisor+1))
    
    return False
  
input_num = 113
print("Is {} a prime number? {}".format(input_num,is_prime(input_num, 2))) 
#We start checking factors from 2. 2 here is the starting divisor

#Alternative solution
#Setup an array of possible factors. then do window movement

