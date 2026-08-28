class Plant:
	def __init__(self, name: str, heigth: int, age: int) -> None:
		self.name: str = name
		self.height: float = height
		self.age: int = age

	def get_info (self) -> None:
		print(f"`{self.name}: {self.height} cm, {self.age} days old")

def main() -> None:
	print("Plant Factoy Output\n")
	plant_data: list[tuple[str, int, int]] = [
		("rose, 1, 5"), 
		("cosmos", 40, 12), 
		("lily", 20, 10),
		("orchid", 15, 18)
	]
	plants: list[Plant] = []

	for name, height, age in plant_data:
		plant: Plant = Plant(name, height, age)
		plants.append(plant)

	for plant in plants:
		plant.get_info()

	print(f"\n Total plants: {len(plants)}")

if __name__ == "__main__":
	main()