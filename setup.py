import pathlib
from setuptools import setup
import xkcd_python

requirements = pathlib.Path("requirements.txt").read_text()
requirements = requirements.splitlines()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name= "xkcd_python", 
        version= "3.2.0",
        author= xkcd_python.__author__,
        author_email= "sasen.learnings@gmail.com",
        description= xkcd_python.__shot_des__,
        long_description= xkcd_python.__description__,
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
