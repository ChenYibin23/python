from flask import Flask, request, Response, json
# from flask.json import JSONEncoder
# MYsqlUtil是自己创建的数据库
from mysql import MysqlUtil
import re
import random
# import redis

# 将MysqlUtil实例化w
mysql = MysqlUtil()
app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    # 通过使用此行代码调用前端wx。request中的data字典中的值
    # get_data为关键字，必须对应小程序文件当中的js文件中的data字典
    message = json.loads(request.get_data().decode('utf-8'))
    print(message)
    # 获取前端传回到message中的值
    # 1、获取前端的zhanghao
    zhanghao = message.get('zhanghao')
    password = message.get('password')
    # 2、对前端传回的zhanghao进行正则判断
    if not re.match(r"^(1[3|4|5|6|7|8|9])\d{9}$", zhanghao):
        # 如果不符合正则的格式则返回手机格式错误
        return Response('手机号格式错误')
        # 如果zhanghao为空也不能运行
    if (zhanghao == ""):
        return Response('手机号格式错误')
    # 3、生成随机的验证码
    # 生成1000到一百之间的随机数字，即四位验证码
    randamNumber = random.randint(1000, 9999)
    print(randamNumber)
    # 使用sql语句将zhanghao，password插入到表aaa中
    sql = "insert into aaa(zhanghao,password) VALUE ('%s','%s')" % (
        zhanghao, password)
    # 运行这个sql语句
    mysql.execute(sql)
    # 此处必须有返回值
    # 返回时的值必须是字符串，需要进行类型的转换
    return str(randamNumber)
    # 4、将验证码发到手机上，需要购买服务接口（百度云/阿里云）


if __name__ == '__main__':
    # host设置域名，port设置端口，debug调试模式
    app.run(host='127.0.0.1', port=5000, debug=True)
