
user_input = int(input("Enter a number: "))

odds_under_input = [num for num in range(1, user_input) if num % 2 != 0]

start_odd = user_input if user_input % 2 != 0 else user_input + 1
another_odds_list = [num for num in range(start_odd, start_odd + 10) if num % 2 != 0]

print("\n--- Task 1 Results ---")
print("Odd numbers below your input:", odds_under_input)
print("Another list of odd numbers:", another_odds_list)


fruits = ["apple", "banana", "cherry", "date"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]


print("\n--- Task 2 Results ---")
print("Original list:", fruits)
print("Updated list:", capitalized_fruits)
