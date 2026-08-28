class Plant:
	def __init__(self, name: str, height: int) -> None:
		self.name: str = name
		self.height: int = height

	def grow(self, amount: int = 0) -> int:
		self.height += amount
		print(f"`{self.name} has grown {amount}cm")
		return amount

	@staticmethod
	def validade(height: int) -> bool:
		return height > 0

	def get_info(self) -> None:
		print(f"{self.name}: {self.height} cm.")


class FloweringPlant(Plant):
	def __init__(self, name: str, height: int, bloom: bool) -> None:
		super().__init__(name, height)
		self.bloom: bool = bloom

class PrizeFlower(FloweringPlant):
	def __init__(self, name: str, height: int, bloom: bool, value: int) -> None:
		super().__init__(name, height, bloom)
		self.value: int = value

class Garden:
	def __init__(self, name: str) -> None:
		self.name: str = name
		self.plants: list[Plant] = []

	def add_plant(self, plant: Plant) -> None:
		print(f"added {plant.name} to {self.name}")
		self.plants.append(plant)

class GardenManager:
	def __init__(self) -> None:
		self.gardens: list[Garden] = []
		self.stats: GardenManager.GardenStats = self.GardenStats(self)
		self.total_growth: int = 0
		self.total_plantss: int = 0

class GardenStats: 
	def __init__(self, manager: "GardenManager") -> None:
		self.manager: GardenManager = manager

	def count_plants(self) -> int:
		total: int = 0
		for garden in self.manager.gardens:
			total += len(garden.plants)
		return total

	def validate_all_heights(self) -> bool:
		for garden in self.manager.gardens:
			for plant in garden.plants:
				if not Plant.validade_heigth(plant.height):
					return False
		return True

	def garden_scores(self) -> None:
		scores: list[str] = []
		for garden in self.manager.gardens:
			total_score: int = 0

		for plant in garden.plants:
			if isinstance(plant, PrizeFlower):
				total_score += plant.value

		if "'" in garden.name:
			owner: str = garden.name.split("'")[0]
		else: 
			owner: str = garden.name
		scores.append(f"garden scores - {','.join(scores)}")

		def total_gardens(self) -> None:
			print(f"Total gardens managed: {len(self.manager.gardens)}")

		def count_by_type(self) -> None:
			r: int = 0
			f: int = 0
			p: int = 0

		for garden in self.manager.gardens:
			for plant in garden.plants:
				if isinstance(plant, PrizeFlower):
					p += 1
				elif isinstance(plant, FloweringPlant):
					f += 1
				else:
					r += 1
				print(f"Plants: {r} regular, {f} flowering, {p} prize flowers")

		def total_growth_and_plants(self) -> None:
			print(f"Plants added: {self.manager.total_plants},")
			print(f"Total growth: {self.manager.total_growth}cm")

		def add_garden(self, garden: Garden) -> None:
			self.gardens.append(garden)
			print(f"added {garden.name} to the network")

		def create_garden(self, name: str) -> Garden:
			new_garden: Garden = Garden(name)
			self.add_garden(new_garden)
			return new_garden

		def add_plant_in_garden(self, garden: Garden, plant_name: str, amout:  int) -> None:
			garden.add_plant(plant)
			self.total_plants += 1

		def grow_plant_in_garden(self, garden: Garden, plant_name: str, amount: int) -> None:
			for plant in garden.plants:
				if plant.name == plant_name:
					plant.grow(amount)
					self.total_growth += amount
					return
				print(f"Plant {plant_name} not found in {garden.name}")

		def generate_garden_report(self, garden: Garden) -> None:
			print(f"\n {garden.name} Report")
			print("Plants in garden:")
			for plant in garden.plants:
				info: str = f"- {plant.name}: {plant.height}cm"
			if isinstance(plant, FloweringPlant):
				if plant.bloom:
					info += " (blooming)"

			if isinstance(plant, PrizeFlower):
				info += f", Prize points: {plant.value}"
			print(info)

		@classmethod
		def create_garden_network(cls) -> "GardenManager":
			return cls()

def main() -> None:
	print("Garden Management System\n")
	manager: GardenManager = GardenManager.create_garden_network()

	garden1: Garden = manager.create_garden("Lis's garden")
	garden2: Garden = manager.create_garden("Math's garden")
	garden3: Garden = manager.create_garden("Anne's garden")
	garden4: Garden = manager.create_garden("Elo's garden")
	garden5: Garden = manager.create_garden("Ra's garden")
	print()

	manager.add_plant_to_garden(
		garden1,
		Plant("   ", 30))
	manager.add_plant_to_garden(
		garden1,
		FloweringPlant("   ", 25, True))
	manager.add_plant_to_garden(
		garden1,
		PrizeFlower("   ", 50, True, 10))
	print()

	manager.add_plant_to_garden(
			garden2,
			Plant("   ", 30))
	manager.add_plant_to_garden(
			garden2,
			FloweringPlant("   ", 25, True))
	manager.add_plant_to_garden(
			garden2,
			PrizeFlower("   ", 50, True, 10))
	print()

	manager.add_plant_to_garden(
			garden3,
			Plant("   ", 30))
	manager.add_plant_to_garden(
			garden3,
			FloweringPlant("   ", 25, True))
	manager.add_plant_to_garden(
			garden3,
			PrizeFlower("   ", 50, True, 10))
	print()

	manager.add_plant_to_garden(
				garden4,
				Plant("   ", 30))
	manager.add_plant_to_garden(
				garden4,
				FloweringPlant("   ", 25, True))
	manager.add_plant_to_garden(
				garden4,
				PrizeFlower("   ", 50, True, 10))
	print()

	manager.add_plant_to_garden(
				garden5,
				Plant("   ", 30))
	manager.add_plant_to_garden(
				garden5,
				FloweringPlant("   ", 25, True))
	manager.add_plant_to_garden(
				garden5,
				PrizeFlower("   ", 50, True, 10))
	print()

	print("\n is helping all plants grow...")
	manager.grow_plant_in_garden(garden1, "Oak Tree", 1)
	manager.grow_plant_in_garden(garden1, "Rose", 1)
	manager.grow_plant_in_garden(garden1, "Sunflower", 1)

	# Generate garden reports
	manager.generate_garden_report(garden1)
	manager.generate_garden_report(garden2)

	# Display statistics
	print()
	manager.stats.total_growth_and_plants()
	manager.stats.count_by_type()
	print(f"\nHeight validation test: {manager.stats.validate_all_heights()}")
	manager.stats.garden_scores()
	manager.stats.total_gardens()


if __name__ == "__main__":
	main()