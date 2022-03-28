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
