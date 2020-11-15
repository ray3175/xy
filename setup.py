import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("xy/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with io.open("xy/__init__.py", "rt", encoding="utf8") as f:
    author = re.search(r'__author__ = "(.*?)"', f.read()).group(1)

with io.open("xy/__init__.py", "rt", encoding="utf8") as f:
    author_email = re.search(r'__author_email__ = "(.*?)"', f.read()).group(1)

setup(
    name="xy",
    version=version,
    url="https://github.com/ray3175/xy",
    license="BSD",
    author=author,
    author_email=author_email,
    description="个人封装的一些类库！",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    python_requires=">=3.9.*",
    install_requires=[]
)
