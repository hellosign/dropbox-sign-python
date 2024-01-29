"""
    Dropbox Sign API

    Dropbox Sign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path

NAME = "dropbox-sign"
VERSION = "1.3.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Dropbox Sign API",
    author="Dropbox Sign API Team",
    author_email="apisupport@hellosign.com",
    url="https://github.com/hellosign/dropbox-sign-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Dropbox Sign API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
