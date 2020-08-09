from hogwarts3.life.Dog import Dog
from hogwarts3.life.Swordsman import Swordsman


dog = Dog("white", "36cm", "15kg", "小型犬", "小白")
dog.doit("接飞盘")
print(dog.show(), "\n")

linghuchong = Swordsman("铁剑", "华山剑法", "linghuchong", 31)
linghuchong.power("独孤九剑")
linghuchong.show()
