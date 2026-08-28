class Plant:
	def __int__(self, name: str, heigth: int, plant_age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.plant_age: int = plant_age

	def grow(self) -> None:
		self.height += 5

	def age(self) -> None:
		self.plan_age += 1

	def get_info(self) -> None:
		print(f"{self.name}: {self.height} cm, {self.plant_age} days old")

def main () -> None:
	plant1: Plant = Plant("rose", 1, 4)
	plant2: Plant = Plant("cosmos", 40, 12)
	plant3: Plant = Plant("bouganvile", 100, 25)
	count: int = 0

	plants: list[Plant] = [plant1, plant2, plant3]
	print(" Day 1 ")
	for plant in plants:
		plant.get_info()

	for i in range(1, 8):
		for plant in plants:
			plant.grow()
			plant.age()
			count += 5

	print("\n day 7")
	for plant in plants:
		plant.get_info()
	print(f"\n Growth this week: {count}")

if __name__ "__main__":
	main()