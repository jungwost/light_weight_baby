class Unit:
    def __init__(self):
        print("Unit  생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class  FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super(). __init__()
        Unit. __init__(self)
        Flyable. __init__(self)
# 드랍쉽
dropship = FlyableUnit()

#2개 이상의 부모claas를 다중상속 받을때는
#  super를 쓰게되면 순서상에 맨처음에 상속받는 claas에 대해서만
# init함수가 호출된다
# 다중상속을 할때, 모든 부모 class에 대해 초기화가 필요할때
# super 함수가 아닌 부모 class를 둘다 호출해준다