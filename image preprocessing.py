from PIL import Image
import os
import xlrd

maxHeight = 94
maxWidth = 80

newWidth = 64
newHeight = 64

def convertImages():
    directory = "./OG Images"
    saveDirectory = "./testing"

    for folder in os.listdir(directory):
        for file in os.listdir(directory + "/" + folder):
            if file[-3:] == "svg" or file[-4:] == "ashx" or file[-5:] == "jpg')" or file[-3:] == "php" or file[-3:] == "asp" or file[-8:] == "gif~c200"\
                    or file[-8:] == "jpg~c200":
                print(file)
                continue

            # print(directory + "/" + folder + "/" + file)

            # if(file[-3:] == "png"):
            #     print(directory + "/" + folder + "/" + file)
            #     image = Image.open(directory + "/" + folder + "/" + file)
            #     new_image = image.convert('RBG')
            #     newImageFile = file[:-3] + "jpg"
            #     # print(newImageFile)
            #     # break
            #     new_image.save(saveDirectory + "/" + folder + "/" + newImageFile)


# check our images so i can figure out the what to resize the images and get rid of bad images
def checkPhotos():
    directory = "./dataset"
    path = "./dataset/Abra/"
    picture = "2eb2a528f9a247358452b3c740df69a0.jpg"

    minHeight = 10000
    minWidth = 10000

    image2 = Image.open(path + picture)
    width2, height2 = image2.size
    print(width2, height2)

    print("in check photos")

    for folder in os.listdir(directory):
        # print(folder)
        path = directory + "/" + folder
        for file in os.listdir(path):
            # some random image file types that PIL doesnt seem to like so we get rid of them
            try:
                # print(path+ "/" + file)
                image = Image.open(path+ "/" + file)
            except:
                print("coulnt open " + path+ "/" + file)
                # print(folder + file)
                if os.path.exists(path + "/" +file):
                    # print(file)
                    os.remove(path + "/" +file)
                    continue

            # if file[-4:] != ".jpg":
            #     # print(folder + file)
            #     if os.path.exists(path + "/" +file):
            #         # print(file)
            #         os.remove(path + "/" +file)
            #         continue
            # if file[-3:] == "svg" or file[-4:] == "ashx" or file[-5:] == "jpg')" or file[-3:] == "php" \
            #         or file[-3:] == "asp" or file[-8:] == "gif~c200" or file[-8:] == "jpg~c200" or file[-3:] == "png":
            #     print(file)
            #     if os.path.exists(path + "/" +file):
            #         print(file)
            #         os.remove(path + "/" +file)
            #         continue

            # else:
            #     image = Image.open(path + "/" + file)
            #     width, height = image.size
            #     image.close()
            #     if (int(width) < minWidth):
            #         minWidth = int(width)
            #     if (int(height) < minHeight):
            #         minHeight = int(height)
                # if (path + filename == path + picture):
                #     print(width, height)




# resize our photos to a standard size and save them to a new folder so we don't lose the originals
def resizePhotos():

    print("resize photos")

    directory = "./dataset"
    single = "./dataset/Abra/2eb2a528f9a247358452b3c740df69a0.jpg"
    saveDirectory = "./testing"

    for folder in os.listdir(directory):
        print(folder)
        dirPath = directory + "/" + folder
        savePath = saveDirectory + "/" + folder
        if not os.path.exists(saveDirectory + "/" + folder):
            os.mkdir(saveDirectory + "/" + folder)
        for file in os.listdir(dirPath):
            filePath = dirPath + "/" + file

            originalImage = Image.open(filePath)
            print(savePath + "/" + file)
            newImage = originalImage.resize((newWidth, newHeight))
            # newImage.show()
            newImage.save(savePath + "/" + file)
            # originalImage.show()
            # originalImage.close()

    # image  = Image.open(single)
    # image2 = image.resize((maxWidth, maxHeight))
    # image.show()
    # image2.show()
    # image.close()


def checkSingleImage(file:str):

    try:
        image = Image.open(file)
        print("opened " + file + " just fine")
    except:
        print("couldnt open " + file)


def addPokemonFromFile(file:str):
    print(file)

    saveDirectory = "./OG Images"

    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) != "":
            print(sheet.cell_value(i, 0))
            pokemon = sheet.cell_value(i, 0)
            if not os.path.exists(saveDirectory + "/" + pokemon):
                os.mkdir(saveDirectory + "/" + pokemon)


    # with open(file, "r") as f:
    #     for line in f:
    #         print(line)


# convertImages()
#
# checkPhotos()
# resizePhotos()


# checkSingleImage("./single/Mewtwo/00000140.jpg")
# checkSingleImage("./single/Mewtwo/00000142.jpg")


addPokemonFromFile("pokemonlist.xlsx")