- 本程序供群内使用，旨在研究软件技术，请勿用于非法用途
- 如果是新开小号，建议实名认证，养号三日后再说
## 注入青䓯素
一、自行下载安装最新版微信、登陆、设置禁止自动更新
二、卸载最新版微信（保留登陆和设置信息）
三、安装微信3.9.8.25，并登录之。
四、运行注入工具injector.exe将wxbot.dll注入
## 快速开始
### 安装pip包
```bash
pip install --upgrade wxhandler
```
### 发送消息
新建文件test.py代码：
```python
from wxhandler import wxHandler1

# # 创建一个微信处理对象
handler = wxHandler1(base_url="http://127.0.0.1:19088") 
# 发送文本消息
handler.sendTextMsg("cbf_415135222", "hello")
```
运行test.py
```bash
python test.py
```
结果：
[发消息](images/1.png)

[发消息](images/1.jpg)

### 获取消息
新建文件flask_server.py
```python
from flask import Flask, request
import json
from wxhandler import wxHandler1

app = Flask(__name__)

base_url = "http://127.0.0.1:19088"


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    # 获取原始的请求数据
    message_data = request.data
    # 将字节串转换为字符串并格式化打印出来 
    data = message_data.decode('utf-8')
    message_json = json.loads(data)
    formatted_message = json.dumps(message_json, indent=4, ensure_ascii=False)
    print("*" * 20,"message", "*" * 20)
    print(formatted_message)
    print("*" * 50)
    # 取得参数
    
    return data

if __name__ == '__main__':
    wxHandler1(base_url).hookSyncMsg(enableHttp=True, httpPort=8000) # 启动微信消息同步
    app.run(port=8000, host="0.0.0.0", debug=True)
```
运行flask_server.py
```bash
python flask_server.py
```
[运行flask](images/2.png)

从微信里发消息：
[发消息](images/3.jpg)

flask里监听到了消息：
[flask](images/4.png)

资源获取和交流：QQ群222302526