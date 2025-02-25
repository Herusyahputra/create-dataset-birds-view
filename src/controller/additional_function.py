import cv2


def remap_image(image, map_x, map_y):
    """
    The purpose is to generate a pair of X-Y Maps for the specified zenith angle, azimuthal angle,
    and zoom factor. The result X-Y Maps can be used later to remap the original fish-eye image to
    the target angle image with undistortion result.

    Args:
        image: Input image
        map_x: The mapping function in the x direction.
        map_y: The mapping function in the y direction.

    Returns:
        image: Updating the image after remapping

    - Example:

    .. code-block:: python

        image_anypoint = remap_image(image, mapX_anypoint, mapY_anypoint)
    """
    image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
    return image


def cropping_image(image, right, bottom, left, top):
    """
    Cropping image by ratio from every side.

    Args:
        image: Input image
        right: ratio of right side (1-0)
        bottom: ratio of bottom side (1-0)
        left: ratio of left side (0-1)
        top: ratio of top side (0-1)

    Returns:
        image has already cropping

    """
    a_left = round(image.shape[1] * right)
    a_top = round(image.shape[0] * bottom)
    a_cols = round(image.shape[1] * left)
    a_rows = round(image.shape[0] * top)
    return image[a_rows:a_rows + a_top, a_cols:a_cols + a_left]
