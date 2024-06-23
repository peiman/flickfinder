from setuptools import setup, find_packages

setup(
    name='flickfinder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'click',
        'rich',
        'python-dotenv'
    ],
    package_data={
        'flickfinder': ['config.ini'],
    },
    entry_points={
        'console_scripts': [
            'flickfinder=flickfinder.cli:cli',
        ],
    },
    author='Peiman Khorramshahi',
    author_email='peiman@khorramshahi.com',
    description='A CLI tool to fetch IMDb ratings and search for movies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/peiman/flickfinder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
