
import numpy as np
import rasterio as rs
from rasterio.plot import show


class ImageGeo:

    def __init__(self,path,nameImage):
        self.path = path
        self.nameImage = nameImage

    def openImage(self):
        newPath = self.path + "\\" + str(self.nameImage)
        img = rs.open(newPath)
        img = img.read(1)
        newimg = np.ones((img.shape[0],img.shape[1]))
        for i in range(len(img)):
            x = img[i]
            newimg[i] = x.astype(np.float32)
        nanind = np.argwhere(newimg == -9999)
        for i in range(len(nanind)):
            n = nanind[i]
            newimg[n[0]][n[1]] = np.nan
        return newimg

class CalculateProp:

    def __init__(self,B1,B5):
        self.B1 = B1
        self.B5 = B5

    def NDWI(self):
        ima01 = self.B1 - self.B5
        ima02 = self.B1 + self.B5
        ndwi = np.divide(ima01,ima02)
        return ndwi

def main():
    path = "C:\\Users\\Micael Broggio\\OneDrive\\oceanografia\\simcosta\\modcosta\\riogrande_rs_estuario\\batimetria\\imagens_landsat8_oli"
    name = "LC08_L1TP_221081_20211124_20211201_01_T1_sr_band1.tif"
    B1 = ImageGeo(path,name)
    B1 = B1.openImage()

    name = "LC08_L1TP_221081_20211124_20211201_01_T1_sr_band5.tif"
    B5 = ImageGeo(path,name)
    B5 = B5.openImage()

    imaRes = CalculateProp(B1,B5)
    np.seterr(invalid='ignore')
    imaRes = imaRes.NDWI()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
