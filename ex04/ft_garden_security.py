class SecurePlant:
	def __init__(self, name: str) -> None:
		self.name: str = name
		self._height: int = 0
		self._age: int = 0

	def set_heigth(self, height: int) -> None:
		if int(height) > 0:
			self._height = height
			print(f"Height updated: {height} [OK]")
		else:
			print(f"Invalid operation attempted: height {height} [REJECTED]")
			print("Security: Negative height rejected")

	def set_age(self, age: int) -> None:
		if int(age) > 0:
			self._age = age
			print(f"Age updated: {age} [OK]")
		else: 
			print(f"Invalid operation attemped: age {age} [REJECTED]")
			print("Security: Negative age rejected")

	def get_heigth(self) -> int:
		return self._height

	def get_age(self) -> int:
		return self._age

	def get_info(self) -> None:
		print(f"Current plant: {self.name}"
		f"({self.get_heigth()} cm, {self.get_age()} days)")

def main() -> None:
	print("Garden Security System\n")

	plants: list[SecurePlant] = []

	for name, height, age in plant_data:
		plant: SecurePlant = SecurePlant(name)
		print(f"Plant created: {plant.name}")
		plant.set_height(height)
		plant.set_age(age)
		print("\n")
		plants.append(plant)

	for plant in plants:
		plant.get_info()

	print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
	main()