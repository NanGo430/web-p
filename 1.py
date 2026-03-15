import http.server
import socketserver
import os

# 设置端口
PORT = 1180

# 确保脚本在当前文件所在目录运行
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

# 允许跨域和缓存处理（优化浏览器加载体验）
class MyHandler(Handler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"✅ 音乐播放器服务已启动！")
    print(f"🔗 访问地址: http://localhost:{PORT}")
    print(f"📂 根目录文件: {os.getcwd()}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止")
        httpd.shutdown()