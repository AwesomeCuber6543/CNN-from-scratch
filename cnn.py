from PIL import Image
import numpy as np
import cv2

image_path = "./convolution_test.jpg"

convolution = [[-1, -2, -1], [1, -4, 1], [0, 1, 0]]


def apply_convolution(image_path, convolution):

    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    pixel_array = np.array(gray_image)
    
    new_image_array = np.zeros((len(pixel_array)//2 - 1, len(pixel_array[0])//2 - 1, 3), dtype=np.uint8)

    for i in range(0, len(pixel_array) - len(convolution), 2):
        for j in range(0, len(pixel_array[0]) - len(convolution[0]), 2):
            print(i, "COMPARED TO", len(pixel_array)//2 - 1)
            print(j >= len(pixel_array[0])//2 - 1)
            if i >= len(pixel_array)//2 - 1 or j >= len(pixel_array[0])//2 - 1:
                continue
            new_image_array[i][j] = get_filter_value(i, j, convolution, pixel_array)


    cv2.imwrite("test_image.jpg", new_image_array)

    return new_image_array


def get_filter_value(start_i, start_j, convolution, pixel_array):
    total_sum = 0

    for i in range(len(convolution)):
        for j in range(len(convolution[0])):
            total_sum += convolution[i][j] * pixel_array[start_i + i][start_j + j]


    return total_sum



if __name__ == "__main__":
    print(apply_convolution(image_path, convolution))
