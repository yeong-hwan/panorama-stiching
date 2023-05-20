import numpy as np

def warp(src_img, H, target_h, target_w):
    """
    Warp src_img (using homography matrix H) to the target plane
    with a window size=(target_h,target_w)

    Args:
        src_img: np.ndarray with shape (src_h,src_w,c)
        H: np.ndarray with shape (3,3)
        target_h: int
        target_w: int
    Returns:
        Warped src image
        np.ndarray with shape (target_h,target_w,c)
    Notice:
        RGB value of non-overlapping location between warped src_img
            and target plane can be repersented as [0,0,0](=black)
        hint) torch.nn.functional.grid_sample
    """

    warped = np.zeros((target_h, target_w, 3), np.float32)

    # Make warping source
    for y in range(0, target_h):
        for x in range(0, target_w):
            pixel = np.array([[x], [y], [1]])

            # Resource_pixel = np.asarray(np.asmatrix(inv_my_homo) * np.asmatrix(pixel))
            resource_pixel = np.asarray(np.asmatrix(
                H) * np.asmatrix(pixel))

            # Coordinate scale
            trans_x = resource_pixel[0][0] / resource_pixel[2][0]
            trans_y = resource_pixel[1][0] / resource_pixel[2][0]

            # match error exception by continue
            if (trans_x < 0 or trans_y < 0
                    or trans_x > src_img.shape[1] - 1 or trans_y > src_img.shape[0] - 1):
                continue

            # int, decimal division
            tx = int(trans_x)
            ty = int(trans_y)
            a = trans_x - tx
            b = trans_y - ty

            # Bilinear Interpolation
            warped[y][x] = ((((1.0 - a) * (1.0 - b)) * src_img[ty][tx])
                            + ((a * (1.0 - b)) * src_img[ty][tx + 1])
                            + ((a * b) * src_img[ty + 1][tx + 1])
                            + (((1.0 - a) * b) * src_img[ty + 1][tx]))

    warped = warped.astype(int)

    return warped