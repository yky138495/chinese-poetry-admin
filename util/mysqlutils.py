import pymysql
import pymysql.cursors


def get_connect(db):
    """连接mysql数据库"""
    connect = pymysql.connect(host='***',
                                 user='*',
                                 password='**',
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connect
