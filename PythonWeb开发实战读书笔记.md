1. 尽早使代码符合PEP8
2. Pythonic

升级pip到最新版本：

```python
 pip install pip -U -q
 #-q表示静默安装，减少过程输出
 pip --version
```

flask的helloword程序：

```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

```

debug设置为true：

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

URL拼接：

```python
# coding=utf-8
from flask import Flask, url_for
app = Flask(__name__)


@app.route('/item/1/')
def item(id):
    pass


with app.test_request_context():
    print url_for('item', id='1')
    print url_for('item', id=2, next='/')

```

