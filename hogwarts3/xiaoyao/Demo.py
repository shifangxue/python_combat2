from hogwarts3.xiaoyao.TongLao import TongLao
from hogwarts3.xiaoyao.Xuzhu import Xuzhu
from random import randint

tstl = TongLao(1000, 20)
tstl.see_peple("丁春秋 ")
tstl.see_peple("wyz ")
tstl.fight_zms(enemy_power=randint(90, 101))

xz = Xuzhu()
xz.read()
xz.fight_zms(enemy_power=130)