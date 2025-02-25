import cv2
import numpy as np


def merge_surrounding_image(images):
    image = [None] * len(images)
    h = 1944
    w = 2592
    for i, img in enumerate(images):
        if img is None:
            image[i] = np.zeros([h, w, 3], dtype=np.uint8)
        elif image is not None:
            image[i] = img
    image[0] = image[0]
    image[1] = cv2.rotate(image[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[2] = cv2.rotate(image[2], cv2.ROTATE_90_CLOCKWISE)
    image[3] = cv2.rotate(image[3], cv2.ROTATE_180)

    height = max(image[1].shape[0], image[2].shape[0], image[0].shape[0] + image[3].shape[0])
    width = (image[1].shape[1] + image[0].shape[1] + image[2].shape[1])
    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    merge_image_canvas[0:image[1].shape[0], 0:image[1].shape[1]] = image[1]
    merge_image_canvas[0:image[0].shape[0], image[1].shape[1]:image[1].shape[1] + image[0].shape[1]] = image[0]
    merge_image_canvas[0:image[2].shape[0], image[1].shape[1] + image[0].shape[1]
                                            :image[1].shape[1] + image[0].shape[1] + image[2].shape[1]] = image[2]
    if image[0].shape[0] + image[3].shape[0] > max(image[1].shape[0], image[2].shape[0]):
        merge_image_canvas[image[0].shape[0]:image[0].shape[0] + image[3].shape[0],
                            image[1].shape[1]:image[1].shape[1] + image[0].shape[1]] = image[3]
    else:
        merge_image_canvas[merge_image_canvas.shape[0] - image[3].shape[0]:merge_image_canvas.shape[0] - image[3].shape[0] + image[3].shape[0],
                            image[1].shape[1]:image[1].shape[1] + image[0].shape[1]] = image[3]
    return merge_image_canvas


def merge_image_left_right_surrounding_view(images):
    image = [None] * len(images)
    h = 1944
    w = 2592
    for i, img in enumerate(images):
        if img is None:
            image[i] = np.zeros([h, w, 3], dtype=np.uint8)
        elif image is not None:
            image[i] = img
    image[0] = image[0]
    image[1] = cv2.rotate(image[1], cv2.ROTATE_90_CLOCKWISE)
    image[2] = cv2.rotate(image[2], cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[3] = cv2.rotate(image[3], cv2.ROTATE_180)

    height = max(image[1].shape[0], image[2].shape[0])
    width = (image[1].shape[1] + image[2].shape[1]) + 50
    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    merge_image_canvas[0:image[1].shape[0], 0:image[1].shape[1]] = image[1]
    merge_image_canvas[0:image[2].shape[0], image[1].shape[1] + 50:image[1].shape[1] + 50 + image[2].shape[1]] = image[2]

    return merge_image_canvas
