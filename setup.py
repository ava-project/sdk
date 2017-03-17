from setuptools import setup, find_packages

import sdk

keywords = [
    'ava', 'sdk',
]

setup(
    name='ava-sdk',
    version=sdk.__version__,
    description=sdk.__doc__,
    author=sdk.__author__,
    license='Apache',
    url=dbbackup.__url__,
    keywords=keywords,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
