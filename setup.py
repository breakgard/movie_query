from setuptools import setup

setup(
    name='movie_query',
    version='0.1',
    packages=['movie_query'],
    install_requires=[
      'click==8.0.1',
      'requests==2.25.1',
      'validators==0.18.2'],
    entry_points='''
        [console_scripts]
        movie_query=movie_query.main:main
    ''',
)
