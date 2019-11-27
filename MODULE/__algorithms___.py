import numpy as np

class Algorithms_Math:
    def __init__(self):
        pass
    def BAOAlgorithms(self):
        pass
    def CreaArr(array, value = 1, index = 2, border = False, left = 0, right = 0, top = 0, bottom = 0, typedata = "tup"):
        return Algorithms_Math.CreNewMatrixLike(array, value, index, border, left, right, top, bottom, typedata);
    
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

