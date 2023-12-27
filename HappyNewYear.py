import random
import time

def wait():
    print("-----------------------")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

print("Chào mừng bạn đến với event cuối cùng của năm 2023")
time.sleep(4)
print("Event này như là 1 tựa game gacha nên nếu không có quà thì tại nhân phẩm thôi, đừng chửi t =))))")
time.sleep(4)
print("Ở event này, bạn sẽ chọn 1 số từ 1-10 và có thể sẽ nhận được 1 phần quà bất ngờ")
time.sleep(4)
print("Và ở cuối event này là tiết mục tìm người được chọn")
time.sleep(2)
print("Bằng cách bạn chọn 1 số ngẫu nhiên từ 1 đến 10 và nếu đúng thì bạn là người được chọn")
time.sleep(4)
print("Và khi bạn đã là người được chọn thì chắc chắn bạn cũng sẽ được nhận 1 món quà tương ứng")
time.sleep(3)
print("Sao cho xứng với danh xưng Người được chọn :D ")
time.sleep(2)
print("Oke,giờ hãy đến với tiết mục chính nào. INTRO!!")
time.sleep(4)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("VÀ Ô VĂN KÊ HÔM NAY CHÚNG TA ĐẾN VỚI EVENT CUỐI CÙNG CỦA NĂM 2023 NHAAAAAAAA!!!!!")
time.sleep(5)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("--------EVENT NĂM MỚI--------")
n = int(input("Hãy nhập 1 số từ 1 đến 10: "))
count = 0
while not (1<=n<=10):
    n = int(input("Hãy nhập 1 số từ 1 đến 10: "))
if n == 1:
    wait()
    print("Bạn đã chọn số 1: Nhắn tin cho tôi cùng với bằng chứng là ảnh chụp màn hình cái này để nhận một phần quá bí mật :)")
elif n == 2:
    wait()
    print("Bạn đã chọn số 2: Tôi sẽ tiết lộ 1 bí mật mà bạn muốn biết (nhắn tin cho tôi và phải cam kết không được kể ai khác)")
elif n == 3:
    wait()
    print("Chúc mừng bạn đã được 5k :D")
elif n == 4:
    wait()
    print("Chúc bạn may mắn năm sau")
elif n == 5:
    wait()
    print("Chúc bạn may mắn năm sau")
elif n == 6:
    wait()
    print("Chúc mừng bạn đã được 10k :D")
elif n == 7:
    wait()
    k = int(input("Hãy trả lời câu hỏi: Bạn có xem CKG hay k? (có = 1; không = 2):  "))
    if k == 1:
        print("Vậy thì nó gọi là chằng gì ạ???")
        time.sleep(1)
        print("Nó gọi là chẳng mấy khi và thực sự là 1 cái gì đấy vậy nên là nhắn tin cho tôi và chụp màn hình làm bằng chứng để nhận 1 phần quà bí mật nhá!!")
    elif k == 0:
        print("Oh nyo, chúc bạn may mắn năm sau")
elif n == 8:
    wait()
    print("Chúc bạn may mắn năm sau!!")
elif n == 9:
    wait()
    print("Chúc mừng năm mới 2024!!!")
elif n == 10:
    wait()
    print("Qua THPT Việt Đức lớp 10A4 nói Anh Triết đẹp zai để nhận 10k")
    
time.sleep(4)
print("Nếu bạn không thắng được bất cứ thứ gì ở trên thì đừng lo, vẫn còn tiết mục cuối để xem bạn có phải người được chọn không :D")

t = random.randint(1, 10)
h = int(input("Hãy nhập 1 số bất kì từ 1 đến 10: "))
if t == h:
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Chúc mừng bạn là người được chọn, hãy nhắn tin cho tôi và chụp màn hình làm bằng chứng để nhận 1 phần quà bí mật")
else:
    print("Rất tiếc bạn không phải là người được chọn!!")
    
time.sleep(2)
print("Nếu bạn không nhận được bất cứ thứ gì từ event này thì đừng buồn bởi bạn vẫn còn năm sau nha!!")
time.sleep(4)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("VÀ CUỐI CÙNG LÀ CHÚC MỪNG NĂM MỚI 2024!!!")
