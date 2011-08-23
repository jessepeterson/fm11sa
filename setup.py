from setuptools import setup

setup(	name='fm11sa',
	version='0.1',
	description='SQLAlchemy FileMaker Pro & Server Advanced 11 plugin',
	packages=['fm11sa'],
	platforms='All',
	install_requires=[
		'sqlalchemy>=0.6',
		'pyodbc==2.1.7',
		],
	entry_points={
		'sqlalchemy.dialects': ['fm11 = fm11sa.fm11sa:dialect',]
		},
	)
