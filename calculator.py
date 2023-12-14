from prototypeClasses import Recipe, Item, Resource


def get_inputs(desired_item, desired_quantity=1):
    required_ingredients = {}

    # Retrieve the item instance by name
    item = Item.get_instance(desired_item)

    if type(item) is not Resource:
        # Check if the item has associated recipes
        if hasattr(item, 'recipes') and isinstance(item.recipes, list):
            for recipe_name in item.recipes:
                # Retrieve the recipe instance by name
                recipe = Recipe.get_instance(recipe_name)

                if recipe:
                    # Calculate the required ingredients for the desired quantity
                    for ingredient_name, ingredient_quantity in recipe.ingredients:
                        required_ingredients[ingredient_name] = \
                            required_ingredients.get(ingredient_name, 0) + (ingredient_quantity * desired_quantity)
    else:
        return None

    return required_ingredients


def get_raw_inputs(desired_item, desired_quantity=1):
    required_raw_inputs = {}
    items_required = {}
    recipes = Recipe.get_all_instances()

    items_required[desired_item] = desired_quantity

    while items_required:
        item, quantity = items_required.popitem()
        # Retrieve the item instance by name
        item_instance = Item.get_instance(item)

        if isinstance(item_instance, Resource):
            if item_instance.name not in required_raw_inputs.keys():
                required_raw_inputs[item_instance.name] = quantity
            else:
                required_raw_inputs[item_instance.name] += quantity
        else:
            # get recipe
            recipe = recipes[item_instance.recipes[0]]

            if recipe is not None:
                # get ingredients
                ingredients = recipe.ingredients
                # get quantity
                result_count = recipe.result_count
                # get number of times to craft
                num_crafts = quantity / result_count

                # print(f"Crafting {item_instance.name} {num_crafts} times")

                for ingredient_name, ingredient_quantity in ingredients:
                    if ingredient_name not in items_required.keys():
                        items_required[ingredient_name] = ingredient_quantity * num_crafts
                    else:
                        items_required[ingredient_name] += ingredient_quantity * num_crafts

    return required_raw_inputs


"""
Item(name="", type="item", stack_size=)
Recipe(name="", type="recipe", ingredients=["",1], result="")
"""

Resource(name="Copper Ore", type="item", stack_size=50)
Resource(name="Iron Ore", type="item", stack_size=50)
Resource(name="Stone Ore", type="item", stack_size=50)
Resource(name="Coal Ore", type="item", stack_size=50)

Item(name="Copper Plate", type="item", stack_size=100)
Recipe(name="Copper Smelting", type="recipe", ingredients=[("Copper Ore", 1)], result="Copper Plate")
Item(name="Iron Plate", type="item", stack_size=100)
Recipe(name="Iron Smelting", type="recipe", ingredients=[("Iron Ore", 1)], result="Iron Plate")
Item(name="Stone Brick", type="item", stack_size=200)
Recipe(name="Stone Smelting", type="recipe", ingredients=[("Stone Ore", 2)], result="Stone Brick")
Item(name="Steel Plate", type="item", stack_size=100)
Recipe(name="Steel Smelting", type="recipe", ingredients=[("Iron Ore", 5)], result="Steel Plate")

Item(name="Iron Gear Wheel", type="item", stack_size=50)
Recipe(name="Iron Gear Wheel", type="recipe", ingredients=[("Iron Plate", 2)], result="Iron Gear Wheel")

Item(name="Automation Science Pack", type="item", stack_size=200)
Recipe(name="Automation Science Pack", type="recipe",
       ingredients=[("Copper Plate", 1), ("Iron Gear Wheel", 1)], result="Automation Science Pack")

Item(name="Transport Belt", type="item", stack_size=100)
Recipe(name="Transport Belt", type="recipe", ingredients=[("Iron Plate", 1), ("Iron Gear Wheel", 1)],
       result="Transport Belt", result_count=2)

Item(name="Copper Cable", type="item", stack_size=200)
Recipe(name="Copper Cable", type="recipe", ingredients=[("Copper Plate", 1)], result="Copper Cable", result_count=2)

Item(name="Electronic Circuit", type="item", stack_size=200)
Recipe(name="Electronic Circuit", type="recipe", ingredients=[("Iron Plate", 1), ("Copper Cable", 3)],
       result="Electronic Circuit")

Item(name="Inserter", type="item", stack_size=50)
Recipe(name="Inserter", type="recipe", ingredients=[("Iron Plate", 1), ("Iron Gear Wheel", 1),
                                                    ("Electronic Circuit", 1)], result="Inserter")

Item(name="Logistic Science Pack", type="item", stack_size=200)
Recipe(name="Logistic Science Pack", type="recipe",
       ingredients=[("Transport Belt", 1), ("Inserter", 1)], result="Logistic Science Pack")

Item(name="Wall", type="item", stack_size=100)
Recipe(name="Wall", type="recipe", ingredients=[("Stone Brick", 5)], result="Wall")

Item(name="Firearm Magazine", type="item", stack_size=100)
Recipe(name="Firearm Magazine", type="recipe", ingredients=[("Iron Plate", 4)], result="Firearm Magazine")

Item(name="Piercing Rounds Magazine", type="item", stack_size=100)
Recipe(name="Piercing Rounds Magazine", type="recipe",
       ingredients=[("Firearm Magazine", 1), ("Copper Plate", 5), ("Steel Plate", 1)],
       result="Piercing Rounds Magazine")

Item(name="Grenade", type="item", stack_size=100)
Recipe(name="Grenade", type="recipe", ingredients=[("Iron Plate", 5), ("Coal Ore", 10)], result="Grenade")

Item(name="Military Science Pack", type="item", stack_size=200)
Recipe(name="Military Science Pack", type="recipe",
       ingredients=[("Piercing Rounds Magazine", 1), ("Grenade", 1), ("Wall", 2)],
       result="Military Science Pack", result_count=2)

# Example usage:
# required_inputs = get_inputs(desired_item="Military Science Pack", desired_quantity=36)
# required_raw_inputs = get_raw_inputs(desired_item="Military Science Pack", desired_quantity=36)
# print(required_inputs)
# print(required_raw_inputs)