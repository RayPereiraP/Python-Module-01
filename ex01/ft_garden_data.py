class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.age: int = age

	def main() -> None:
		plant1: Plant = Plant("rose", 1, 5)
		plant2: Plant = ("cosmos", 40, 12)
		plant3: Plant = Plant("black bat", 100, 30)
		print(f"{plant1.name}: {plant1.height} heigth, {plant1.age} days old")
		print(f"{plant2.name}: {plant2.height} heigth, {plant2.age} days old")
		print(f"{plant3.name}: {plant3.height} heigth, {plant3.age} days old")

if __name__ == "__main__":
	main()