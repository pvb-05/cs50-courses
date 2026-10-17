# submit50 cs50/problems/2022/python/nutrition
fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapes": 60,
    "Grapefruit": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 60,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 30,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 50
}

str = input('Input:').strip().lower().title()

if str in fruits:
    print(f'Calories: {fruits[str]}')
