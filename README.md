# Socket 通信

## ➀socket module 

Socket は、サーバとクライアントを結ぶ仮想的な接続を実現する。

![socket](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F215099%2F27765345-cab8-26df-ab40-688f535bcb9e.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=3bb901aa129b3e08ddc48f0fde229b57)

サーバとクライアントがお互い関係を持っているので、片方のソケットが書き込んだデータは、もう片方のソケットから取り出すことができる。

### アドレスファミリ

| アドレスファミリ |                   意味                   |
| :--------------- | :--------------------------------------: |
| AF_INET          |           IPv4 によるソケット            |
| AF_INET6         |           IPv6 によるソケット            |
| AF_UNIX          |   ローカルなプロセス間通信用のソケット   |
| AF_INET          | デバイスレベルのパケットインターフェース |



### socket type

| ソケットタイプ |                             意味                             |
| :------------- | :----------------------------------------------------------: |
| SOCK_STREAM    | 順序性と信頼性があり、双方向の接続されたバイトストリーム（byte stream）を提供する(TCP) |
| SOCK_DGRAM     | データグラム（接続、信頼性なし、固定最大長メッセージ）をサポートする(UDP) |

ソケットタイプとアドレスファミリの組み合わせて、通信方式を決定する。



### クラス・メソッド 

[detail](https://docs.python.org/3/library/socket.html#socket.socket.recv)

- `socket.bind`(*address*)

**Bind the socket to *address*.** The socket must not already be bound.

- `socket.listen`([*backlog*])

**Enable a server to accept connections.** If *backlog* is specified, it must be at least 0 (if it is lower, it is set to 0); it specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.

*Changed in version 3.5:* The *backlog* parameter is now optional.

- `socket.accept`()

**Accept a connection.** The socket must be bound to an address and listening for connections. **The return value is a pair `(conn, address)` where *conn* is a *new* socket object usable to send and receive data on the connection, and *address* is the address bound to the socket on the other end of the connection.**

- `socket.recv`(*bufsize*[, *flags*])

**Receive data from the socket.** The return value is a bytes object representing the data received. **The maximum amount of data to be received at once is specified by *bufsize*.** See the Unix manual page *[recv(2)](https://manpages.debian.org/recv(2))* for the meaning of the optional argument *flags*; it defaults to zero.

- `socket.send`(*bytes*[, *flags*])

**Send data to the socket.** The socket must be connected to a remote socket. The optional *flags* argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv) above. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data. For further information on this topic, consult the [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html#socket-howto).

- `socket.sendall`(*bytes*[, *flags*])

**Send data to the socket.** The socket must be connected to a remote socket. The optional *flags* argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv) above. **Unlike [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send), this method continues to send data from *bytes* until either all data has been sent or an error occurs.** `None` is returned on success. On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.



## ➁socketserver module

[detail](https://docs.python.org/ja/3/library/socketserver.html)

[`socketserver`](https://docs.python.org/ja/3/library/socketserver.html#module-socketserver) モジュールはネットワークサーバを実装するタスクを単純化します。

### クラス・メソッド

- *class* `socketserver.TCPServer`(<u>*server_address*</u>, <u>*RequestHandlerClass*</u>, *bind_and_activate=True*)

  This uses the Internet TCP protocol, which provides for continuous streams of data between the client and server. <u>**If *bind_and_activate* is true, the constructor automatically attempts to invoke [`server_bind()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.server_bind) and [`server_activate()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.server_activate).**</u> The other parameters are passed to the [`BaseServer`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer) base class.

- `serve_forever`(*poll_interval=0.5*)

  **Handle requests until an explicit [`shutdown()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.shutdown) request.** Poll for shutdown every *poll_interval* seconds. Ignores the [`timeout`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.timeout) attribute. It also calls [`service_actions()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.service_actions), which may be used by a subclass or mixin to provide actions specific to a given service. For example, the [`ForkingMixIn`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.ForkingMixIn) class uses [`service_actions()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseServer.service_actions) to clean up zombie child processes.

- `handle`()

  この関数では、クライアントからの要求を実現するために必要な全ての作業を行わなければなりません。デフォルト実装では何もしません。この作業の上で、いくつかのインスタンス属性を利用することができます; クライアントからの要求は `self.request` です; クライアントのアドレスは `self.client_address` です; そしてサーバごとの情報にアクセスする場合には、サーバインスタンスを `self.server` で取得できます。The type of `self.request` is different for datagram or stream services. For stream services, `self.request` is a socket object; for datagram services, `self.request` is a pair of string and socket.

- `setup`()

  [`handle()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseRequestHandler.handle) メソッドより前に呼び出され、何らかの必要な初期化処理を行います。標準の実装では何も行いません。

- `finish`()

  [`handle()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseRequestHandler.handle) メソッドより後に呼び出され、何らかの必要なクリーンアップ処理を行います。標準の実装では何も行いません。 [`setup()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseRequestHandler.setup) メソッドが例外を送出した場合、このメソッドは呼び出されません。

- *class* `socketserver.BaseRequestHandler`

  **This is the superclass of all request handler objects.** It defines the interface, given below. **A concrete request handler subclass must define a new [`handle()`](https://docs.python.org/ja/3/library/socketserver.html#socketserver.BaseRequestHandler.handle) method,** and can override any of the other methods. A new instance of the subclass is created for each request.