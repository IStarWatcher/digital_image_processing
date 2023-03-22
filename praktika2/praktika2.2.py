import cv2
import argparse
import numpy as np
import imutils

def task2():
    path = './praktika2/Image_1/'

    def set_image(image):
        return cv2.imread(path + image)
    
    def fragment_search():
        for i in range(1, 11):
            image = set_image('IMAGE.jpg')
            fragment = set_image(f'Et_{i}.jpg')
            (fragmentHeight, fragmentWidth) = fragment.shape[:2]
            # Осуществляем поиск фрагмента на изображении
            result = cv2.matchTemplate(image, fragment, cv2.TM_CCOEFF)
            (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
            # Выделяем искомый фрагмент и отделяем его от изображения
            topLeft = maxLoc
            botRight = (topLeft[0] + fragmentWidth, topLeft[1] + fragmentHeight)
            roi = image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
            # Создаем затемненный прозрачный слой, для затемнения всей части изображения
            mask = np.zeros(image.shape, dtype="uint8")
            image = cv2.addWeighted(image, 0.20, mask, 0.75, 0)
            # Возвращаем искомый фрагмент в изображение
            image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
            # Вывод фрагмента и изображения в отдельные окна (закрываются при нажатии любой клавиши на клавиатуре)
            cv2.imshow(f"Image{i}", imutils.resize(image, height=900))
            cv2.imshow(f"Et_{i}", fragment)
            cv2.waitKey(0)

            #path_result = r'./result/'
            cv2.imwrite(f"./praktika2/result/fragment_search{i}.jpg", image)
            
    
    fragment_search()

task2()