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
		"""Initialize a flowering plant with name, height, and bloom status"""
		super().__init__(name, height)
		self.bloom: bool = bloom