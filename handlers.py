import re
import sys
# from util.util import *
# print('<html><head><title>...</title></head><body>')
#
# title = True
# for block in blocks(sys.stdin):
#     block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
#     if title:
#         print('<h1>')
#         print(block)
#         print('</h1>')
#         title = False
#     else:
#         print('<p>')
#         print(block)
#         print('</p>')
# print('</body></html>')






class Handler(object):
        def callback(self, prefix, name, *args):
            method = getattr(self, prefix+name, None)
            if callable(method):
                return method(*args)

        def start(self, name):
            self.callback('start_', name)

        def end(self, name):
            self.callback('end_', name)

        # 这个有点抽象大概就是传入函数名，和正则生成的一个match对象<_sre.SRE_Match objectyi和matchcallback调用，
        # re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'this is a *test* jjj' )

        def sub(self, name):
            def substitution(match):
                result = self.callback('sub_', name , match)
                if result is None:
                    result = match.group(0)
                return result
            return substitution


class HTMLRenderer(Handler):

        def start_document(self):
            print('<html><head><title>...</title></head><body>')

        def end_document(self):
            print('</body></html>')

        def start_paragraph(self):
            print('<p>')

        def end_paragraph(self):
            print('</p>')

        def start_heading(self):
            print('<h2>')

        def end_heading(self):
            print('</h2>')

        def start_title(self):
            print('<h1>')

        def end_title(self):
            print('</h1>')

        def sub_emphasis(self, match):
            return '<em>%s</em>'%match.group(1)

        def sub_url(self, match):
            return '<a href="%s">URL%s</a>'%(match.group(1), match.group(1))

        def sub_mail(self, match):
            return '<a href="mailto:%s">MAIL%s</a>'%(match.group(1), match.group(1))

        def feed(self, data):
            print(data)

