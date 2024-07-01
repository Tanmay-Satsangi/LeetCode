#User function Template for python3

def isSubset( a1, a2, n, m):
    
    dict1 = {}
    
    for num in a1:
        if num not in dict1:
            dict1[num] = 1
        else: 
            dict1[num] += 1
    
    
    for num2 in a2:
        if num2 in dict1:
            if dict1[num2] == 0:
                return "No"
            dict1[num2] -= 1
        else: 
            return "No"
            
    return "Yes"
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends