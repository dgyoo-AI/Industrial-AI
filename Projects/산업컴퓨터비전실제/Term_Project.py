import imutils
import tkinter
import tkinter.scrolledtext as st
from tkinter import filedialog
import pytesseract

import cv2
import numpy as np
import pytesseract
from PIL import Image
from PIL import ImageTk
import os

selectImage = None
resizeImg = None
resizeRes = None
procImage = None
edgeLine = None
findContour = None
detectedContour = None
contourNum = None
selectedListnameNew = None
selectedListnameOld = None
edgeHeight = None
edgeWidth = None
edgeChannel = None
croppedImg = None
expendImg = None

IMAGE_FOLDER_PATH = '../Img'


def redraw_canvas(img):
    img = Image.fromarray(img)              # return image object
    img = ImageTk.PhotoImage(image=img)   # tkinter 호환 이미지로 변경

    width = img.width()
    height = img.height()

    imageCanvas.config(scrollregion=(0, 0, width, height))
    setResult = imageCanvas.create_image(0, 0, anchor="nw", image=img)
    imageCanvas.image = img       # for avoid garbage collector


def redraw_result(img):
    img = Image.fromarray(img)              # return image object
    img = ImageTk.PhotoImage(image=img)   # tkinter 호환 이미지로 변경

    width = img.width()
    height = img.height()

    imageResult.config(scrollregion=(0, 0, width, height))
    setResult = imageResult.create_image(0, 0, anchor="nw", image=img)
    imageResult.image = img       # for avoid garbage collector


def reload_image_list_buttoncallback():
    file_list = os.listdir(IMAGE_FOLDER_PATH)

    if imageList.size() > 0:
        for i in range(imageList.size()):
            imageList.delete(0)

    for i, filename in enumerate(file_list):
        if filename.lower().endswith(".jpg"):
            imageList.insert(i+1, filename)


def load_selected_image(filename):
    global selectImage, procImage
    global edgeHeight, edgeWidth, edgeChannel

    pathFilename = "../Img/" + filename     # 파일 경로에 한글 호환 문제로 상대경로 변경

    selectImage = cv2.imread(pathFilename)
    if selectImage is None:
        return

    procImage = selectImage.copy()
    procImage = cv2.cvtColor(procImage, cv2.COLOR_BGR2RGB)        # tkinter 색상체계로 변환 BGR -> RGB

    edgeHeight, edgeWidth, edgeChannel = selectImage.shape

    redraw_canvas(procImage)


def list_name_selectcallback(event):
    global selectedListnameNew, selectedListnameOld
    if event.widget.size() <= 0:
        return

    selectedListnameNew = event.widget.selection_get()
    load_selected_image(selectedListnameNew)

    if selectedListnameNew != selectedListnameOld:
        refresh_image()
        selectedListnameOld = selectedListnameNew


def scaleedit_move_changecallback(event):
    scaleVal = event.widget.get()

    if len(scaleEdit.get()) > 0:
        scaleEdit.delete(0, tkinter.END)
        scaleEdit.insert(0, scaleVal)
    else:
        scaleEdit.insert(0, 0)
        scaleEdit.insert(0, scaleVal)
        scaleEdit.delete(len(scaleEdit.get())-1)


def scaleedit_update_changecallback(event):
    scaleVal = event.widget.get()

    if len(scaleEdit.get()) > 0:
        scaleEdit.delete(0, tkinter.END)
        scaleEdit.insert(0, scaleVal)
        scaleInt.set(scaleVal)
    else:
        scaleEdit.insert(0, 0)
        scaleEdit.insert(0, scaleVal)
        scaleEdit.delete(len(scaleEdit.get())-1)


def sizescale_update_editentercallback(event):
    scaleInt.set(event.widget.get())


def sizescale_update_editfocusoutcallback(event):
    scaleInt.set(event.widget.get())


def refresh_image():
    global procImage, expendImg, croppedImg

    procImage = None
    imageCanvas.config(scrollregion=(0, 0, 0, 0))

    expendImg = None
    imageResult.image = None

    numberEdit.delete(0, tkinter.END)

    croppedImg = None


def resize_image_buttoncallback():
    global selectImage, procImage, resizeImg

    procImage = selectImage.copy()
    procImage = imutils.resize(procImage, width=int(scaleEdit.get()))
    resizeImg = procImage.copy()
    redraw_canvas(procImage)


def edgeminedit_move_changecallback(event):
    scaleVal = event.widget.get()

    if len(edgeEditMin.get()) > 0:
        edgeEditMin.delete(0, tkinter.END)
        edgeEditMin.insert(0, scaleVal)
    else:
        edgeEditMin.insert(0, 0)
        edgeEditMin.insert(0, scaleVal)
        edgeEditMin.delete(len(edgeEditMin.get())-1)


def edgeminedit_update_changecallback(event):
    scaleVal = event.widget.get()

    if len(edgeEditMin.get()) > 0:
        edgeEditMin.delete(0, tkinter.END)
        edgeEditMin.insert(0, scaleVal)
        edgeIntMin.set(scaleVal)
    else:
        edgeEditMin.insert(0, 0)
        edgeEditMin.insert(0, scaleVal)
        edgeEditMin.delete(len(edgeEditMin.get())-1)


def edgeminscale_update_editentercallback(event):
    edgeIntMin.set(event.widget.get())


def edgeminscale_update_editfocusoutcallback(event):
    edgeIntMin.set(event.widget.get())


def edgemaxedit_move_changecallback(event):
    scaleVal = event.widget.get()

    if len(edgeEditMax.get()) > 0:
        edgeEditMax.delete(0, tkinter.END)
        edgeEditMax.insert(0, scaleVal)
    else:
        edgeEditMax.insert(0, 0)
        edgeEditMax.insert(0, scaleVal)
        edgeEditMax.delete(len(edgeEditMax.get()) - 1)


def edgemaxedit_update_changecallback(event):
    scaleVal = event.widget.get()

    if len(edgeEditMax.get()) > 0:
        edgeEditMax.delete(0, tkinter.END)
        edgeEditMax.insert(0, scaleVal)
        edgeIntMax.set(scaleVal)
    else:
        edgeEditMax.insert(0, 0)
        edgeEditMax.insert(0, scaleVal)
        edgeEditMax.delete(len(edgeEditMax.get()) - 1)


def edgemaxscale_update_editentercallback(event):
    edgeIntMax.set(event.widget.get())


def edgemaxscale_update_editfocusoutcallback(event):
    edgeIntMax.set(event.widget.get())


def contouredit_move_changecallback(event):
    scaleVal = event.widget.get()

    if len(contourEdit.get()) > 0:
        contourEdit.delete(0, tkinter.END)
        contourEdit.insert(0, scaleVal)
    else:
        contourEdit.insert(0, 0)
        contourEdit.insert(0, scaleVal)
        contourEdit.delete(len(contourEdit.get())-1)


def contouredit_update_changecallback(event):
    scaleVal = event.widget.get()

    if len(contourEdit.get()) > 0:
        contourEdit.delete(0, tkinter.END)
        contourEdit.insert(0, scaleVal)
        contourInt.set(scaleVal)
    else:
        contourEdit.insert(0, 0)
        contourEdit.insert(0, scaleVal)
        contourEdit.delete(len(contourEdit.get())-1)


def contourscale_update_editentercallback(event):
    contourInt.set(event.widget.get())


def contourscale_update_editfocusoutcallback(event):
    contourInt.set(event.widget.get())


def filtering_image_buttoncallback():
    global procImage, resizeImg, edgeLine

    procImage = resizeImg.copy()
    procImage = cv2.cvtColor(procImage, cv2.COLOR_BGR2GRAY)  # convert to gray scale

    procImage = cv2.bilateralFilter(procImage, 11, 17, 17)  # Blur to reduce noise

    procImage = cv2.Canny(procImage, int(edgeEditMin.get()), int(edgeEditMax.get()))
    edgeLine = procImage.copy()
    redraw_canvas(procImage)


def draw_contour_image_buttoncallback():
    global procImage, edgeLine, resizeImg, findContour
    global edgeHeight, edgeWidth, edgeChannel

    procImage = edgeLine.copy()

    counts, new = cv2.findContours(procImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    orgImg = resizeImg.copy()
    cv2.drawContours(orgImg, counts, -1, (0, 255, 0), 2)

    counts = sorted(counts, key=cv2.contourArea, reverse=True)[:int(contourEdit.get())]
    findContour = counts
    orgImg = resizeImg.copy()
    cv2.drawContours(orgImg, counts, -1, (0, 255, 0), 1)
    redraw_canvas(orgImg)


def detect_contour_image_buttoncallback():
    global procImage, resizeImg, findContour, detectedContour, contourNum, selectedListnameNew

    idx = 1
    # loop over contours
    orgImg = resizeImg.copy()
    for c in findContour:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)    # approximate the contour

        if len(approx) == 4:    # chooses contours with 4 corners
            detectedContour = approx
            x, y, w, h = cv2.boundingRect(c)    # finds co-ordinates of the plate
            new_img = orgImg[y:y+h, x:x+w]
            fname, fexec = os.path.splitext(selectedListnameNew)
            cv2.imwrite('../Img/'+fname+str(idx)+'.png', new_img)   # stores the new image
            contourNum = idx
            idx += 1
            break

    #print('Contour Count : ', detectedContour)

    cv2.drawContours(orgImg, [detectedContour], -1, (0, 255, 0), 2)
    redraw_canvas(orgImg)

    detectedContour = 0


def show_target_image_buttoncallback():
    global resizeRes, selectedListnameNew, croppedImg, expendImg

    fname, fexec = os.path.splitext(selectedListnameNew)
    croppedImg = '../Img/'+fname+str(contourNum)+'.png'
    carNum = cv2.imread(croppedImg)
    expendImg = imutils.resize(carNum, width=200)
    resizeRes = expendImg.copy()

    redraw_result(expendImg)


def extract_text_image__buttoncallback():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    config = ('-l kor --oem 1 --psm 13')

    img = cv2.imread(croppedImg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    filename = "../Img/{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename), config=config)
    os.remove(filename)

    result_chars = ''
    for c in text:
        if ord('가') <= ord(c) <= ord('힣') or c.isdigit():
            result_chars += c

    numberEdit.insert(0, result_chars)


def end_dialog():
    cv2.destroyAllWindows()
    window.destroy()


# GUI Design
window=tkinter.Tk()
window.title("Image Viewer")
window.geometry("1024x768")
imageWnd_width = 800
imageWnd_height = 570
imgResult_width = 800
imgResult_height = 150

# Image canvas : Main Image
imageCanvas = tkinter.Canvas(window, relief=tkinter.SUNKEN, bd=1)
imageCanvas.config(width=imageWnd_width, height=imageWnd_height)
imageCanvas.config(highlightthickness=1)
sbarV = tkinter.Scrollbar(window, orient=tkinter.VERTICAL)
sbarH = tkinter.Scrollbar(window, orient=tkinter.HORIZONTAL)
sbarV.config(command=imageCanvas.yview)
sbarH.config(command=imageCanvas.xview)
imageCanvas.config(yscrollcommand=sbarV.set)
imageCanvas.config(xscrollcommand=sbarH.set)
sbarH.place(x=5, y=imageWnd_height, width=imageWnd_width, height=20)
sbarV.place(x=imageWnd_width + 2, y=5, width=20, height=imageWnd_height)
imageCanvas.place(x=5, y=5, width=imageWnd_width, height=imageWnd_height)
imageResult = tkinter.Canvas(window, relief=tkinter.SUNKEN, bd=1)
imageResult.config(width=imgResult_width, height=imgResult_height)
imageResult.config(highlightthickness=1)
imageResult.place(x=5, y=imageWnd_height + 50, width=imgResult_width, height=imgResult_height-50)
scaleLabel = tkinter.Label(window, text="Result Image", bd=1)
scaleLabel.place(x=5, y=imageWnd_height + 20, width=100, height=30)

# file open button
viewer_right_x = 20 + imageWnd_width
viewer_right_y = 10

imageList = tkinter.Listbox(window)
imageList.place(x=viewer_right_x, y=viewer_right_y, width=200, height=150)
imageList.bind('<ButtonRelease-1>', list_name_selectcallback)
sbarYList = tkinter.Scrollbar(window, orient=tkinter.VERTICAL)
sbarYList.place(x=viewer_right_x + 200 - 20, y=viewer_right_y, width=20, height=150)
imageList.config(yscrollcommand=sbarYList.set)
sbarYList.config(command=imageList.yview)

# load button
buttonReload = tkinter.Button(window, text="Load List", command=reload_image_list_buttoncallback)
buttonReload.place(x=viewer_right_x, y=viewer_right_y + 150, width=200, height=30)

# Image Size scale
scaleLabel = tkinter.Label(window, text="Image Size width", bd=1)
scaleLabel.place(x=viewer_right_x, y=viewer_right_y + 190, width=100, height=30)
scaleEdit = tkinter.Entry()
scaleEdit.place(x=viewer_right_x, y=viewer_right_y + 230, width=30, height=20)
scaleEdit.bind('<Return>', sizescale_update_editentercallback)
scaleEdit.bind('<FocusOut>', sizescale_update_editfocusoutcallback)
scaleVar = tkinter.IntVar()
scaleInt = tkinter.Scale(window, variable=scaleVar, orient=tkinter.HORIZONTAL, from_=400, to=600)
scaleInt.place(x=viewer_right_x + 40, y=viewer_right_y + 210, width=160, height=40)
scaleInt.bind('<B1-Motion>', scaleedit_move_changecallback)
scaleInt.bind('<ButtonRelease-1>', scaleedit_update_changecallback)
scaleInt.set(500)                       # Scale size 초기값 설정
scaleEdit.insert(0, scaleInt.get())     # Entry size 초기값 설정

# resize button
buttonResize = tkinter.Button(window, text="Resize", command=resize_image_buttoncallback)
buttonResize.place(x=viewer_right_x, y=viewer_right_y + 250, width=200, height=30)

# Filter Min,Max scale
edgeLabel = tkinter.Label(window, text="Contour Min, Max", bd=1)
edgeLabel.place(x=viewer_right_x, y=viewer_right_y + 290, width=100, height=30)
edgeEditMin = tkinter.Entry()
edgeEditMin.place(x=viewer_right_x, y=viewer_right_y + 330, width=30, height=20)
edgeEditMin.bind('<Return>', edgeminscale_update_editentercallback)
edgeEditMin.bind('<FocusOut>', edgeminscale_update_editfocusoutcallback)
edgeVarMin = tkinter.IntVar()
edgeIntMin = tkinter.Scale(window, variable=edgeVarMin, orient=tkinter.HORIZONTAL, from_=10, to=200)
edgeIntMin.place(x=viewer_right_x + 40, y=viewer_right_y + 310, width=160, height=40)
edgeIntMin.bind('<B1-Motion>', edgeminedit_move_changecallback)
edgeIntMin.bind('<ButtonRelease-1>', edgeminedit_update_changecallback)
edgeIntMin.set(10)                          # Scale Min 초기값 설정
edgeEditMin.insert(0, edgeIntMin.get())     # Entry Min 초기값 설정

edgeEditMax = tkinter.Entry()
edgeEditMax.place(x=viewer_right_x, y=viewer_right_y + 367, width=30, height=20)
edgeEditMax.bind('<Return>', edgemaxscale_update_editentercallback)
edgeEditMax.bind('<FocusOut>', edgemaxscale_update_editfocusoutcallback)
edgeVarMax = tkinter.IntVar()
edgeIntMax = tkinter.Scale(window, variable=edgeVarMax, orient=tkinter.HORIZONTAL, from_=100, to=250)
edgeIntMax.place(x=viewer_right_x + 40, y=viewer_right_y + 347, width=160, height=40)
edgeIntMax.bind('<B1-Motion>', edgemaxedit_move_changecallback)
edgeIntMax.bind('<ButtonRelease-1>', edgemaxedit_update_changecallback)
edgeIntMax.set(250)                         # Scale Max 초기값 설정
edgeEditMax.insert(0, edgeIntMax.get())     # Entry Max 초기값 설정

# filtering button
buttonFilter = tkinter.Button(window, text="Find Contour", command=filtering_image_buttoncallback)
buttonFilter.place(x=viewer_right_x, y=viewer_right_y + 390, width=200, height=30)

# contour count
contourLabel = tkinter.Label(window, text="Contour Count", bd=1)
contourLabel.place(x=viewer_right_x, y=viewer_right_y + 430, width=100, height=30)
contourEdit = tkinter.Entry()
contourEdit.place(x=viewer_right_x, y=viewer_right_y + 470, width=30, height=20)
contourEdit.bind('<Return>', contourscale_update_editentercallback)
contourEdit.bind('<FocusOut>', contourscale_update_editfocusoutcallback)
contourVar = tkinter.IntVar()
contourInt = tkinter.Scale(window, variable=contourVar, orient=tkinter.HORIZONTAL, from_=10, to=50)
contourInt.place(x=viewer_right_x + 40, y=viewer_right_y + 450, width=160, height=40)
contourInt.bind('<B1-Motion>', contouredit_move_changecallback)
contourInt.bind('<ButtonRelease-1>', contouredit_update_changecallback)
contourInt.set(10)                          # Scale Count 초기값 설정
contourEdit.insert(0, contourInt.get())     # Entry Count 초기값 설정

# draw contour button
buttonContour = tkinter.Button(window, text="Draw Contour", command=draw_contour_image_buttoncallback)
buttonContour.place(x=viewer_right_x, y=viewer_right_y + 490, width=200, height=30)

# detect Image button
buttonDetect = tkinter.Button(window, text="Detect Target", command=detect_contour_image_buttoncallback)
buttonDetect.place(x=viewer_right_x, y=viewer_right_y + 540, width=200, height=30)

# show target button
buttonShow = tkinter.Button(window, text="Show Target", command=show_target_image_buttoncallback)
buttonShow.place(x=viewer_right_x, y=imageWnd_height + imgResult_height - 55, width=200, height=30)

# extract text button
buttonExtract = tkinter.Button(window, text="Extract Text", command=extract_text_image__buttoncallback)
buttonExtract.place(x=5, y=imageWnd_height + imgResult_height + 5, width=200, height=30)

numberEdit = tkinter.Entry()
numberEdit.place(x=5 + 210, y=imageWnd_height + imgResult_height + 5, width=viewer_right_x - 230, height=30)
numberEdit.config(font=("고딕", 14))


# Exit button
buttonExit = tkinter.Button(window, text="Exit", command=end_dialog)
buttonExit.place(x=viewer_right_x, y=imageWnd_height + imgResult_height + 5, width=200, height=30)

window.mainloop()
