# 41. super 다중상속

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyalbe:
    def __init__(self):
        print("Flyable 생성자")

#두개 이상의 부모클래스로부터 다중 상속을 받는 경우
#super 사용시 순서상 맨 처음 상속받는 클래스에 대해서만 
# __init__ 메소드가 호출된다.
class FlyableUnit(Unit, Flyalbe):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyalbe.__init__(self)
# 드랍쉽
dropship = FlyableUnit()