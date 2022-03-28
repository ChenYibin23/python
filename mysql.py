import pymysql


class MysqlUtil:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.username = 'root'
        self.password = 'root'
        self.database = 'qrcode'  # 数据库名
        self.charset = 'utf8'
        self.autocommit = True
        pass

    def connection(self):
        # 连接数据库
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.username,
                                  password=self.password, db=self.database, charset=self.charset, autocommit=self.autocommit)
        return self.db

    def get_cursor(self):
        # 获取游标
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        return self.cursor

    def close_db(self):
        # 关闭连接
        self.cursor.close()
        self.db.close()

    def execute(self, sql):
        try:
            con = self.connection()
            cur = self.get_cursor()
            data = cur.execute(sql)
            con.commit()
            return data
        except:
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def fetch_all(self, sql):
        try:
            con = self.connection()
            cur = self.get_cursor()
            cur.execute(sql)
            data = cur.fetchall()
            return data
        except:
            # 如果发生错误则回滚
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def fetch_one(self, sql):
        try:
            con = self.connection()
            cur = self.get_cursor()
            cur.execute(sql)
            data = cur.fetchone()
            return data
        except:
            # 如果发生错误则回滚
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()
