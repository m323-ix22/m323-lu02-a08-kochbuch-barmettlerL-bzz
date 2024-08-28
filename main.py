"""
desc. here
"""
import json

def adjust_recipe(recipe, num_people):
    """
    adjusts the servings depending on the amount of people
    """
    num_people_recipe = recipe["servings"]
    editing_recipe = recipe.copy()
    for ingredient in editing_recipe["ingredients"]:
        editing_recipe["ingredients"][ingredient] = (
                editing_recipe["ingredients"][ingredient] / num_people_recipe * num_people)
    editing_recipe['servings'] = num_people
    return editing_recipe

def load_recipe(recipe):
    """
    loads recipe into a dictionary
    """
    return json.loads(recipe)



if __name__ == '__main__':
    RECIPE_JSON = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    recipe_loaded = load_recipe(RECIPE_JSON)
    adjusted_recipe = adjust_recipe(recipe_loaded, 7)
    print(adjusted_recipe)
