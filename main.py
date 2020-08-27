import requests
import pyperclip
import pymysql
import json
import random
import time
import sys
from config import *

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

baseUrl = 'https://www.missevan.com/sound/getsound'


def fetch_url(id):
    r = requests.get(f'{baseUrl}?soundid={id}', headers=header)
    data = json.loads(r.text)
    return data['info']['sound']


# 获取音频信息
sound = fetch_url(sys.argv[1])

# 复制音频url
pyperclip.copy(sound['soundurl_128'])


class DatabaseAccess():
    # 初始化属性
    def __init__(self):
        self.__db_host = host
        self.__db_port = port
        self.__db_user = user
        self.__db_password = password
        self.__db_database = database

    # 连接数据库
    def isConnectionOpen(self):
        self.__db = pymysql.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_user,
            password=self.__db_password,
            database=self.__db_database,
            charset='utf8'
        )

    # 插入数据
    def linesinsert(self, song_names, song_urls, song_covers, createds):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into wp_hermit(song_name,song_url,song_cover,created) value(%s,%s,%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (song_names, song_urls, song_covers, createds))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()

    # 赋值
    def data_update(self):
        song_name = sound['soundstr']
        song_url = sound['soundurl_128']
        song_cover = sound['front_cover']
        created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.linesinsert(song_name, song_url, song_cover, created)
        print("success !")


if __name__ == "__main__":
    # 创建实例化对象
    db = DatabaseAccess()
    # 调用方法
    db.data_update()
