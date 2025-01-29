####
# MIT License
# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
####

import setuptools

INSTALL_REQUIRES = [
    "numpy>=1.24.4",
    "matplotlib>=3.0.0"
]

EXTRAS_REQUIRE = {    
    "utilities": ["fire>=0.4.0", "tqdm>=4.59.0", "plotly>=4.11.0"],
}


setuptools.setup(
    name="figureout",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=["tests", "scripts"]),
    url="https://github.com/MicheleBarsotti/figurout",
    license="Public",
    author="mbarsotti",
    author_email="",
    description="Internal algorithm repository of Henesis",
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.8,<3.9",
    extras_require=EXTRAS_REQUIRE,
)

