#More Squids
#determine which rating the dentist achieved the most.

#Step
#Use frequency solution?
#Ratings are from 1 to 10 only
#Format input same as the frequent_elements output
#Create a find_max function to find the index with highest count; use the max_num solution
#If highest count is found, find the index of that highest count and return it

def find_max(arr): 
    #Base case. comparison requires 2 elements
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
       
    ideal_max = find_max(arr[1:])
    
    if arr[0] > ideal_max:
        return arr[0]
    return ideal_max 
    
def frequent_elements(arr, container = []):
    for i in range(11): #Ratings are from 1 to 10
        container.append(0)

    def hist(container, arr):
        if len(arr) == 0:
            return container
        elif len(arr) >= 1:
            container[arr[0]] += 1

            return hist(container, arr[1:])

    result = hist(container, arr)

    return result

squids_cut = [3,3,4,4,4,2,2,1,10]
print("Input: {}".format(squids_cut))
histogram = frequent_elements(squids_cut)

#Only returns the first rating with highest count
highest_count_rating = histogram.index(find_max(histogram))

#For reference purpose
for i in range(1,11):
    print("Rating {}: {}".format(i,histogram[i]))

print("The rating with most count is {}".format(highest_count_rating))


