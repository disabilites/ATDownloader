# ATDownloader综合下载器
***
基于python3.0的命令提示行下载器，目前仅支持下载网易云音乐的相关内容，后续还会继续拓展功能。
***
## 网易云音乐
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

### 相关命名
ncm -h 查看帮助 

```
usage: ncm [-h] [-s song_id] [-p playlist_id]

Welcome to ATDownloader!

optional arguments:
  -h, --help      show this help message and exit
  -s song_id      song_id
  -p playlist_id  playlist_id
```

ncm -s  下载歌曲  

`ncm -s 如：494174528（歌曲ID）`

ncm -p  下载歌单  

`ncm -p 如：2264487099（歌单ID）`

ncm -a  下载专辑 

`ncm -a 如：38225036（专辑ID）`

### 注意
1.该程序目前只能在**python3.0**环境下运行  

2.**下架或版权歌曲无法下载**  

3.歌曲码率、下载位置等可以在**config.ini**里更改  

### 更新
2018-7-02 增加专辑下载功能，歌单下载进行分类（因为所使用的API没有歌单的名字，所以另外从网页上获取歌单名字，较为繁琐）

