from setuptools import setup

setup(
    name="movie_query",
    version="1.0.0",
    packages=["movie_query"],
    author="Pawel Wysokinski",
    author_email="work@pawelwysokinski.pl",
    description="Example app for querying a rest API",
    license="MIT",
    keywords="example demo movie",
    install_requires=["click==8.0.1", "requests==2.25.1", "validators==0.18.2"],
    extras_require={
        "dev": [
            "pylint==2.9.0",
            "pytest==6.2.4",
            "requests-mock==1.9.3",
            "black==21.6b0",
            "setuptools==57.0.0",
        ]
    },
    entry_points="""
        [console_scripts]
        movie_query=movie_query.main:main
    """,
)
