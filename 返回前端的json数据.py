from flask import Flask, make_response, json, jsonify

app = Flask(__name__)


# 关闭自动编码为ASCII
app.config['JSON_AS_ASCII'] = False


@app.route('/index')
def index():
    # 用字典的形式存储数据
    data = {
        'name': '张三'
    }

# 返回data到make_response
# ensure_ascii为将内容转化为ascii码，默认为true，修改之后可返回中文
    response = make_response(json.dumps(data, ensure_ascii=False))
    # 设置数据为json数据（1）
    response.mimetype = 'application/json'
    return response
    # 设置数据为json数据（2）
    return jsonify(data)


if __name__ == '__main__':
    # 括号中可填上运行方式
    app.run()
