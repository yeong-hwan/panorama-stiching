import numpy as np
from get_coord import get_coord
from homography import get_homography, ransac
from warp import warp


def stitch(src_img, dst_img):
    """
    1) Manually indicate corresponding points
    2) Find src_img -> dst_img homography matrix
    3) Warp src_img and stitch with dst_img
    Args:
        src_img: np.ndarray with shape (src_h,src_w,c)
        dst_img: np.ndarray with shape (dst_h,dst_w,c)
    Returns:
        src,dst stitched image. np.ndarray with shape (target_h,target_w,c)
    Notice:
        get_homography() or ransac() function should be used for computing homography
        warp() function should be used for warping an image
    """

    src_points, dst_points = get_coord(src_img, dst_img)

    H = get_homography(src_points, dst_points)

    Hi = np.linalg.inv(H)
    target_h = int((src_img.shape[0] + dst_img.shape[0]) * 1)
    target_w = int((src_img.shape[1] + dst_img.shape[1]) * 1)

    warped = warp(src_img, Hi, target_h, target_w)

    result_h, result_w = dst_img.shape[:2]
    result = np.copy(warped)
    result[0:result_h, 0:result_w, :] = dst_img

    result = result.astype('uint8')

    return result
