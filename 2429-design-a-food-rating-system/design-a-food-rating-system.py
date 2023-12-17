from sortedcontainers import SortedSet
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_ratings = {}
        self.food_cuisines = {}
        self.cuisine_food_set = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i]
            self.food_cuisines[foods[i]] = cuisines[i]
            self.cuisine_food_set[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food, new_rating):
        cuisine_name = self.food_cuisines[food]
        old_element = (-self.food_ratings[food], food)
        self.cuisine_food_set[cuisine_name].remove(old_element)
        self.food_ratings[food] = new_rating
        self.cuisine_food_set[cuisine_name].add((-new_rating, food))

    def highestRated(self, cuisine):
        highest_rated_food = self.cuisine_food_set[cuisine][0]
        return highest_rated_food[1]
