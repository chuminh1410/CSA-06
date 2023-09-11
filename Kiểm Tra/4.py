class nguoi:
    def __init__(self, ten, nam_sinh, dia_chi):
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.dia_chi = dia_chi

class dan(nguoi):
    def __init__(self, ten, nam_sinh, dia_chi, nghe_nghiep, he_so_luong=4.2):
        super().__init__(ten, nam_sinh, dia_chi)
        self.nghe_nghiep = nghe_nghiep
        self.he_so_luong = he_so_luong

    def tinh_luong(self):
        luong_co_ban = 1000
        return self.he_so_luong * luong_co_ban

    def hien_thi_thong_tin(self):
        print(f'Tên: {self.ten}')
        print(f'Năm sinh: {self.nam_sinh}')
        print(f'Địa chỉ: {self.dia_chi}')
        print(f'Nghề nghiệp: {self.nghe_nghiep}')
        print(f'Hệ số lương: {self.he_so_luong}')

class can_bo(nguoi):
    def __init__(self, ten, nam_sinh, dia_chi, chuc_vu, hoc_ham, hoc_vi, he_so_luong=8.3):
        super().__init__(ten, nam_sinh, dia_chi)
        self.chuc_vu = chuc_vu
        self.hoc_ham = hoc_ham
        self.hoc_vi = hoc_vi
        self.he_so_luong = he_so_luong

    def tinh_luong(self):
        luong_co_ban = 1000
        return self.he_so_luong * luong_co_ban

def nhap_thong_tin():
    ten = input("Nhập tên: ")
    nam_sinh = input("Nhập năm sinh: ")
    dia_chi = input("Nhập địa chỉ: ")
    chuc_vu = input("Nhập chức vụ: ")
    hoc_ham = input("Nhập học hàm: ")
    hoc_vi = input("Nhập học vị: ")
    return ten, nam_sinh, dia_chi, chuc_vu, hoc_ham, hoc_vi

def in_thong_tin(can_bo):
    print(f'Tên: {can_bo.ten}')
    print(f'Năm sinh: {can_bo.nam_sinh}')
    print(f'Địa chỉ: {can_bo.dia_chi}')
    print(f'Chức vụ: {can_bo.chuc_vu}')
    print(f'Học hàm: {can_bo.hoc_ham}')
    print(f'Học vị: {can_bo.hoc_vi}')
    luong = can_bo.tinh_luong()
    print(f'Lương: {luong} $')
    
selected = can_bo(*nhap_thong_tin())
in_thong_tin(selected)
