# <>提取参数
# <int:id> int转换器

# 自定义转换器

from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)
# 调用父类
class aaa(BaseConverter):
    def __init__(self,url_map,regex):
        # 调用父类的方法（super关键字）
        # 调用了父类中的__init__并将url_map传入
        super(aaa,self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print('to_python方法被调用')
        # 父类的方法功能已经实现好了
        return value



# 将自定义的转换器添加到flask应用中
# 以字典的形式添加到flask中
app.url_map.converters['re'] = aaa
@app.route('/index/<re(""):value>')
def index(value):
    print(value)
    return 'hello'


if __name__ == '__main__':
    app.run()