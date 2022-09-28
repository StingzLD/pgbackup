from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Corey Hastings',
    author_email='stingzlightingdesign@hotmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/StingzLD/pgbackup',
    packages=find_packages('1'),
    package_dir={'': '1'},
    install_requires=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ],
    }
)
