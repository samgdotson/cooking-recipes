

recipes = {
"chicken tonkatsu" : ["chicken breast",
"egg",
"Dijon mustard",
"water",
"panko",
"vegetable oil",
"napa cabbage",
"yellow onion",
"soy sauce",
"portobello mushrooms",
"pickled ginger"], 
"flat iron steak" : ["flat iron steak",
"black pepper",
"green beans",
"hoisin sauce",
"soy sauce", 
"rice vinegar",
"toasted sesame oil",
"chili garlic sauce",
"olive oil",
"sesame seeds"],
"balsamic braised chicken thighs" : ["chicken thigh",
"black pepper",
"bacon",
"butter",
"red onion",
"garlic",
"dried figs",
"chicken broth",
"balsamic vinegar",
"polenta"], 
"pad thai" : ["rice noodles",
"tamarind",
"brown sugar",
"honey",
"fish sauce",
"rice vinegar",
"vegetable oil",
"pepper flakes",
"green onion",
"garlic",
"egg",
"napa cabbage",
"shrimp",
"bean sprouts",
"peanuts",
"lime",
"salt"], 
"spicy pork stir fry" : ["lime juice",
"soy sauce", 
"sesame oil",
"cornstarch", 
"honey", 
"chili garlic sauce", 
"pork tenderloin",
"salt",
"lo mein noodles",
"vegetable oil",
"fresh ginger",
"garlic",
"red bell pepper",
"snow peas",
"green onion", 
"cashews"]
}

inventory = ["cornstarch", 
"toasted sesame oil",
"sesame oil",
"rice vinegar",
"soy sauce",
"green beans",
"flour",
]


def number_ingredients(recipe):
	"""
	Returns the total number of ingredients in a recipe.

	Parameters:
	-----------
	recipe : string
		The name of the recipe. A key in the dictionary
		``recipes``.

	Returns:
	--------
	Inline, the number of ingredients in the recipe
	"""
	recipe = recipe.lower()
	return (len(recipes[recipe]))

print(number_ingredients("Chicken Tonkatsu"))

def match_recipe(ingredients):
	"""
	Returns a list of possible recipes given the a list
	of ingredients that you want to use, or have on hand.

	Parameters:
	-----------
	ingredients : list, string

	Returns: 
	recipes : list, string
	"""

	possible = []

	for recipe in recipes:
		total = 0
		for ingredient in ingredients:
			if ingredient in recipes:
				print("yes")
				total = total + 1
				print(recipe)

match_recipe("soy sauce")






