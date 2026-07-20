from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='lorenz-attractor',
    version='1.0',
    description='Generates the Lorenz attractor and visualizes it using matplotlib',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Samy Alderson',
    author_email='samy.alderson@example.com',
    url='https://github.com/samyalderson/lorenz-attractor',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=['numpy', 'matplotlib', 'scipy'],
    extras_require={
        'dev': ['pytest', 'pytest-cov']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords='lorenz attractor matplotlib visualization'
)