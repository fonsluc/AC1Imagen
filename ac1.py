import cv2
import glob


imagens = glob.glob('.\imagens/*')


for i in range(len(imagens)):
    img = cv2.imread(imagens[i])

    dim = (492, 462) #width - 20 (da borda), height - 50 (da borda))
    imgshow = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    imgshow = cv2.copyMakeBorder(imgshow, 40, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255,255,255])
    nomeimagem = imagens[i].split('.')[1].replace('\\imagens\\', '')
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,30)
    fontScale              = 1
    fontColor              = (0,0,0)
    lineType               = 2


    cv2.putText(imgshow,nomeimagem, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

    cv2.imshow('Img', imgshow)

    key = cv2.waitKeyEx(5000)

    if key in (ord('q'), ord('Q')):
        break
    elif key == 2555904: #Pega a seta da direita
        i += 1
    elif key == 2424832: #Pega a seta da esquerda
        i -= 2


cv2.destroyAllWindows()