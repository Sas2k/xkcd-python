import pathlib
from setuptools import setup
import xkcd_python

requirements = pathlib.Path("requirements.txt").read_text()
requirements = requirements.splitlines()

# Setting up
setup(
        name= "xkcd_python", 
        version= "3.3.0",
        author= xkcd_python.__author__,
        author_email= "sasen.learnings@gmail.com",
        description= xkcd_python.__shot_des__,
        long_description_content_type="text/markdown",
        long_description= open("README.md", "r", encoding="utf-8").read(),
        install_requires=requirements,
        
        keywords=['python', "python3"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"
        ]
)
