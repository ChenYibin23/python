# from MyQR import myqr

# print ("生成二维码")
# myqr.run(words='https://www.fosugd.com/wechat/score',
#     save_name='测试.jpg',
#     save_dir='C:/Users/zjy/Desktop'
#     )
# print("生成完毕")
import qrcode
from flask import request

# 方法2
def qr_code_2():
    #前端传过来的数据包含（username，tel, age, 备注信息）
    # user_massgae = request.get_data().decode('utf-8')
    username = "资佳阳" #实际上应该是从user_message里面取出来的
    sex = "男"
    tel = 111111111   #注意取出来的是int 还是string
    remark = "备注" 
    response_data = {"Xingming":username, "Xingbie":sex,  "Dianhua":tel ,"Beizhu":remark}

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
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    # 调用qrcode的make()方法传入url或者想要展示的内容
    data = response_data
    qr.add_data(data)
    qr.make(fit=True)# 填充数据
    img = qr.make_image() # 生成图片
    img.save("C:/Users/zjy/Desktop/test2.png")

qr_code_2()
