from setuptools import setup, find_packages

setup(
    name='ATDownloader',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.18.4',
        'mutagen>=1.40.0',
    ],
    entry_points={
    'console_scripts': [
        'ncm=ncm.main:main',
    ]
    },

    author='horizon',
    author_email='horizon@im.ashtwo.cn',
    url='https://github.com/codezjx/ATDownloader',
)
