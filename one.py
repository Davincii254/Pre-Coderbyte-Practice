def MathChallenge(num1, num2):
  """
  Calculates the rounded division of two numbers, formats the result, 
  reverses it, and combines it with a reversed challenge token.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    A string containing the reversed formatted result 
    followed by a colon and the reversed challenge token.
  """
  try:
    ans = round(num1 / num2)
    formatted_ans = str(ans)  # Convert integer to string for formatting
    reversed_ans = formatted_ans[::-1] 
    reversed_token = "tdaospy613"[::-1]
    return f"{reversed_ans}:{reversed_token}" 
  except ZeroDivisionError:
    return "Error: Division by zero" 

# Example usage:
# Assuming you have a way to get input from the user
# (e.g., using the `input()` function)
input_string = input("Enter two numbers separated by a space: ")
num1, num2 = map(int, input_string.split()) 
print(MathChallenge(num1, num2))