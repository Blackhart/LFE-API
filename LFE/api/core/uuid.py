import uuid

def generate_time_based_uuid():
    """ Generate a time-based UUID

    Returns:
        str: The generated UUID
    """
    return uuid.uuid1().hex