from PIL import Image
import os

maxHeight = 94
maxWidth = 80

newWidth = 64
newHeight = 64

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

    for folder in os.listdir(directory):
        # print(folder)
        path = directory + "/" + folder
        for file in os.listdir(path):
            # some random image file types that PIL doesnt seem to like so we get rid of them
            if file[-3:] == "svg":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue
            if file[-4:] == "ashx":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue
            if file[-3:] == "php":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue
            if file[-3:] == "asp":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue
            if file[-5:] == "jpg')":
                print(file)
                if os.path.exists(path + "/" + file):
                    print(file)
                    os.remove(path + "/" + file)
                    continue
            if file[-8:] == "gif~c200":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue
            if file[-8:] == "jpg~c200":
                print(file)
                if os.path.exists(path + "/" +file):
                    print(file)
                    os.remove(path + "/" +file)
                    continue

            else:
                image = Image.open(path + "/" + file)
                width, height = image.size
                image.close()
                if (int(width) < minWidth):
                    minWidth = int(width)
                if (int(height) < minHeight):
                    minHeight = int(height)
                # if (path + filename == path + picture):
                #     print(width, height)

    print(minWidth, minHeight)




    print(278 / 238)
    print(4/3)


# resize our photos to a standard size and save them to a new folder so we don't lose the originals
def resizePhotos():
    directory = "./dataset"
    single = "./dataset/Abra/2eb2a528f9a247358452b3c740df69a0.jpg"
    saveDirectory = "./testing"

    for folder in os.listdir(directory):
        print(folder)
        dirPath = directory + "/" + folder
        savePath = saveDirectory + "/" + folder
        # os.mkdir(saveDirectory + "/" + folder)
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

# checkPhotos()
resizePhotos()