class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.age: int = age

	def get_height(self) -> int:
		return self.height

	def get_age(self) -> int:
		return self.age

	def get_info(self) -> None:
		pass

class Flower(Plant):
	def __init__(self, name: str, height: int, age: int, color: str) -> None:
		super().__init__(name, height, age)
		self.color: str = color

	def bloom(self) -> None:
		print(f"{self.color} {self.name} is bloominggggg!")

	def get_into(self) -> None:
		print(f"{self.name.capitalize()} (Flower): {self.get_heigth()} cm, "
		f"{self.get_age()} days, {self.color} color")

class Tree(Plant):
	def __init__(self, name: str, height: int, age: int, diameter: int) -> None:
		super().__init__(name, height, age)
		self.diameter: int = diameter

	def produce_shade(self) -> None:
		print(f"{self.name} with {self.diameter} has produced shade")

	def get_info(self) -> None:
		print(f"{self.name.capitalize()} (Tree): {self.get_height()} cm, "
		f"{self.get_age()} days, {self._diameter} cm diameter")

class Vegetable(Plant):
	def __init__(self, name: str, height: int, age: int, harvest_season: str, nutri_value: str) -> None:
			super().__init__(name, height, age)
			self.harvest_season: str = harvest_season
			self.nutritional_value: str = nutri_value

	def get_info(self) -> None:
		print(f"{self.name.capitalize()} (Vegetable): {self.get_height()} cm, "
				f"{self.get_age()} days, {self.harvest_season},\n"
				f"{self.name.capitalize()} is rich in {self.nutritional_value}")

def main() -> None:
	print("Garden plant typesss")

	flower_data: list[tuple[str, int, int, str]] = [
		("rose", 1, 5, "red"),
		#colocar mais aqui
	]

	tree_data: list[tuple[str, int, int, str]] = [
		("oak", 800, 4000, 30),
		#colocar mais aqui
	]

	vegetable_data: list[tuple[str, int, int, str, str]] = [
		("tomato", 50, 80, "summer", "vitamin c"),
		#colocar mais aqui
	]
	plants: list[Plant] = []

	for name, height, age, color in flower_data:
		plant: Flower = Flower(name, height, age, color)
		plants.append(plant)

	for name, height, age, diameter in tree_data:
		plant: Tree = Tree(name, height, age, diameter)
		plants.append(plant)

	for name, height, age, harvest_season, nutri_value in vegetable_data:
		plant: Vegetable = Vegetable(name, height, age, harvest_season, nutri_value)
		plants.append(plant)

	for plant in plants:
		plant.get_info()
		if isinstance(plant, Flower):
			plant.bloom()
		elif isinstance(plant, Tree):
			plant.produce_shade()
		print() if plant != plants[-1] else None

if __name__ == "__main__":
	main()