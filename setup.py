import sys
from setuptools import setup, find_packages


# # check python version
# if sys.version_info < (3, 5, 4):
#     sys.exit('Python < 3.5.4 is not supported.')

setup(
    name='nest',
    version='0.1.1',
    description='Nest - A flexible tool for building and sharing deep learning modules',
    url='https://github.com/lzd0825/Nest',
    author='Zhou, Yanzhao',
    author_email='yzhou.work@outlook.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyYAML',
        'python-dateutil'
    ],
    entry_points={
        'console_scripts': ['nest=nest.__main__:main'],
    },
)
