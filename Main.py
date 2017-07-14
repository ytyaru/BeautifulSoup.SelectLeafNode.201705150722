#!python3
#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import os.path
import CssPseudoClass
import chardet
"""
https://docs.python.jp/3/contents.htmlから見出しを抜き出す。
* 葉ノードを取得する
"""
class Main(object):
    def __init__(self):
        pass
    
    def GetLeafNodePyDocToC(self):
        return self.__GetLeafNoeds(self.__HttpGetPyDocToC())
    
    def __HttpGetPyDocToC(self):
        if not os.path.isfile(self.__GetHtmlFilePath()):
            url = 'https://docs.python.jp/3/contents.html'
            r = requests.get(url)
            r.raise_for_status()
            print(r.encoding) # ISO-8859-1
            r.encoding = r.apparent_encoding # http://qiita.com/nittyan/items/d3f49a7699296a58605b
            print(r.encoding) # utf-8
            with open(self.__GetHtmlFilePath(), 'w', encoding='utf-8') as f:
                f.write(r.text)
                
        with open(self.__GetHtmlFilePath()) as f:
            return BeautifulSoup(f.read(), 'lxml') # html.parser, lxml
            
    def __GetHtmlFilePath(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PyDoc.Contents.html')

    def __GetLeafNoeds(self, soup):
        tree = soup.find('div', class_='toctree-wrapper compound') # 2個目に取得できるものは空だから1個目を取る
        # bs4は擬似クラスをnth-of-typeしか実装してないらしい。
#        leafs = tree.select('li:not(:has(ul))') # NotImplementedError: Only the following pseudo-classes are implemented: nth-of-type.
        selector = CssPseudoClass.CssPseudoClass()
        leafs = []
        for li in tree.find_all('li'):
            if not selector.Has(li, 'ul'):
                # li内のa要素内にcode要素があるときがある。li.a.stringだとNoneが返されてしまう。`stripped_strings`で空白文字を省いた文字列を取得できる。
                title = ''.join(li.a.stripped_strings) # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings
                leafs.append(title)
        print('count = {0}'.format(len(leafs)))

        leafs_text = ''
        for leaf in leafs:
            leafs_text += leaf + '\n'
        print(leafs_text)
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PyDoc.Contents.Leafs.txt'), 'w') as f:
            f.write(leafs_text)


if __name__ == '__main__':
    m = Main()
    m.GetLeafNodePyDocToC()

