import os

def facewash_image(instance, filename):
    """
    Generate a filename for a vehicle brand image and returns the path for the uploaded image.

    Args:
        instance: The instance of the vehicle brand image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/facewash"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def serum_image(instance, filename):
    """
    Generate a filename for a vehicle brand image and returns the path for the uploaded image.

    Args:
        instance: The instance of the vehicle brand image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/serum"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def moisturizer_image(instance, filename):
    """
    Generate a filename for a vehicle brand image and returns the path for the uploaded image.

    Args:
        instance: The instance of the vehicle brand image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/moisturizer"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def sunscreen_image(instance, filename):
    """
    Generate a filename for a vehicle brand image and returns the path for the uploaded image.

    Args:
        instance: The instance of the vehicle brand image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/sunscreen"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

