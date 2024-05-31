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
