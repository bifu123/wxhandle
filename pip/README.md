# wxhandler

A Python package for handling wxHandler operations. 
- wxhandler will be use on wechat-3.9.2.23. 
- wxhandler1 will be use on wechat-3.9.8.25.
My github: https://github.com/bifu123/wxhandler

## Installation

```bash
pip install wxhandler
```
## Usage
```python
from wxhandler import wxHandler1

# create wxHandler1 object
handler = wxHandler1(base_url="http://127.0.0.1:19088") 
# send text message
wxid = "cbf_415135222"
message = "hello"
handler.sendTextMsg(wxid, message)
```


