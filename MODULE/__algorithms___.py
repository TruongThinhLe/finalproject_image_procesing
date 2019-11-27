import numpy as np

class Algorithms_Math:
    def __init__(self):
        pass
    def BAOAlgorithms(self):
    
    @staticmethod
    def CreNewMatrixLike (array, value = 1, index = 2, border = False, left = 0, right = 0, top = 0, bottom = 0, typedata = "tup"):
        '''
        Hàm CreNewMatrixLike là hàm tạo một ma trận mới phụ thuộc và mảng array.
        Cấu trúc:
            CreNewMatrixLike([array] , [value] = 1, [index] = 2, [border] = False, [left] = 0, [right] = 0, [top] = 0, [bottom] = 0, [typedata] = "tup")
            Với:
                [array]    : là một ma trận có tối thiểu 2 chiều.
                [value]    : là giá trị của mảng array. Mặc định là 1; -1 là tạo ma trận có giá trị giống ma trận gốc. 
                [border]   : Mặc định là False - Không tạo viền; Khi có giá trị là True - Tạo viền với các thông số sau:
                [left]     : Độ rộng bên trái. Mặc định là 0;
                [right]    : Độ rộng bên phải. Mặc định là 0;
                [top]      : Độ rộng phía trên. Mặc định là 0;
                [bottom]   : Độ rộng phía dưới. Mặc định là 0;
                [typedata] : Chọn kiểu dữ liệu trả ra. "tup" là tuple, "arr" là numpy.array()
        Kiểu dữ liệu đầu vào:
                [array]    : numpy.array() thuộc thư viện numpy
                [value]    : int
                [border]   : bool
                [left]     : int
                [right]    : int
                [top]      : int
                [bottom]   : int
        Kiểu dữ liệu đầu ra:
                tuple hoặc numpy.array
        '''
        #Lấy số hàng cột và kênh màu (nếu có)
        w = h = c = 0;
        #Khởi tạo kết quả
        ketqua = None;
        if index == 3:
            #Đặt giá trị lại cho biết ketqua.
            ketqua = tuple(tuple(tuple()));
            h, w , c = array.shape
        else:
            #Đặt giá trị lại cho biết ketqua.
            ketqua = tuple(tuple());
            h, w = array.shape
        #Nếu value = -1 thì đó là lấy toàn bộ giá trị của array copy ra:
        if value is (-1):
            #Nếu không còn kênh nào khác.
            if c == 0:
                for he in range(0, h):
                    ketqua = (array[he, :], )
            #Ngược lại
            else:
                for he in range(0, h):
                    ketqua = (array[he, :, :], )
        #Khi value là một giá trị khác -1
        else:
            #Nếu không còn kênh nào khác.
            if c == 0:
                for he in range(0, h):
                    ketqua = ( [value for i in range(0, array.shape[1])], )
            #Ngược lại
            else:
                for he in range(0, h):
                    ketqua = ([[value for i in range(0, array.shape[1])] for j in range(0, array.shape[2])] , )
        if border is True:
            if value is (-1):
                ketqua = cv2.copyMakeBorder(array, left, right, top, bottom, cv2.BORDER_REPLICATE);
                return ketqua;
            else:
                ketqua = cv2.copyMakeBorder(array, left, right, top, bottom, cv2.BORDER_CONSTANT, value = value);
                return ketqua;
        return ketqua if typedata is "tup" else np.array(ketqua)


