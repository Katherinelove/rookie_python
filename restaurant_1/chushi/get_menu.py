class Ingredient():
    def __init__(self,title,description=""):
        self.title=title
        self.description=description


class Recipe():
    def __init__(self,title,ingredients=[],directions=[],note=""):
        self.title=title
        self.ingredients=ingredients
        self.directions=directions
        self.note=note
    def print_recipe(self):
        print(self.title)
        print("Ingredients")
        for ingredient in self.ingredients:
            print(ingredient.title)
        print("Directions")
        n=1
        for direction in self.directions:
            print(str(n)+"-"+direction)
            n+=1
        if self.note:
            print("special note:")
            print(self.note )
i=Ingredient(title="eggs")
r=Recipe(title="Scrambled eggs",
         ingredients=[i],
         directions=["break egg","beat egg","cook egg",],
         note="loveyou")
r.print_recipe()