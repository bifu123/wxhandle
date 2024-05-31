from setuptools import setup, find_packages

setup(
    name="wxhandler",
    version="0.1.1.5.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="chenbifu",
    author_email="pythonaaa@gmail.com",
    description="A Python package for handling wxHandler operations.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chenbifu/wxhandler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
