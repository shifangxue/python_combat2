

from hogwarts3.life.Super_life import super_life
"""
定义Dog类
描述犬类共有属性与特征
"""
class Dog(super_life):
    """
    :param
        color:颜色
        height:身高
        weight:体重
        flag:大 中 小
        name：名字
    """
    def __init__(self, color="w", height="10cm", weight="10kg", flag="小型犬", name="n/a"):
        super().__init__(name)    # super_life.__init__(self,name)
        self.color = color
        self.height = height
        self.weight = weight
        self.flag = flag

    def doit(self, msg):
        print(f"主人我叫'{self.name}', 我会'{msg}' ")

    def show(self):
        return f"这是我的信息:皮肤{self.color}\t身高{self.height}\t体重{self.weight}\t{self.flag}"


