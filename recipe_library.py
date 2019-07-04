import recipe as rp 

recipes = {
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

def add_recipe(name, ingredients):
	new_recipe = rp.recipe(name, ingredients)
	cookbook.append(new_recipe)
	return

ls_ing =  ["chicken breast",
"egg",
"Dijon mustard",
"water",
"panko",
"vegetable oil",
"napa cabbage",
"yellow onion",
"soy sauce",
"portobello mushrooms",
"pickled ginger"]
chkn_tonk = rp.recipe("chicken tonkatsu", ls_ing)

print(chkn_tonk.name)





