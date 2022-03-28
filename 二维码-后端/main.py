from flask import Flask, request, json, jsonify
import requests
from datetime import date, datetime
from flask.json import JSONEncoder
from dbsql.MysqlUtil import MysqlUtil
import qrcode

mysql = MysqlUtil()

app = Flask(__name__)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)


app.json_encoder = CustomJSONEncoder


@app.route('/', methods=['POST', 'GET'])
def index():
    data = json.loads(request.get_data().decode('utf-8'))  # 将前端Json数据转为字典
    print('小程序发起的code:', data)  # 发布前删除
    isuser = None
    appID = 'wxb75f7c86b57e3048'  # 开发者关于微信小程序的appID
    appSecret = 'c54b4e3e98b559c2a1465c01a7137487'  # 开发者关于微信小程序的appSecret
    code = data['code']  # 前端POST过来的微信临时登录凭证code
    req_params = {
        'appid': appID,
        'secret': appSecret,
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
    response_data = requests.get(
        wx_login_api, params=req_params)  # 向API发起GET请求
    data = response_data.json()
    print(data)
    openid = data['openid']  # 得到用户关于当前小程序的OpenID
    print("openid", openid)
    return jsonify({
        'status': 'success',
        'openid': openid,
    })


def return_img_stream(img_local_path):
    import base64
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


@app.route('/qrcode', methods=['POST', 'GET'])
def qr_code_2():
    # json.loads将前端json文件中的数据转化为Python字典
    # utf-8将二进制语言转化为汉字
    # get_data获取前端的wx.request中的data
    message = json.loads(request.get_data().decode('utf-8'))
    username = message.get('username')
    print(message)
    wx_id = message.get('wx_id')
    sex = message.get('sex')
    age = message.get('age')
    tel = message.get('tel')
    remark = message.get('remark')
    response_data = {'Xingming': username, 'Xingbie': sex,
                     'age': age, 'Dianhua': tel, 'Beizhu': remark}

    sql = "insert into users(username,wx_id,sex,age,tel,remark) VALUE ('%s','%s','%s','%s','%s','%s')" % (
        username, wx_id, sex, age, tel, remark)
    mysql.execute(sql)

    '''
    参数 version 表示生成二维码的尺寸大小，取值范围是 1 至 40，最小尺寸 1 会生成 21 * 21 的二维码矩阵，
    version 每增加 1，生成的二维码就会添加 4 个单位大小，例如 version 是 2，则生成 25 * 25 尺寸大小的二维码。
    参数 error_correction 指定二维码的容错系数，分别有以下4个系数：
    ERROR_CORRECT_L: 7%的字码可被容错
    ERROR_CORRECT_M: 15%的字码可被容错
    ERROR_CORRECT_Q: 25%的字码可被容错
    ERROR_CORRECT_H: 30%的字码可被容错

    参数 box_size 表示二维码里每个格子的像素大小。
    参数 border 表示边框的格子宽度是多少（默认是4）
    '''

    # 实例化QRCode生成qr对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=5,
        border=4
    )
    # 调用qrcode的make()方法传入url或者想要展示的内容
    data = response_data
    qr.add_data(data)
    qr.make(fit=True)  # 填充数据
    img = qr.make_image()  # 生成图片
    img.save("C:/Users/陈逸彬/Desktop/EEE/"+username+".png")
    img_path = 'C:/Users/陈逸彬/Desktop/EEE/' + \
        username+'.png'  # 发布的时候改为Linux的png文件夹
    img_stream = return_img_stream(img_path)

    return jsonify({
        'img': img_stream
    })


# 二维码访问地址
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
    # server = pywsgi.WSGIServer(('0.0.0.0', 3355), app)#发布环境
    # server.serve_forever()
