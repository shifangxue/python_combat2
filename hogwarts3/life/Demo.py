from hogwarts3.life.Dog import Dog
from hogwarts3.life.Swordsman import Swordsman
from hogwarts3.xiaoyao.TongLao import TongLao
from hogwarts3.xiaoyao.Xuzhu import Xuzhu
from random import randint

dog = Dog("white", "36cm", "15kg", "小型犬", "小白")
dog.doit("接飞盘")
print(dog.show(), "\n")

linghuchong = Swordsman("铁剑", "华山剑法", "linghuchong", 31)
linghuchong.power("独孤九剑")
linghuchong.show()
print("\n")

tstl = TongLao(1000, 20)
tstl.see_peple("丁春秋 ")
tstl.see_peple("wyz ")
tstl.fight_zms(enemy_power=randint(90, 101))

xz = Xuzhu()
xz.read()