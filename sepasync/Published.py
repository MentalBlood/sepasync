import dataclasses
from bs4 import BeautifulSoup, Tag

from .Entry import Entry
from .Content import Content
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Published(Container):

	page: Content

	async def inside(self, *args, **kwargs):

		text = await self.page()
		entries_list = BeautifulSoup(text, features='lxml').find(
			'div', {'id': 'content'}
		).find(
			'ul'
		)

		for c in entries_list:
			if isinstance(c, Tag):

				href_node = c.find('a')

				yield Entry(
					content=Content(
						href_node.attrs['href']
					),
					name=href_node.find('strong').text
				)