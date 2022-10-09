from setuptools import setup, find_packages


if __name__ == '__main__':

	setup(
		name='sepasync',
		version='1.3.2',
		description='Fast, working tool for downloading entries from SEP',
		long_description=open('README.md').read(),
		long_description_content_type='text/markdown',
		author='mentalblood',
		install_requires=[
			'bs4',
			'loguru',
			'httpx',
			'python_version >= "3.10"'
		],
		packages=find_packages()
	)
