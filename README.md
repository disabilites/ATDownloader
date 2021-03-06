# ATDownloader综合下载器

基于<b>python3.0（2.0环境可能无法运行）</b>的命令提示行下载器，目前支持下载网易云音乐和Pixiv，后续还会继续拓展功能。

### 安装
进入setup.py目录，运行：  

`python setup.py install`

显示以下信息，则表示安装成功：  

```
running install
running bdist_egg
running egg_info
...

Processing dependencies for ATDownloader==1.0
Finished processing dependencies for ATDownloader==1.0
```

默认会在C盘的用户目录下生产.ATDownloader和配置文件config.ini

### 更新
2018-07-02 增加专辑下载功能，歌单下载进行分类（因为所使用的API没有歌单的名字，所以另外从网页上获取歌单名字，较为繁琐）

2018-07-03 增加Pixiv作品下载功能，支持**作品下载（请在合适的年龄、时间、地点下载）；修复一个配置文件的bug

2018-07-06 增加Pixiv排行榜下载功能；修改部分代码  

2018-07-09 增加网易云音乐下载显示进度条功能；多首歌曲下载；跳过已下载歌曲；修复Pixiv下载bug；榜单未更新时的异常处理

2018-07-10 增加Pixiv多作品下载

2018-07-12 增加一言（Hitokoto/ヒトコト）功能；增加错误信息输出，修复配置文件bug

***

## 网易云音乐

### 相关命名

ncm -h 查看帮助 

```
usage: ncm [-h] [-s song_id] [-p playlist_id] [-a album_id]

Welcome to ATDownloader!

optional arguments:
  -h, --help      show this help message and exit
  -s song_id      歌曲ID
  -ss song_ids    多首歌曲ID
  -p playlist_id  歌单ID
  -a album_id     专辑ID
```

ncm -s  下载歌曲  

`ncm -s 494174528（歌曲ID）`

ncm -ss 下载多首歌曲

`ncm -ss 557579157 468490592 ...（多首歌曲ID，中间用空格隔开）`

ncm -p  下载歌单  

`ncm -p 2264487099（歌单ID）`

ncm -a  下载专辑 

`ncm -a 38225036（专辑ID）`

### 注意

1.**下架或版权歌曲无法下载**  

2.歌曲码率、下载位置等可以在**config.ini**里更改  

3.自动添加歌曲图片，艺术家等信息

4.下载时如果两首歌的歌名、艺术家完全相同，则之前的歌会被覆盖

***

## Pixiv

### 相关命令

ncm -h 查看帮助

```
usage: pixiv [-h] [-i illust_id] [-r rank]

Welcome to ATDownloader!

optional arguments:
  -h, --help    show this help message and exit
  -i illust_id  作品ID
  -r rank       排行榜
```

ncm -i 下载单个作品

`pixiv -i 69241757`

ncm -is 下载多个作品

`pixiv -is 69520660 69005540 ...（多个作品ID，中间用空格隔开）` 

ncm -r 下载排行榜内容，默认参数（mode=day,page=1,date=''） 
>mode:榜单（可选：day、week、month）  
>page:页数（一页有30个作品）  
>date:榜单日期（格式：年-月-日，如2018-07-06）

```
pixiv -r day _ _
or
pixiv -r week 3 _
or
pixiv -r month _ 2018-07-06
```


### 注意
1.不需要梯子也能下载

2.图片下载位置可以在**config.ini**里修改

3.请不要在工作学习时间下载不适合全年龄段图片

4.不需要改变的参数请用<b>"_"</b>占位  

5.排行榜时区为**UTC+9**，每日12：00PM更新，与您所在时区可能会有所偏差

6.参数请按 mode page date顺序填写，并用空格隔开 

***

## 一言（Hitokoto/ヒトコト）

### 相关命令

htkt -h 查看帮助

```
usage: main.py [-h] [-cat [cat]]

Welcome to ATDownloader!

optional arguments:
  -h, --help  show this help message and exit
  -cat [cat]  分类
```

htkt -cat 分类，默认参数（cat=None）
>a	Anime - 动画  
>b	Comic - 漫画  
>c	Game - 游戏  
>d	Novel - 小说  
>e	原创  
>f	来自网络  
>g	其他

```
htkt -cat
隐约雷鸣，阴霾天空，但盼风雨来，能留你在此。     —— 言叶之庭
or
htkt -cat c
愿风指引着你的道路，愿你的刀刃永远锋利。     —— 魔兽世界
```
