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
]

EXTRAS_REQUIRE = {
    "machine_learning": [
        "scikit-learn>=0.23.2",
        "torch>=1.11,<1.13",
        "torchvision>=0.12.0",
        "torchaudio>=0.7.0",
        "einops>=0.3.0",
        "pyyaml>=5.4.1",
    ],
    "signal_processing": ["scipy>=1.5.0"],
    "testing": ["more-itertools>=8.7.0", "pytest>=6.2.2", "pytest-mock>=3.5.1"],
    "eeg": ["mne>=1.0.2", "scipy>=1.5.0", "pyxdf>=1.16.3", "mnelab>=0.6.3"],
    "classification": [
        "scikit-learn>=0.23.2",
        "pyriemann>=0.2.6",
        "torch>=1.11,<1.13",
        "einops>=0.3.0",
        "pyyaml>=5.4.1",
        "sktime>=0.6.1",
        "Braindecode==0.4.85",
    ],
    "utilities": ["fire>=0.4.0", "tqdm>=4.59.0", "plotly>=4.11.0"],
}
EXTRAS_REQUIRE["development"] = list(set(sum(EXTRAS_REQUIRE.values(), [])))

EXTRAS_REQUIRE["demo"] = EXTRAS_REQUIRE["classification"] + EXTRAS_REQUIRE["signal_processing"]

_BAD_REQS = ("mne", "mnelab", "Braindecode", "pyxdf")
EXTRAS_REQUIRE["dev_lite"] = [
    req for req in EXTRAS_REQUIRE["development"] if not req.startswith(_BAD_REQS)
]


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

