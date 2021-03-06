from setuptools import setup

with open('yeelightbt/version.py') as f: exec(f.read())

setup(
    name='yeelightbt',

    version=__version__,
    description='Python library for interfacing with yeelight\'s bt lights',
    url='https://github.com/hcoohb/python-yeelightbt',

    author='Teemu Rytilahti - Fabien Valthier',
    author_email='tpr@iki.fi',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],

    keywords='yeelight bluepy',

    packages=["yeelightbt"],

    python_requires='>=3.4',
    install_requires=['bluepy', 'click'],
    entry_points={
        'console_scripts': [
            'yeelightbt=yeelightbt.cli:cli',
        ],
    },
)
