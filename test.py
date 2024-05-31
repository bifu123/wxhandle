from wxhandler import wxHandler1

# # 创建一个微信处理对象
handler = wxHandler1(base_url="http://127.0.0.1:19088") 
# 发送文本消息
handler.sendTextMsg("cbf_415135222", "hello")

