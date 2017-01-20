class baking:
    shape = str()      # 붕어, 잉어
    dough = ''
    ingredient = ''
    star_candy = int()

    def __init__(self, name):
        self.shape = name

    def bake(self, minute):
        spent_t = minute * 60
        return spent_t

    def flip(self, num):
        for i in range(num):
            print(i + 1, '회 뒤집기')

붕어빵1 = baking()
붕어빵2 = baking()
붕어빵3 = baking('고래')
#....?