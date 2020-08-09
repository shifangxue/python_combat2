from hogwarts3.life.Super_life import super_life

"""
定义侠客模块
    class Swordsman ：用于描述一个剑客类
        :arg
           weapon:兵器
           kongfu:绝招
           age：年龄 
"""

class Swordsman(super_life):

    def __init__(self, weapon, kongfu, name, age):
        super_life.__init__(self, name)
        self.weapon = weapon
        self.kongfu = [kongfu]
        self.age = age

    def power(self, kongfu):
        self.kongfu.append(kongfu)
        self.weapon = "飞虹"
        print(f"闭关修练，get 新技能{self.kongfu[-1]}")

    def show(self):
        print(f"姓名：{self.name}\n年龄：{self.age}\n兵器:{self.weapon}\n技能：{self.kongfu}")