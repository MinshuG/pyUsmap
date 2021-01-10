from setuptools import setup
import pathlib


HERE = pathlib.Path(__file__).parent


README = (HERE / "README.md").read_text()


setup(
    name="pyUsmap",
    version="1.1.0",
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