#  模板 采用jinja2的语法结构

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    # 创建字典
    aaa = {
        'name': '张三',
        'age': 18,
        'mylist': [1, 2, 3, 4, 5, 6]
    }
    # 将字典aaa给到名为bbb的变量
    return render_template('002.html', bbb=aaa)

# 创建自定义过滤器
def ccc(ddd):
    '''自定义过滤器'''
    # 设置步距为2
    return ddd[::2]

# 注册过滤器  括号中第一个值写上自定义函数名，第二个写上过滤器名（使用时）
app.add_template_filter(ccc, 'eee')

# 测试自定义的过滤器
# li = [1, 2, 3, 4, 5]
# fff = ccc(li)
# print(fff)
if __name__ == '__main__':
    app.run()
