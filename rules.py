
class Rule(object):
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class ParagraphRule(Rule):
    """
       段落是不符合其他规则的快
    """
    type = 'paragraph'

    def condition(self, block):
        return True


class HeadRule(Rule):

    """
    标题是一个最多70字符的行，不一冒号结束
    """
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block)<= 70 and not block[-1] ==':'


class TitleRule(Rule):
    """
    标题是一个最多70字符的行，不一冒号结束
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadRule.condition(self, block)
