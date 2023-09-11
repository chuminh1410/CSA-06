class hinh_chu_nhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong


chieu_dai = float(input("Chiều dài hình chữ nhật: "))
chieu_rong = float(input("Chiều rộng hình chữ nhật: "))
hinh_chu_nhat = hinh_chu_nhat(chieu_dai, chieu_rong)
print("Chu vi của hình chữ nhật là:", hinh_chu_nhat.tinh_chu_vi())
print("Diện tích của hình chữ nhật là:", hinh_chu_nhat.tinh_dien_tich())
