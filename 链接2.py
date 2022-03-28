# from urllib import response
from flask import Flask, request, json, Response
from mysql import MysqlUtil
import random
import re

app = Flask(__name__)
mysql = MysqlUtil()


@app.route('/index', methods=['GET', 'POST'])
def login():
    message = json.loads(request.get_data().decode('utf-8'))
    zhanghao = message.get('zhanghao')
    password = message.get('password')
    print(message)
    # if (zhanghao == ""):
    #     return Response("手机号有误")
    # if not re.match(r"^(1[3|4|5|6|7|8|9])\d{9}$", zhanghao):
    #     return Response("手机号有误")
    if not re.match(r"^(1[3|4|5|6|7|8|9])\d{9}$", zhanghao):
        # 如果不符合正则的格式则返回手机格式错误
        return Response('手机号格式错误')
        # 如果zhanghao为空也不能运行
    if (zhanghao == ""):
        return Response('手机号格式错误')
    sql = "insert into user1(zhanghao,password) VALUE ('%s','%s')" % (
        zhanghao, password)
    mysql.execute(sql)
    randomNumber = random.randint(1000, 9999)
    return str(randomNumber)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
