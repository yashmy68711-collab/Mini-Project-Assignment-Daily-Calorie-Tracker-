# tracker.py - Daily Calorie Tracker 

print("===================================")
print("   Welcome to Daily Calorie Tracker CLI")
print("   Track your meals, calories, and daily limit")
print("===================================\n")


meals = []
calories = []

n = int(input("How many meals did you eat today? "))

for i in range(n):
    meal = input(f"Enter meal {i+1} name: ")
    cal = int(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)


print("\nYour Meals for Today:")
for meal, cal in zip(meals, calories):
    print(f"- {meal}: {cal} calories")


total_calories = sum(calories)
print(f"\nTotal calories consumed today: {total_calories}")

limit = int(input("\nEnter your daily calorie limit: "))

if total_calories > limit:
    print(f"You exceeded your limit by {total_calories - limit} calories!")
else:
    print(f"Good job! You are within your limit, {limit - total_calories} calories left.")


with open("session_log.txt", "a") as file:
    file.write("Today's Log:\n")
    for meal, cal in zip(meals, calories):
        file.write(f"{meal}: {cal} calories\n")
    file.write(f"Total Calories: {total_calories}\n")
    file.write(f"Daily Limit: {limit}\n")
    if total_calories > limit:
        file.write(f"Exceeded by {total_calories - limit} calories.\n")
    else:
        file.write(f"Within limit, {limit - total_calories} calories remaining.\n")
    file.write("-"*30 + "\n")

print("\nSession saved to 'session_log.txt'.")
