
api_url = 'https://api.imjad.cn/pixiv/v2/'
err_strList = ['/', '\\', '<', '>', '|', ':', '?', '*', '"']
re_strList = ['／', '＼', '〈', '〉', '｜', '：', '？', '﹡', '“']

def get_referer(illust_id):
    referer = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + illust_id
    return referer

def get_illust_params(illust_id):
    illust_params = {'type': 'illust', 'id': illust_id}
    return illust_params