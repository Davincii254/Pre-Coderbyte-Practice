def HDistance(strArr):
    

    # Input validation: Check if the input array has exactly two strings
    if len(strArr) != 2:
        return "Invalid input: strArr must contain two strings."  # Return error message

    str1 = strArr[0]  # Assign the first string to str1
    str2 = strArr[1]  # Assign the second string to str2

    # Input validation: Check if the strings have equal length
    if len(str1) != len(str2):
        return "Invalid input: Strings must be of equal length."  # Return error message

    distance = 0  # Initialize the Hamming distance counter to 0

    # Iterate through the strings, comparing characters at each position
    for i in range(len(str1)):  # Loop from index 0 to the length of the string - 1
        if str1[i] != str2[i]:  # Check if the characters at the current index are different
            distance += 1  # If different, increment the distance counter

    return distance  