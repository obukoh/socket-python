# クライアントを作成

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50007))
    # サーバにメッセージを送る
    val = input('Enter your message: ').encode()
    s.sendall(val)
    # s.sendall(b'hello')
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
    data = s.recv(1024)
    #
    print(repr(data))
