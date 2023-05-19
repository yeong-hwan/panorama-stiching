import numpy as np


def get_homography(src_points, dst_points):
    """
    Solve for the homography given arbitrary number of point correspondences
    
    Args:
        src_points: np.ndarray with shape (num_points,2), 2=> xy(or wh) axis
        dst_points: np.ndarray with shape (num_points,2), 2=> xy(or wh) axis
        (i)th correspondence: src_points[i] <-> dst_points[i]
    Returns:
        Homography matrix H: H(src)->dst
        np.ndarray with shape (3,3)

    Notice:
        H[2,2] should be scaled to 1.0
    """

    N = len(src_points)

    xy_1 = src_points
    xy_2 = dst_points

    # test for n(len) = 8 -> (2n = 16)
    len_of_pair = len(xy_1)

    # 1. make A
    A = np.empty((0, 8))

    for idx_a in range(len_of_pair):
        A = np.append(A, np.array([[xy_1[idx_a][0], xy_1[idx_a][1], 1, 0, 0, 0, -
                      xy_1[idx_a][0] * xy_2[idx_a][0], -xy_1[idx_a][1] * xy_2[idx_a][0]]]), axis=0)
        A = np.append(A, np.array([[0, 0, 0, xy_1[idx_a][0], xy_1[idx_a][1], 1, -
                      xy_1[idx_a][0] * xy_2[idx_a][1], -xy_1[idx_a][1] * xy_2[idx_a][1]]]), axis=0)

    A = A.astype(int)

    # 2. make B
    B = np.empty((0, 1))

    for idx_b in range(len_of_pair):
        B = np.append(B, np.array([[xy_2[idx_b][0]]]), axis=0)
        B = np.append(B, np.array([[xy_2[idx_b][1]]]), axis=0)


    # 3. caculate H by A, B
    At = np.transpose(A)

    part_A = At.dot(A)
    part_B = At.dot(B)

    H = np.linalg.inv(part_A).dot(part_B)
    H = np.transpose(H)[0]
    H = np.append(H, 1)
    H = np.reshape(H, (3, 3))

    return H


