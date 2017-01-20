# 다형성
# Developer 부모 클래스 선언
class Developer:
    def __init__(self, name):
        self.name = name

    def coding(self):
        print(self.name, 'is developer!!')

# Python Developer 자식 클래스 선언
class PythonDev(Developer):
    def coding(self):
        print(self.name, 'is Python Dev!!')

# JAVA Dev 자식 클래스 선언
class JavaDev(Developer):
    def coding(self):
        print(self.name, 'is JAVA Dev!!')


# C++ Dev 자식 클래스 선언
class CPPDev(Developer):
    def coding(self):
        print(self.name, 'is C++ Dev!!')

# RoR Dev 자식 클래스 선언
class RoRDev(Developer):
    def coding(self):
        print(self.name, 'is Ruby on Rails Dev!!')

pd = PythonDev('찬영이')
jd = JavaDev('준영이')
cd = CPPDev('채영이')
rd = RoRDev('성훈이')

pd.coding()
jd.coding()
cd.coding()
rd.coding()

