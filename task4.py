import random
flowers = ("гортензия", "тюльпанчик", "роза", "лилия", "пиончик")
colors = ("красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый")
bouquet = dict(zip(flowers,[random.choice(colors) for i in flowers]))
print(bouquet)