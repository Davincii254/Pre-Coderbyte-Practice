def SearchingChallenge(str):
  """
  Finds the first non-repeating character in a string and combines it with a challenge token.

  Args:
    str: The input string.

  Returns:
    A string containing the reversed first non-repeating character 
    followed by a colon and the reversed challenge token.
  """
  char_count = {} 

  # Count character frequencies
  for char in str:
    if char != " ": 
      char_count[char] = char_count.get(char, 0) + 1 

  # Find the first non-repeating character
  for char in str:
    if char != " " and char_count[char] == 1:
      non_repeating_char = char
      break

  # Reverse the non-repeating character and the challenge token
  reversed_char = non_repeating_char[::-1] 
  reversed_token = challengeToken[::-1] 

  # Combine and return the result
  finished_ans = f"{reversed_char}: {reversed_token}"
  return finished_ans

# Example usage:
# Assuming you have a way to get input from the user
# (e.g., using the `input()` function)
input_string = input() 
print(SearchingChallenge(input_string))