import numpy as np

class Algorithms_Math:
    def __init__(self):
        pass
    def BAOAlgorithms(self):
        pass
    def CreaArr(self, array, value = 1, index = 2, border = False, left = 0, right = 0, top = 0, bottom = 0, typedata = "tup"):
        return Algorithms_Math.CreNewMatrixLike(array, value, index, border, left, right, top, bottom, typedata);
    def Convolution (self, image, kernel):
        
    @staticmethod
    def CreNewMatrixLike (array, value = 1, index = 2, border = False, left = 0, right = 0, top = 0, bottom = 0, typedata = "tup"):
        w = h = c = 0;
        ketqua = None;
        if index == 3:
            ketqua = tuple(tuple(tuple()));
            h, w , c = array.shape
        else:
            ketqua = tuple(tuple());
            h, w = array.shape
        if value is (-1):
            if c == 0:
                for he in range(0, h):
                    ketqua = (array[he, :], )
            else:
                for he in range(0, h):
                    ketqua = (array[he, :, :], )
        else:
            if c == 0:
                for he in range(0, h):
                    ketqua = ( [value for i in range(0, array.shape[1])], )
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

    
    @staticmethod
    def tensordot(arr, kernel, type = "binary", mode = "sum"):
        try:
            arr_copy = Algorithms_Math.CreNewMatrixLike(arr, -1, typedata = "arr")
        except:
            pass
        if mode in {"sum", "average"}:
            sum = 0
            if type is "binary":
                for i in range(0, arr.shape[0]):
                    for j in range(0, arr.shape[1]):
                        sum += arr_copy[i, j] * kernel[i, j]
                return sum;
            elif type in {"color2D" , "gray"}:
                for i in range(0, arr.shape[0]):
                    for j in range(0, arr.shape[1]):
                        sum += arr_copy[i, j] * kernel[i, j]
                return sum / (arr_copy.shape[0] * arr_copy.shape[1])
            elif type is "color3D"
                try:
                    sum = 0
                    arr_copy = Algorithms_Math.CreNewMatrixLike(arr, -1, index = 3, typedata = "arr")
                    result = list()
                    for c in range(0, 3):
                        for i in range(0, arr.shape[0]):
                            for j in range(0, arr.shape[1]):
                                sum += arr_copy[i, j] * kernel[i, j]
                        result.append(sum / (arr_copy.shape[0] * arr_copy.shape[1]))
                    return result;
                except:
                    return None
        elif mode is "delation":
            pass
        elif mode is "colation":
            pass