class personal_information :
    def __init__(self, name, year, lop, adress):
        self.name = name
        self.year = year
        self.lop = lop
        self.adress = adress

    def in_thong_tin(self):
        print(f'Tên: {self.name}')
        print(f'Năm sinh: {self.year}')
        print(f'Lớp: {self.lop}')
        print(f'Địa chỉ: {self.adress}')

toi = personal_information("Chu Ngọc Quang Minh", 2007, "11B4", "Royal City, Hà Nội")

toi.in_thong_tin()
