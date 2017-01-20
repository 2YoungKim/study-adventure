# Unit 부모 클래스 선언
class Unit:
    def __init__(self, name, energy, is_fly):
        self.name = name        # 유닛의 이름
        self.energy = energy    # 각각의 유닛이 가지고 있는 에너지
        self.is_fly = is_fly    # 공중 유닛인가, 지상 유닛인가 (Boolean)

    def get_tribe(self):        # 어떤 종족인지?
        print(self.name + 'is a basic tribe!!')

    def get_energy(self):
        if self.energy > 0: # 에너지가 0 이상일 경우
            print(self.name + '의 현재 에너지는', self.energy , '입니다.')
        else:
            print(self.name + '유닛은 전사했습니다.')

# 테란 종족 클래스
class Terran(Unit):
    def get_tribe(self):
        print(self.name + 'is Terran!!')

    def be_attacked(self):
        self.energy -= 3

# 프로토스 종족 클래스
class Protoss(Unit):
    def get_tribe(self):
        print(self.name + 'is Protoss!!')

    def be_attacked(self):
        self.energy -= 2

# 저그 종족 클래스
class Zerg(Unit):
    def get_tribe(self):
        print(self.name + 'is Zerg!!')

    def be_attacked(self):
        self.energy -= 4

# 종족별 유닛 생성
marine = Terran('마린', 15, False)
corsair = Protoss('프로토스', 20, True)
hydra = Zerg('히드라', 10, False)

print('현재의 에너지!!! \n-------------------')
marine.get_energy()
corsair.get_energy()
hydra.get_energy()

# 게임 어택 시뮬레이션
for x in range (3):
    marine.be_attacked()
    corsair.be_attacked()
    hydra.be_attacked()
    print('\n*', x+1, '차 공격받은후의 에너지!!! \n----------------------------')
    marine.get_energy()
    corsair.get_energy()
    hydra.get_energy()

print('\nGame Over !!!')