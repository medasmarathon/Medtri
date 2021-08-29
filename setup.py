import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="medtri",
    version="0.0.1",
    author="Duc Dang",
    author_email="vinhduc91@outlook.com",
    description="Medical events library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medasmarathon/Medtri",
    project_urls={
        "Bug Tracker": "https://github.com/medasmarathon/Medtri/issues",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    package_dir={"": "medtri"},
    packages=setuptools.find_packages(where="medtri"),
    python_requires=">=3.6",
    )