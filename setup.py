from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'CLSZ algorithm for clustering directed graphs.'
LONG_DESCRIPTION =\
    "The CLSZ algorithm for applying spectral clustering to hermitian adjacency matrices of directed graphs"

# Setting up
setup(
    name="clsz",
    version=VERSION,
    author="Peter Macgregor",
    author_email="<macgregor.pr@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["numpy", "scipy", "sklearn", "networkx"],

    keywords=['python', 'clsz', 'directed graph', 'clustering', 'spectral clustering', 'hermitian'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Operating System :: POSIX :: Linux'
    ]
)