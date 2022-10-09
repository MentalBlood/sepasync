import dataclasses

from .Entry import Entry
from .Published import Published
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class SEPPage(Container):

	url: str

	async def inside(self, *args, **kwargs):

		splited = self.url.split('/')

		result_factory = None

		if 'entries' in splited:
			result_factory = Entry
		elif 'published.html' in splited:
			result_factory = Published

		yield result_factory(Content(self.url))