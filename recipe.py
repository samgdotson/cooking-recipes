import numpy as np 


class recipe(object):
	"""
	A recipe class that contains all the information you would want to know for a recipe. 

	Parameters:
	-----------
	name : string
		The name of the recipe. 
	ingredients : list of strings
		A list of ingredients used in a recipe. Current implementation includes an amount

	directions : string
		A string containing the path to an html file or text file with the directions to the 
		recipe in them. 

	**kwargs : dictionary of optional values:
		Currently accepts: 
		'special' : string or list of strings
			Identifies what special diets this recipe satisfies. Ex. 'keto', 'vegan', 'paleo'
		'time' : float
			How long it takes to make the recipe from start to finish (in minutes). Approximately. 

	"""
	def __init__(self, name, ingredients, directions=None, **kwargs):
		super(recipe, self).__init__()
		self.name = name
		self.ingredients = ingredients
		self.directions = directions
		
		if 'time' in kwargs.keys():
			self.prep_time = time

		if 'special' in kwargs.keys():
			self.special = special


	def add_ingredient(self, ingredient):
		"""
		Adds an ingredient to the list of ingredients.

		Parameters:
		-----------
		ingredient : string
		"""
		self.ingredients.append(ingredients) #ingredients must be a list in order to have the method `append`. 
		return

	def num_ingredients(self):
		"""
		Returns:
		-------- 
		int : the number of ingredients used in a recipe.
		"""
		return len(self.ingredients)

	def add_directions(self, path):
		"""
		Adds directions to the recipe.

		Parameters:
		-----------
		path : string
			The path to the file containing the directions. 
		"""
		self.directions = directions
		return

	def add_step(self, step):
		"""
		Adds a step to the directions.

		Parameters: 
		-----------
		step : string
			This is the string that will be written to the directions file. 
		"""
		#opens the file with the directions
		file = open(self.directions)

		#write to the file
		file.write('\n')
		file.write(step)
		file.close()

		return

	def check_vegan(self):
		"""
		Checks if the recipe is vegan. 

		Returns
		-------
		boolean : True for vegan, False if not.
		"""

		for ingredient in self.ingredients:
			if ingredient not in vegan_ingredients:
				return False

		return True

