

import rasterio as rs
from rasterio.plot import show


class ImagyGeo:

    def __init__(self,path,nameImage):
        self.path = path
        self.nameImage = nameImage

    def openImage(self):
        newPath = self.path + "\\" + str(self.nameImage)
        img = rs.open(newPath)
        return img

def main():
    path = "C:\\Users\\Micael Broggio\\OneDrive\\oceanografia\\simcosta\\modcosta\\riogrande_rs_estuario\\batimetria\\imagens_landsat8_oli"
    name = "LC08_L2SP_221081_20211124_20211201_02_T1_SR_B1.tif"
    imagemB1 = ImagyGeo(path,name)
    imagemB1 = imagemB1.openImage()
    imagemB1 = imagemB1.read(1)

    name = "LC08_L2SP_221081_20211124_20211201_02_T1_SR_B5.tif"
    imagemB5 = ImagyGeo(path,name)
    imagemB5 = imagemB5.openImage()
    imagemB5 = imagemB5.read(1)

    imagemResult = imagemB1 + imagemB5
    show(imagemResult)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
