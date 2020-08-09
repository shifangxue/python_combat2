from hogwarts3.xiaoyao.AttributeError import AttributeError

class TongLao:

    def __init__(self, hp=1000, power=20):
        try:
            if power <= hp:
                self.hp = hp
                self.power = power
            else:
                print("武力值大于血量了，这已不是人，这是神。")
                raise AttributeError("属性不对")
        except SyntaxError:
            print("输入的属性值错误")

    def see_peple(self, name):
        if name.strip().upper() == "WYZ" or name.strip().upper() == "无涯子":
            print("师弟！！！！")
        elif name.strip == "李秋水":
            print("呸，贱人")
        elif name.strip() == "丁春秋":
            print("叛徒!我杀了你")
        else:
            print("赐你一道生死符，与天同寿。")

    def fight_zms(self, enemy_hp=1000, enemy_power=20):
        if enemy_power <= enemy_hp:
            self.power = self.power * 10
            self.hp = self.hp / 2
            while True:
                # print(f"童姥hp:{self.hp}\t 对手hp:{enemy_hp}")
                if self.hp <= 0 and enemy_hp <= 0:
                    print(f"童姥hp:{self.hp}\t 对手hp:{enemy_hp}")
                    print("同归于尽")
                    break

                if self.hp <= 0:
                    print(f"童姥hp:{self.hp}\t 对手hp:{enemy_hp}")
                    print("童姥返老还童了")
                    break
                if enemy_hp <= 0:
                    print(f"童姥hp:{self.hp}\t 对手hp:{enemy_hp}")
                    print("天上地下，童老独尊。")
                    break

                self.hp = self.hp - enemy_power
                enemy_hp = enemy_hp - self.power
        else:
            print("敌人太强悍，无法比划，找个人类来比武！！！")
