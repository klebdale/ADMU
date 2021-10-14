#Optimal Prime
#Given a prime number and a number n, 
#write a function that returns the prime numbers before the given input prime number within the window of n.

#Steps
#Part 1: check if given number is prime, else stop already
#Part 2: Do DnC on window given

def is_prime(number, divisor):
    if number > 1: #prime numbers are greater than 1, else not prime
    
        if number == divisor: #Base case: If divisor reached the number already without finding any factor
            return True

        if number % divisor == 0: #If it has a divisor other than itself then not prime
            return False

        return(is_prime(number,divisor+1))
    
    return False

def count_prime(start_num, input_num, final_count, window_prime):
    for num in range(start_num, input_num+1): #had to +1 to be inclusive
        if (is_prime(num,2)):
            final_count+=1
            window_prime.append(num)
        
    return final_count, window_prime
  
input_num = 23
n = 5
start_num = input_num - n
window_prime =[]

#Part 1
print("Is {} a prime number? {}".format(input_num,is_prime(input_num, 2))) 
if(is_prime(input_num, 2)):
    #Part 2
    print("From {} to {}, there are {} prime number(s)".format(start_num, input_num, count_prime(start_num,input_num, final_count=0,window_prime=[])))
