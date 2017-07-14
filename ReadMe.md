# このソフトウェアについて

https://docs.python.jp/3/contents.htmlから木構造になっている見出しのうち葉ノードだけを抜き出した。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

# 実行

```sh
python3 Main.py
```

GitHubに登録し、メール確認済みの、ユーザ名、パスワード、メールアドレスを使う。

# 結果

* `https://docs.python.jp/3/contents.html`を`PyDoc.Contents.html`として保存する
* `PyDoc.Contents.Leafs.txt`として見出しの葉ノードのタイトルだけをリストにする

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)

