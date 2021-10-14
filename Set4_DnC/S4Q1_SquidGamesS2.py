from itertools import islice
#Set 4, question 1: Squid Games Season 2
#a. Given n number of players, each player will be able to pick a number from 1 to 10
#(assume that there are more than 10 players in the current round).
#b. A player can pick a number that another player got (example, Player A picked 5 and
#Player B picked 5 as well).
#c. Big boss man gets to choose a number p that is less than 10 wherein the first p
#groups with the highest count of similar numbers picked will survive.

#Solution
#Format input same as the frequent_elements output into a histogram
#Make the number chosen be the 'container'. so the container index = number; elements inside the index = number of players
#Get the p highest groups to be saved
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def frequent_elements(arr, container = []):
    for i in range(len(arr)):
        container.append(0)

    def hist(container, arr):
        if len(arr) == 0:
            return container
        elif len(arr) >= 1:
            container[arr[0]] += 1

            return hist(container, arr[1:])

    result = hist(container, arr)

    return result

def cull(arr, p):
    #Place arr into dictionary to retain the chosen number (index) and number of players per index
    my_dict = dict(list(enumerate(arr)))
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    #print(sorted_dict)
    first_p_items = take(p, sorted_dict.items())
    return(first_p_items)
        
        

arr = [1, 1, 1, 2, 2, 3, 3, 3]
p = 2

print("Input: {}".format(arr))
print("\nSurviving Groups\nNumber Picked - Number of Players")
print(cull(frequent_elements(arr),p))


