from util.util import *
from rules import *
from handlers import *


class Parser(object):
    """
    .....Dessciption
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):

        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    def __init__(self, handler):
        super().__init__(handler)
        # 1.找到问题实例来调用实例方法，不能通过类来调用
        # 有进一步抽象原来处理的是数据现在用函数处理的是类和函数
        self.addRule(HeadRule())
        self.addRule(TitleRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', r'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)