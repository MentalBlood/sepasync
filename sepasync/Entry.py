import os
import dataclasses
from loguru import logger
from bs4 import BeautifulSoup

from .Path import Path
from .Content import Content
from .FileName import FileName
from .Container import Container



@dataclasses.dataclass(frozen=True)
class Entry(Container):

	content: Content
	name: str | None = None

	@staticmethod
	def composePath(path, name):
		return os.path.abspath(
			Path(path, [FileName(f'{name}.htm')])
		)

	async def inside(self, path):

		name = self.name
		file_path = Entry.composePath(path, name)

		if not (name is None):
			if os.path.exists(file_path):
				return

		root = BeautifulSoup(await self.content(), 'html.parser')

		text_node = root.find(
			'div',
			{'id': 'aueditable'},
		)
		if text_node is None:

			try:
				yield Entry(
					Content(
						filter(
							lambda n: 'http' in n.text,
							root.find(
								'div', {'class': 'notice'}
							).find_all(
								'a'
							)
						).__next__().text
					),
					self.name
				)
			except:
				...

			return

		if name is None:
			name = text_node.find('h1').text
			if Entry.saved(path, name):
				return

		for i in [
			'other-internet-resources',
			'related-entries',
			'academic-tools',
		]:

			node_to_remove = text_node.find('div', {'id': i})

			try:
				href = node_to_remove.find('h2').attrs['id']
				text_node.find('a', {'href': f'#{href}'}).parent.decompose()
			except:
				...

			node_to_remove.decompose()

		try:
			text_node.find('div', {'id': 'acknowledgments'}).decompose()
		except:
			...

		text = text_node.__str__()

		os.makedirs(path, exist_ok=True)
		with open(file_path, 'w', encoding='utf8') as f:
			f.write(text)

		logger.success(file_path)

		return