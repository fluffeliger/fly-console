from setuptools import find_packages, setup

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='flyconsole',
    version='1.0',
    description='Manipulate the Terminal in all different ways',
    package_dir={'': '.'},
    packages=find_packages(where='.'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fluffeliger/fly-console',
    author='fluffeliger',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"
)