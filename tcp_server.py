import json
import threading
import socketserver
import requests

from wxhandler import wxhandler1

# 将HOOK消息转到本脚本



class ReceiveMsgSocketServer(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        conn = self.request
        while True:
            try:
                ptr_data = b""
                while True:
                    data = conn.recv(1024)
                    ptr_data += data
                    if len(data) == 0 or data[-1] == 0xA:
                        break

                msg = json.loads(ptr_data)
                ReceiveMsgSocketServer.msg_callback(msg)

            except OSError:
                break
            except json.JSONDecodeError:
                pass
            conn.sendall("200 OK".encode())
        conn.close()

    @staticmethod
    def msg_callback(msg):
        # 打印出接收到的消息
        formatted_message = json.dumps(msg, indent=4, ensure_ascii=False)
        print(formatted_message)


def start_socket_server(port: int = 19099,
                        request_handler=ReceiveMsgSocketServer,
                        main_thread: bool = True) -> int or None:
    ip_port = ("127.0.0.1", port)
    try:
        s = socketserver.ThreadingTCPServer(ip_port, request_handler)
        if main_thread:
            s.serve_forever()
        else:
            socket_server = threading.Thread(target=s.serve_forever)
            socket_server.setDaemon(True)
            socket_server.start()
            return socket_server.ident
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    base_url = "http://127.0.0.1:19088"
    wxhandler1(base_url).hookSyncMsg(False, 8000) # 启动微信消息同步
    start_socket_server()
