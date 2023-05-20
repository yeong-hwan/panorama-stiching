import os
from stitch import stitch
import cv2


def stitch_all():
    """
    1) Stitch all the images located in img_path by your algorithm
    2) Save result image to the save_path
    Notice:
        stitch() function should be used
        Your algorithm should consider multiple images (more than 2)
    """
    img_path = './test_imgs/'  # don't modify
    save_path = './img/result.jpg'  # don't modify

    img_path_list = []

    for root, subdirs, files in os.walk(img_path):
        if len(files) > 0:
            for f in files:
                fullpath = root + f
                img_path_list.append(fullpath)

    img_path_list.sort()

    # print(img_path_list)

    panorama_img = cv2.imread(img_path_list[0])
    # print(panorama_img.dtype)

    for idx in range(1, len(img_path_list)):
        dst_img = cv2.imread(img_path_list[idx])
        panorama_img = stitch(panorama_img, dst_img)

    cv2.imwrite(save_path, panorama_img)


############# don't modify #############
if __name__ == '__main__':
    stitch_all()
