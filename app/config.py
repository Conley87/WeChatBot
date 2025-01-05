import os

# PORT = int(os.environ.get('PORT', 3001))  # 该端口需保持与wechatbot-webhook容器端口一致
REPLYMODE = os.getenv('REPLYMODE', 'true').lower() == 'true'  # 回复模式，是否仅被@时回复
SEND_API = os.getenv('SEND_API', 'http://localhost:3001/webhook/msg/v2 ')
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
