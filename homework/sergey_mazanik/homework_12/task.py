class Flowers:
    def __init__(self, freshness: int, color: str, stem_length: int, cost: float):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost


class Rose(Flowers):
    def __init__(self, freshness: int, color: str, stem_length: int, cost: float, name: str = 'Rose'):
        super().__init__(freshness, color, stem_length, cost)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Chamomile(Flowers):
    def __init__(self, freshness: int, color: str, stem_length: int, cost: float, name: str = 'Chamomile'):
        super().__init__(freshness, color, stem_length, cost)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Peony(Flowers):
    def __init__(self, freshness: int, color: str, stem_length: int, cost: float, name: str = 'Peony'):
        super().__init__(freshness, color, stem_length, cost)
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Bouquet(Flowers):
    def __init__(self, flowers: list):
        self.flowers = flowers

    def cost_of_bouquet(self):
        cost_of_bouquet = 0
        for flower in self.flowers:
            cost_of_bouquet += flower.cost
        return cost_of_bouquet

    def lifetime_of_bouquet(self):
        avg_lifetime = 0
        for flower in self.flowers:
            avg_lifetime += flower.freshness
        return round(avg_lifetime / len(self.flowers))

    def sorted_by_parameter(self, parameter: str):
        sorted_bouquet = sorted(self.flowers, key=lambda x: getattr(x, parameter))
        return [flower.name for flower in sorted_bouquet]

    def found_flower_by_parameter(self, parameter: str, value: str | int):
        found_flower = [flower for flower in self.flowers if getattr(flower, parameter) == value]
        return [flower.name for flower in found_flower]


rose = Rose(7, 'red', 50, 10)
chamomile = Chamomile(15, 'white', 10, 1)
peony = Peony(10, 'pink', 25, 15)
bouquet = Bouquet([rose, chamomile, peony])

print(bouquet.cost_of_bouquet())
print(bouquet.lifetime_of_bouquet())
print(bouquet.sorted_by_parameter('freshness'))
print(bouquet.sorted_by_parameter('color'))
print(bouquet.sorted_by_parameter('stem_length'))
print(bouquet.sorted_by_parameter('cost'))
print(bouquet.found_flower_by_parameter('color', 'red'))
print(bouquet.found_flower_by_parameter('cost', 15))
