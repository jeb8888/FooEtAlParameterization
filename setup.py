from setuptools import setup, find_packages

setup(
    name="foo_param",
    version="1.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'foo_param=foo_param.cli:main',
        ],
    },
    author="Foo et al.",
    author_email="authors@foo.com",
    description="Foo et al. Parameterization Package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jeb8888/FooEtAlParameterization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
