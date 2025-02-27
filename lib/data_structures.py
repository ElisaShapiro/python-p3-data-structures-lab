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

def get_names(spicy_foods):
    return [spicy_food["name"] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {"🌶" * spicy_food["heat_level"]}' )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    return sum([spicy_food["heat_level"] for spicy_food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
