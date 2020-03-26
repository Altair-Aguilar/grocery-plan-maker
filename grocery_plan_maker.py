##################################################################################################
#WHEN ADDING A NEW MEAL: 
#A. ADD TO EITHER meals OR friday_meals, depending on which it is
#B. IF IT REQUIRES A SIDE, ADD TO meals_that_need_sides
#C. ADD TO ingredients_dic ALONG WITH THE CORRESPONDING INGREDIENTS
#WHEN ADDING A NEW SIDE: 
#A. ADD TO sides
#C. ADD TO ingredients_dic ALONG WITH THE CORRESPONDING INGREDIENTS

#Needed for .shuffle() method to randomize meal choices
import random

#Meal lists for create_meal_plan
meals = [
"Lasagna", "Spaghetti", "Chicken Fettuccine", "American Goulash", 
"Mostaccioli", 'Burger', "Brats", "Cuban", "Banh Mi"
]
friday_meals = [
"Fish"
]
meals_that_need_sides =[
'Burger', "Brats", "Cuban", "Banh Mi"
]
sides = [
'test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6'
] 
#To be returned by create_meal_plan and create_lists
this_weeks_meals = []

this_weeks_list = []
###################################################################
#List elements for organize_lists, current list elements are used by organize_lists-
#so that the grocery list is organized by the layout of the store
##########ALDI############
aldi_produce = [
'iceberg lettuce', 'green peppers', 'tomato', 'garlic', 'apples', 'brussel sprouts', 'grapes', 'plums', 'oranges', 
'clementines', 'carrots', 'cabbage', 'broccoli', 'green onions', 'cilantro', 'bell peppers', 'celery', 'red onions',
]
aldi_bready = ['side ingredient', 'burger bun']
aldi_deli = ['mozzarella', 'monterrey jack', 'cheddar', 'swiss', 'brats', 'ground beef']
aldi_cereal = []
aldi_condiments = []
aldi_paper = ['paper plates', 'paper towels', 'napkins', 'ziploc bags']
aldi_dairy = ['milk', 'hwc', 'half and half', 'butter', 'cream cheese', 'sour cream']
aldi_frozen = []
current_aldi_produce = []
current_aldi_bready = []
current_aldi_deli = []
current_aldi_cereal = []
current_aldi_condiments = []
current_aldi_paper = []
current_aldi_dairy = []
current_aldi_frozen = []

###############COSTCO##############
pass
###############COSTCO##############
#For assorted items that do not (or have not yet been added) fit into any other categories
end_of_list = []

#List of aldi and costco (N/A) organization lists
aldi_aisles_list = [
aldi_produce, aldi_bready, aldi_deli, aldi_cereal, aldi_condiments, aldi_paper, aldi_dairy, aldi_frozen
]

aldi_aisles_list_current = [
current_aldi_produce, current_aldi_bready, current_aldi_deli, current_aldi_cereal,
current_aldi_condiments, current_aldi_paper, current_aldi_dairy, current_aldi_frozen
]

################################################################################
#Ingredients required for each meal
ingredients_dic = {
"Lasagna" : ['iceberg lettuce'],
"Spaghetti" : ['iceberg lettuce'],
"Chicken Fettuccine" : ['iceberg lettuce'],
"American Goulash" : ['iceberg lettuce'],
"Mostaccioli" : ['iceberg lettuce'],
'Burger' : ['ground beef', 'iceberg lettuce', 'tomato', 'burger bun'],
'Brats' : ['iceberg lettuce'],
'Cuban' : ['iceberg lettuce'],
"Banh Mi" : ['iceberg lettuce'],
"Fish" : ['iceberg lettuce'],
'test 1' :['side ingredient'],
'test 2':['side ingredient'],
'test 3':['side ingredient'],
'test 4':['side ingredient'],
'test 5':['side ingredient'],
'test 6':['side ingredient']
}
################################################################################
#Chooses 6 random meals from meals and 1 from friday_meals and appends to this_weeks_meals


def create_meal_plan():
	random.shuffle(meals)
	random.shuffle(friday_meals)
	random.shuffle(sides)
	for x in range(6):
		random.shuffle(sides)
		meal_append = meals.pop()
		if meal_append in meals_that_need_sides:
			for x in range(2):
				random.shuffle(sides)
				side_append = sides.pop()
				sides.append(side_append)
				this_weeks_meals.append(side_append)
		this_weeks_meals.append(meal_append)
	friday_meal_append = friday_meals.pop()
	this_weeks_meals.append(friday_meal_append)
	return (this_weeks_meals)

#Takes the ingredients from ingredients_dic required for each meal from this_weeks_meals and appends to this_weeks_list
def create_lists():
	for meal in this_weeks_meals:
		ingredients = ingredients_dic[meal]
		for ingredient in ingredients:
			this_weeks_list.append(ingredient)
	return this_weeks_list

#Organizes this_weeks_list using the lists in #aldi_aisles_list and Costco(N/A)
def organize_lists(unorganized_list):
	organized_lists = []
	aisle_counter = 0
	edited_list = []
	for item in unorganized_list:
		edited_list.append(item)
	for aisle in aldi_aisles_list:
		for item in unorganized_list:
			if item in aisle:
				edited_list.remove(item)
				aldi_aisles_list_current[aisle_counter].append(item)
		aisle_counter += 1
	
	for x in aldi_aisles_list_current:
		if x != []:
			organized_lists.append(x)
	
	for x in edited_list:
		organized_lists.append(x)
	return organized_lists

print(create_meal_plan())
print(organize_lists(create_lists()))
