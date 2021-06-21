from setuptools import setup
import pathlib
from Usmap import __version__

HERE = pathlib.Path(__file__).parent


README = (HERE / "README.md").read_text()


setup(
    name="pyUsmap",
    version=__version__,
    description=".usmap file reader",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MinshuG/pyUsmap",
    author="MinshuG",
    classifiers=[       
        "Programming Language :: Python :: 3",
    ],
    install_requires=["Brotli"],
    packages=["Usmap", "Usmap/Objects"],
)
