import requests
import json

# 微信版本3.9.2.23
class wxHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    # 0.检查微信登录**
    def checkLogin(self):
        url = f"{self.base_url}/api/?type=0"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 1.获取登录用户信息**
    def userInfo(self):
        url = f"{self.base_url}/api/?type=0"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 2.发送文本消息**
    def sendTextMsg(self, wxid, msg):
        url = f"{self.base_url}/api/?type=2"
        payload = json.dumps({
            "wxid": wxid,
            "msg": msg
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        return response.json()
   
    # 3.发送@文本消息**
    def sendAtText(self, wxids, chatRoomId, msg):
        print("modify wxids  chatRoomId")
        raise RuntimeError("modify wxids   chatRoomId then deleted me")
        url = f"{self.base_url}/api/?type=3"

        payload = json.dumps({
            "wxids": wxids,
            "chatRoomId": chatRoomId,
            "msg": msg
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 5.发送图片消息**
    def sendImagesMsg(self, wxid, imagePath):
        url = f"{self.base_url}/api/?type=5"
        print("modify imagePath")
        raise RuntimeError("modify imagePath then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "imagePath": imagePath
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 6.发送文件消息**
    def sendFileMsg(self, wxid, filePath):
        url = f"{self.base_url}/api/?type=6"
        print("modify filePath")
        raise RuntimeError("modify filePath then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "filePath": filePath
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 9.hook消息** (新特性)
    def hookSyncMsg(self, enableHttp, httpPort):
        # 定义要发送的数据
        data = {
            "port": "19099",
            "ip": "127.0.0.1",
            "url": f"http://127.0.0.1:{httpPort}",
            "timeout": "3000",
            "enableHttp": bool(enableHttp) # True HTTP专用 | False TCP专用
        }
        url = f"{self.base_url}/api/?type=9"
        # 使用 json 参数传递 JSON 数据
        response = requests.post(url, json=data)
        if response.json()["result"] == "OK":  # 使用 .json() 方法来解析响应的 JSON 数据
            if data["enableHttp"] == True:
                notice = f' * hook启动成功。文本消息将转发到http服务：{data["url"]}'
            else:
                notice = ' * hook启动成功。文本消息将转发到TCP服务'
        else:
            notice = ' * hook启动失败。文本消息转发设置失败'
        print(notice)
        return notice
    

    # 10.取消hook消息**
    def unhookSyncMsg(self):
        url = f"{self.base_url}/api/?type=10"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 11.hook图片**
    def hookImage(self):
        # hook图片原始内容，不推荐该接口，可以使用图片查询接口
        url = f"{self.base_url}/api/?type=11"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 12.取消hook图片**
    def unHookImage(self):
        url = f"{self.base_url}/api/?type=12"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 13.hook语音**
    def hookVoice(self, voiceDir):
        url = f"{self.base_url}/api/?type=13"
        payload = {
            "voiceDir": voiceDir # 语音保存的目录
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 14.取消hook语音**
    def unHookVoicee(self):
        url = f"{self.base_url}/api/?type=14"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 15.删除好友**
    def delFriend(self, wxid):
        # 删除好友,该接口不够完善，删除后，只会在通讯录里删除，如果点击聊天记录，又会重新加回来，删除的不彻底
        url = f"{self.base_url}/api/?type=17"
        print("modify delFriend ")
        raise RuntimeError("modify delFriend then deleted me")
        payload = json.dumps({
            "wxid": wxid
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 19.通过手机或qq查找微信**
    def getWx(self, keyword):
        url = f"{self.base_url}/api/?type=19"
        print("modify delFriend ")
        raise RuntimeError("modify delFriend then deleted me")
        payload = json.dumps({
            "keyword": keyword # 手机或qq
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 20.通过wxid添加好友**
    def addFriend(self, wxid, msg):
        url = f"{self.base_url}/api/?type=20"
        print("modify addFriend ")
        raise RuntimeError("modify addFriend then deleted me")
        payload = json.dumps({
            "wxid": wxid, # 好友wxid
            "msg": msg # 添加好友时的验证消息

        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 23.通过好友申请**
    def addFriend(self, v3="v3", v4="v3", permission=0):
        url = f"{self.base_url}/api/?type=23"
        print("modify addFriend ")
        raise RuntimeError("modify addFriend then deleted me")
        payload = json.dumps({
            "v3": v3, # 添加好友消息内容里的encryptusername
            "v4": v4, # 添加好友消息内容里的ticket
            "permission": permission # 好友权限,0是无限制,1是不让他看我,2是不看他,3是1+2
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 25.获取群成员**
    def getMemberFromChatRoom(self, chatRoomId):
        print("modify chatRoomId  ")
        raise RuntimeError("modify chatRoomId then deleted me")
        url = f"{self.base_url}/api/?type=25"
        payload = json.dumps({
            "chatRoomId": chatRoomId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 26.获取群成员昵称**
    def getMemberNickName(self, chatRoomId, memberId):
        print("modify getMemberNickName  ")
        raise RuntimeError("modify getMemberNickName then deleted me")
        url = f"{self.base_url}/api/?type=26"

        payload = json.dumps({
            "chatRoomId": chatRoomId, # 群id
            "memberId": memberId # 成员id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 27.删除群成员**
    def delMemberFromChatRoom(self, chatRoomId, memberIds):
        url = f"{self.base_url}/api/?type=27"
        print("modify chatRoomId  memberIds ")
        raise RuntimeError("modify chatRoomId memberIds then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "memberIds": memberIds # string 成员id，多个用,分隔
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 28.增加群成员**
    def addMemberToChatRoom(self, chatRoomId, memberIds):
        url = f"{self.base_url}/api/?type=28"
        print("modify chatRoomId  memberIds ")
        raise RuntimeError("modify chatRoomId memberIds then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "memberIds": memberIds # string 成员id，多个用,分隔
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 31.修改自身群昵称**
    def modifyNickname(self, chatRoomId, wxid, nickName):
        url = f"{self.base_url}/api/?type=31"
        print("modify chatRoomId  wxid  nickName")
        raise RuntimeError("modify chatRoomId  wxid  nickName then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "wxid": wxid,
            "nickName": nickName
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 32.获取数据库句柄**
    def getDBInfo(self):
        url = f"{self.base_url}/api/?type=32"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
  
    # 34.查询数据库**
    def execSql(self, dbHandle:int, sql):
        url = f"{self.base_url}/api/?type=34"
        print("modify dbHandle ")
        raise RuntimeError("modify dbHandle then deleted me")
        payload = json.dumps({
            "dbHandle": dbHandle,
            "sql": sql
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 35.hook日志**
    def hookLog(self):
        url = f"{self.base_url}/api/?type=35"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

   # 36.取消hook日志**
    def unhookLog(self):
        url = f"{self.base_url}/api/?type=36"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 40.转发消息**
    def forwardMsg(self, wxid, msgId:str):
        print("modify msgId  ")
        raise RuntimeError("modify msgId then deleted me")
        url = f"{self.base_url}/api/?type=40"

        payload = json.dumps({
            "wxid": wxid,
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 44.退出登录**
    def loginOut(self):
        print("modify loginOut  ")
        raise RuntimeError("modify loginOut then deleted me")
        url = f"{self.base_url}/api/?type=44"

        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    


    # 46.联系人列表**
    def getContactList(self):
        url = f"{self.base_url}/api/?type=46"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 47.群详情**
    def getChatRoomDetailInfo(self, chatRoomId):
        url = f"{self.base_url}/api/?type=47"
        print("modify chatRoomId ")
        raise RuntimeError("modify chatRoomId then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 48.获取解密图片**
    def decodeImage(self, imagePath, savePath):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/?type=48"

        payload = json.dumps({
            "imagePath": imagePath, # 待解码图片地址 "C:\\66664816980131.dat",
            "savePath": savePath # 解码后图片的存储目录 "C:\\test"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 49.提取文字**
    def getTextFromImage(self, imagePath):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/?type=49"

        payload = json.dumps({
            "imagePath": imagePath # 图片路径,
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 50.拍一拍**
    def sendPatMsg(self, chatRoomId, wxid):
        url = f"{self.base_url}/api/?type=50"
        print("modify receiver")
        raise RuntimeError("modify receiver then deleted me")
        payload = json.dumps({
            "wxid": wxid, # 要拍的用户wxid，如果使用用户自定义的微信号，则不会显示群内昵称
            "chatRoomId": chatRoomId # 微信群聊id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
   
    # 51.群内消息置顶**
    def topMsg(self, wxid, msgId:int):
        print("modify msgId  ")
        raise RuntimeError("modify msgId then deleted me")
        url = f"{self.base_url}/api/?type=51"
        payload = json.dumps({
            "wxid": wxid, # 置顶消息的发送人wxid
            "msgId": msgId # 消息id
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 52.取消群内消息置顶**
    def removeTopMsg(self, chatRoomId, msgId:int):
        print("modify msgId chatRoomId ")
        raise RuntimeError("modify msgId chatRoomId then deleted me")

        url = f"{self.base_url}/api/?type=52"

        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
     
    # 53.朋友圈首页消息**
    def getSNSFirstPage(self):
#         获取朋友圈最新消息，调用之后，会在tcpserver服务中收到朋友圈的消息。格式如下：

# {
#   'data': [
#     {
#       'content': '朋友圈[玫瑰][玫瑰]',
#       'createTime': 1675827480,
#       'senderId': 'wxid_12333',
#       'snsId': 14057859804711563695,
#       'xml': '<TimelineObject><id><![CDATA[1405712322563695]]></id><username><![CDATA[wxid_12333]]></username><createTime><![CDATA[1675827480]]></createTime><contentDescShowType>0</contentDescShowType><contentDescScene>0</contentDescScene><private><![CDATA[0]]></private><contentDesc><![CDATA[朋友圈[玫瑰][玫瑰]]]></contentDesc><contentattr><![CDATA[0]]></contentattr><sourceUserName></sourceUserName><sourceNickName></sourceNickName><statisticsData></statisticsData><weappInfo><appUserName></appUserName><pagePath></pagePath><version><![CDATA[0]]></version><debugMode><![CDATA[0]]></debugMode><shareActionId></shareActionId><isGame><![CDATA[0]]></isGame><messageExtraData></messageExtraData><subType><![CDATA[0]]></subType><preloadResources></preloadResources></weappInfo><canvasInfoXml></canvasInfoXml><ContentObject><contentStyle><![CDATA[2]]></contentStyle><contentSubStyle><![CDATA[0]]></contentSubStyle><title></title><description></description><contentUrl></contentUrl></ContentObject><actionInfo><appMsg><mediaTagName></mediaTagName><messageExt></messageExt><messageAction></messageAction></appMsg></actionInfo><appInfo><id></id></appInfo><location poiClassifyId="" poiName="" poiAddress="" poiClassifyType="0" city=""></location><publicUserName></publicUserName><streamvideo><streamvideourl></streamvideourl><streamvideothumburl></streamvideothumburl><streamvideoweburl></streamvideoweburl></streamvideo></TimelineObject>'
#     }]
# }
        url = f"{self.base_url}/api/?type=53"

        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 54.朋友圈下一页**
    def getSNSNextPage(self, snsId):
        print("modify snsId  ")
        raise RuntimeError("modify snsId then deleted me")
        url = f"{self.base_url}/api/?type=54"

        payload = json.dumps({
            "snsId": snsId
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 55.获取联系人或者群名称**
    def getContactName(self, id):
        print("modify snsId  ")
        raise RuntimeError("modify snsId then deleted me")
        url = f"{self.base_url}/api/?type=55"

        payload = json.dumps({
            "id": id # wxid或者群id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 56.获取消息附件**
    def downloadAttach(self, msgId:int):
        print("modify downloadAttach ")
        raise RuntimeError("modify downloadAttach then deleted me")
        url = f"{self.base_url}/api/?type=56"

        payload = json.dumps({
            "msgId": msgId # 消息id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
   
    # 57.获取语音文件**
    def getVoiceByMsgId(self, msgId:int, voiceDir):
        print("getVoiceByMsgId param ")
        raise RuntimeError("modify getVoiceByMsgId then deleted me")
        url = f"{self.base_url}/api/?type=57"

        payload = json.dumps({
            "msgId": msgId,
            "voiceDir": voiceDir # 语音的存储目录 "c:\\test"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    
 # 微信版本3.9.2.23   

# 微信版本大于或等于3.9.5.81本例使用3.9.8.25
class wxHandler1:
    def __init__(self, base_url):
        self.base_url = base_url

    # 0.检查微信登录**
    def checkLogin(self):
        url = f"{self.base_url}/api/checkLogin"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 1.获取登录用户信息**
    def userInfo(self):
        url = f"{self.base_url}/api/userInfo"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 2.发送文本消息**
    def sendTextMsg(self, wxid, msg):
        url = f"{self.base_url}/api/sendTextMsg"
        payload = json.dumps({
            "wxid": wxid,
            "msg": msg
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 3.hook消息**
    def hookSyncMsg(self, enableHttp, httpPort):
        url = f"{self.base_url}/api/hookSyncMsg"
        # 定义要发送的数据
        data = {
            "port": "19099",
            "ip": "127.0.0.1",
            "url": f"http://127.0.0.1:{httpPort}",
            "timeout": "3000",
            "enableHttp": bool(enableHttp) # 直接使用转换后的布尔值
        }
        
        # 使用 json 参数传递 JSON 数据
        response = requests.post(url, json=data)
        if response.json()["msg"] == "success":  # 使用 .json() 方法来解析响应的 JSON 数据
            if data["enableHttp"] == True:
                notice = f'文本消息将转发到http服务：{data["url"]}'
            else:
                notice = '文本消息将转发到TCP服务'
        else:
            notice = '文本消息转发设置失败'
        print(f'{notice}\n{response.text}')

    # 4.取消hook消息**
    def unhookSyncMsg(self):
        url = f"{self.base_url}/api/unhookSyncMsg"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 5.好友列表**
    def getContactList(self):
        url = f"{self.base_url}/api/getContactList"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 6.获取数据库信息**
    def getDBInfo(self):
        url = f"{self.base_url}/api/getDBInfo"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 7.查询数据库**
    def execSql(self, dbHandle:int, sql):
        url = f"{self.base_url}/api/execSql"
        print("modify dbHandle ")
        raise RuntimeError("modify dbHandle then deleted me")
        payload = json.dumps({
            "dbHandle": dbHandle,
            "sql": sql
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 8.发送文件消息**
    def sendFileMsg(self, wxid, filePath):
        url = f"{self.base_url}/api/sendFileMsg"
        print("modify filePath")
        raise RuntimeError("modify filePath then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "filePath": filePath
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    #9.获取群详情**
    def getChatRoomDetailInfo(self, chatRoomId):
        url = f"{self.base_url}/api/getChatRoomDetailInfo"
        print("modify chatRoomId ")
        raise RuntimeError("modify chatRoomId then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 10.添加群成员**
    def addMemberToChatRoom(self, chatRoomId, memberIds):
        url = f"{self.base_url}/api/addMemberToChatRoom"
        print("modify chatRoomId  memberIds ")
        raise RuntimeError("modify chatRoomId memberIds then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "memberIds": memberIds # string 成员id，多个用,分隔
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 12.删除群成员**
    def delMemberFromChatRoom(self, chatRoomId, memberIds):
        url = f"{self.base_url}/api/delMemberFromChatRoom"
        print("modify chatRoomId  memberIds ")
        raise RuntimeError("modify chatRoomId memberIds then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "memberIds": memberIds # string 成员id，多个用,分隔
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 11.修改群昵称**
    def modifyNickname(self, chatRoomId, wxid, nickName):
        url = f"{self.base_url}/api/modifyNickname"
        print("modify chatRoomId  wxid  nickName")
        raise RuntimeError("modify chatRoomId  wxid  nickName then deleted me")
        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "wxid": wxid,
            "nickName": nickName
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 13.获取群成员**
    def getMemberFromChatRoom(self, chatRoomId):
        print("modify chatRoomId  ")
        raise RuntimeError("modify chatRoomId then deleted me")
        url = f"{self.base_url}/api/getMemberFromChatRoom"
        payload = json.dumps({
            "chatRoomId": chatRoomId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 14.置顶群消息**
    def topMsg(self, msgId:int):
        print("modify msgId  ")
        raise RuntimeError("modify msgId then deleted me")
        url = f"{self.base_url}/api/topMsg"
        payload = json.dumps({
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 15.移除置顶群消息**
    def removeTopMsg(self, chatRoomId, msgId:int):
        print("modify msgId chatRoomId ")
        raise RuntimeError("modify msgId chatRoomId then deleted me")

        url = f"{self.base_url}/api/removeTopMsg"

        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 16.邀请入群**
    def InviteMemberToChatRoom(self, chatRoomId, memberIds):
        print("modify memberIds chatRoomId ")
        raise RuntimeError("modify memberIds chatRoomId then deleted me")

        url = f"{self.base_url}/api/InviteMemberToChatRoom"

        payload = json.dumps({
            "chatRoomId": chatRoomId,
            "memberIds": memberIds # wxid，用,分隔
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 17.hook日志**
    def hookLog(self):
        url = f"{self.base_url}/api/hookLog"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 18.取消hook日志**
    def unhookLog(self):
        url = f"{self.base_url}/api/unhookLog"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 19.建群**
    def createChatRoom(self, memberIds):
        print("modify memberIds  ")
        raise RuntimeError("modify memberIds then deleted me")
        url = f"{self.base_url}/api/createChatRoom"

        payload = json.dumps({
            "memberIds": memberIds # string 群成员id，以,分割
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 20.退群**
    def quitChatRoom(self, chatRoomId):
        print("modify chatRoomId  ")
        raise RuntimeError("modify chatRoomId then deleted me")
        url = f"{self.base_url}/api/quitChatRoom"

        payload = json.dumps({
            "chatRoomId": chatRoomId
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 21.转发消息**
    def forwardMsg(self, wxid, msgId:str):
        print("modify msgId  ")
        raise RuntimeError("modify msgId then deleted me")
        url = f"{self.base_url}/api/forwardMsg"

        payload = json.dumps({
            "wxid": wxid,
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 22.朋友圈首页**
    def getSNSFirstPage(self):
        url = f"{self.base_url}/api/getSNSFirstPage"

        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    # 23.朋友圈下一页**
    def getSNSNextPage(self, snsId):
        print("modify snsId  ")
        raise RuntimeError("modify snsId then deleted me")
        url = f"{self.base_url}/api/getSNSNextPage"

        payload = json.dumps({
            "snsId": snsId
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 24.收藏消息**
    def addFavFromMsg(self, msgId):
        print("modify msgId  ")
        raise RuntimeError("modify msgId then deleted me")
        url = f"{self.base_url}/api/addFavFromMsg"

        payload = json.dumps({
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
        
    # 24.收藏图片**    
    def addFavFromImage(self, wxid, imagePath):
        print("modify wxid imagePath ")
        raise RuntimeError("modify wxid  imagePath then deleted me")
        url = f"{self.base_url}/api/addFavFromImage"

        payload = json.dumps({
            "wxid": wxid,
            "imagePath": imagePath
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 26.获取群成员信息**
    def getContactProfile(self, wxid):
        print("modify wxid  ")
        raise RuntimeError("modify wxid   then deleted me")
        url = f"{self.base_url}/api/getContactProfile"

        payload = json.dumps({
            "wxid": wxid
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

    # 25.发送@消息**
    def sendAtText(self, wxids, chatRoomId, msg):
        print("modify wxids  chatRoomId")
        raise RuntimeError("modify wxids   chatRoomId then deleted me")
        url = f"{self.base_url}/api/sendAtText"

        payload = json.dumps({
            "wxids": wxids,
            "chatRoomId": chatRoomId,
            "msg": msg
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 27.发送公众号消息**
    def forwardPublicMsg(self, appName, userName, title, url, thumbUrl, digest, wxid):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/forwardPublicMsg"

        payload = json.dumps({
            "appName": appName, # 公众号id，消息内容里的appname
            "userName": userName, # 公众号昵称，消息内容里的username
            "title": title, # 链接地址，消息内容里的title
            "url": url, # 链接地址，消息内容里的url
            "thumbUrl": thumbUrl, # 缩略图地址，消息内容里的thumburl
            "digest": digest, # 摘要，消息内容里的digest
            "wxid": wxid # 	wxid
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 28.转发公众号消息**
    def forwardPublicMsgByMsgId(self, msgId:int, wxid):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/forwardPublicMsgByMsgId"

        payload = json.dumps({
            "msgId": msgId,
            "wxid": wxid
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 29.下载附件**
    def downloadAttach(self, msgId:int):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/downloadAttach"

        payload = json.dumps({
            "msgId": msgId
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 30.解码图片**
    def decodeImage(self, filePath, storeDir):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/decodeImage"

        payload = json.dumps({
            "filePath": filePath, # 待解码图片地址 "C:\\66664816980131.dat",
            "storeDir": storeDir # 解码后图片的存储目录 "C:\\test"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 31.获取语音**
    def getVoiceByMsgId(self, msgId:int, storeDir):
        print("modify param ")
        raise RuntimeError("modify param then deleted me")
        url = f"{self.base_url}/api/getVoiceByMsgId"

        payload = json.dumps({
            "msgId": msgId,
            "storeDir": storeDir # 语音的存储目录 "c:\\test"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 32.发送图片**
    def sendImagesMsg(self, wxid, imagePath):
        url = f"{self.base_url}/api/sendImagesMsg"
        print("modify imagePath")
        raise RuntimeError("modify imagePath then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "imagePath": imagePath
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    # 33.发送自定义表情**
    def sendCustomEmotion(self, wxid, filePath):
        url = f"{self.base_url}/api/sendCustomEmotion"
        print("modify filePath")
        raise RuntimeError("modify filePath then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "filePath": filePath
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 34.发送小程序**
    def sendApplet(self, wxid, waidConcat, appletWxid, jsonParam, headImgUrl, mainImg, indexPage):
        url = f"{self.base_url}/api/sendApplet"
        print("modify sendApplet")
        raise RuntimeError("modify sendApplet then deleted me")
        payload = json.dumps({
            "wxid": wxid, # 接收人wxid
            "waidConcat": waidConcat, # app的wxid与回调信息之类绑定的拼接字符串，伪造的数据可以随意
            "appletWxid": appletWxid, # app的wxid
            "jsonParam": jsonParam, # 相关参数
            "headImgUrl": headImgUrl, # 头像url
            "mainImg": mainImg, # 主图的本地路径,需要在小程序的临时目录下
            "indexPage": indexPage # 小程序的跳转页面
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    # 35.拍一拍**
    def sendPatMsg(self, wxid, receiver):
        url = f"{self.base_url}/api/sendPatMsg"
        print("modify receiver")
        raise RuntimeError("modify receiver then deleted me")
        payload = json.dumps({
            "wxid": wxid,
            "filePath": receiver # 接收人id，可以是自己wxid，私聊好友wxid，群id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
   
    # 36.OCR**
    def ocr(self, imagePath):
        url = f"{self.base_url}/api/ocr"
        print("modify receiver")
        raise RuntimeError("modify receiver then deleted me")
        payload = json.dumps({
            "imagePath": imagePath # 图片全路径
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()   
 


    