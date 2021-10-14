#Stairway to heaven

#The function should return the path from (0,0) to (n,m) whose sum of all elements has a maximum value.
#movement is left-right and top-bottom only
#starting is 0,0 (top left)
#ending is n,m (lower right)

#Another possible solution is to transform the matrix into binary tree (since possible movements are right and down only)
#Conduct a depth-based sum of each branch
#possible to do in DnC / recursive manner. Problem is the transformation of matrix into binary tree
#driver code to manually input values to each left and right node is lengthy


def stairway(matrix, routes):
    n = len(matrix)
    m = len(matrix[0])
    
    def recursive(mat,route,x,y,total):
        
        total += mat[x][y]
        route.append(mat[x][y])
        
        #base case - if corner already
        if (x == n-1 and y == m-1):
            routes.append([total,route.copy()])
            route.pop()
            return
        
        else:
            #right movement
            if x+1 < n:
                recursive(mat,route,x+1,y,total)

            #bottom movement
            if y+1 < m:
                recursive(mat,route,x,y+1,total)
       
        if route: route.pop()
            
    recursive(matrix,[],0,0,0)
    return routes
    

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]  
]

#returned routes format is [sum, path]
#sort routes based on sum (largest sum first)
sorted_paths = sorted(stairway(matrix,[]),key=lambda x: (x[0]), reverse=True)

#Check all the paths and sums; for reference purpose
#for route in sorted_paths:
#    print(route)

#Output the path with largest sum
print("Path {} has the largest sum of {}".format(sorted_paths[0][1], sorted_paths[0][0]))

