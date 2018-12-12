import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_analysis",
    version="0.0.1",
    author="Paulo Arevalo",
    author_email="parevalo@bu.edu",
    description="Test example package from AGU 2018 workshop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parevalo/2018-agu-workshop",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
