def StringChanges(strParam):
    result = []  # Initialize an empty list to store the modified characters
    i = 0       # Initialize an index to iterate through the input string
    while i < len(strParam):  # Loop through the input string
         if strParam[i] == 'M':  # Check if the current character is 'M'
            if result:        # Check if the result list is not empty (important for first 'M')
               result.append(result[-1]) # Duplicate the last character added
         elif strParam[i] == 'N':  # Check if the current character is 'N'
            i += 1             # Skip the next character (if it exists)
         else:                 # If it's a lowercase letter
            result.append(strParam[i]) # Add it to the result
         i += 1             # Increment the index to move to the next character
    strParam = ''.join(result) # Join the characters in the list back into a string
    return strParam           # Return the modified string

# keep this function call here 
print(StringChanges(input())) # Get input and print the result