from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Efficient and scalable documentations'
LONG_DESCRIPTION = 'A package to create scalable descriptions'

setup(
    name="lib-handbook",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Raphaël Candelier",
    author_email="raphael.candelier@sorbonne-universite.fr",
    license='GNU GPL v3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy'],
    keywords='conversion',
    classifiers= [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
    ]
)
