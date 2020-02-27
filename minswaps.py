# Python3 program to find the minimum 
# number of swaps required to sort 
# the given array 

# Function to find minimum swaps 
def minimumSwaps(arr): 
	
	# Initialise count variable 
	count = 0; 
	i = 0; 
	while (i < len(arr)): 

		# If current element is 
		# not at the right position 
		if (arr[i] != i + 1): 

			while (arr[i] != i + 1): 

				# Swap current element 
				# with correct position 
				# of that element  
				arr[arr[i] - 1],arr[i] = arr[i],arr[arr[i]-1] 
				count += 1; 
			
		# Increment for next index 
		# when current element is at 
		# correct position 
		i += 1; 
	
	return count; 

# Driver code 
if __name__ == '__main__': 
	arr = [4,3,1,2]; 

	# Function to find minimum swaps 
	print(minimumSwaps(arr)); 
	
