import dataclasses

from .SEPPage import SEPPage
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Task(Container):

	urls: list[str]

	async def inside(self, *args, **kwargs):
		for u in self.urls:
			yield SEPPage(u)