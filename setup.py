import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvtkpy",
    version="0.0.1",
    author="Vince Buffalo",
    author_email="vsbuffalo@gmail.com",
    description="A package to compute temporal covariances, for the analyses of Buffalo and Coop (2020).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vsbuffalo/cvtkpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'scipy',
        'panda',
        'tqdm',
        'matplotlib',
        'statsmodels',
        'scikit-allel',
        'sklearn'
    ],
    python_requires='>=3.6',
)
