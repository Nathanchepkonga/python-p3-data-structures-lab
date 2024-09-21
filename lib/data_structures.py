spicy_foods = [ 
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. Function to get the names of all the spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Function to get spiciest foods (heat level > 5)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Function to print each spicy food in the desired format
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

# 4. Function to get a spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

# 5. Function to print only the spiciest foods (heat level > 5)
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# 6. Function to get the average heat level of all foods
def get_average_heat_level(spicy_foods):
    total_heat_level = sum([food["heat_level"] for food in spicy_foods])
    return total_heat_level // len(spicy_foods)

# 7. Function to add a new spicy food to the list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
