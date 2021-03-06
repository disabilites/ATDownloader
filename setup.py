from setuptools import setup, find_packages

setup(
    name='ATDownloader',
    version='1.2',
    packages=find_packages(),
    install_requires=[
        'requests>=2.18.4',
        'mutagen>=1.40.0',
        'lxml>=4.1.1',
        'beautifulsoup4>=4.6.0',
    ],
    entry_points={
    'console_scripts': [
        'ncm=ncm.main:main',
        'pixiv=pixiv.main:main',
        'htkt=htkt.main:main',
    ]
    },

    author='horizon',
    author_email='horizon@im.ashtwo.cn',
    url='https://github.com/codezjx/ATDownloader',
    keywords=['downloader', 'netease', 'cloud-music', 'pixiv', 'hitokoto'],
    description = 'Netease cloud music song downloader, Pixiv img downloader'
)
