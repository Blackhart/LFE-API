from datetime import datetime

from api.data.constant import DATE_FORMAT

def convert_to_datetime(date_string):
    """ Convert a date string to a datetime object
    
    convert_to_datetime() parses a string representing a time according to a format.
    format should be of the form 'AAAA-MM-DD'.

    Args:
        date_string (str): Date string to convert

    Returns:
        datetime: The converted datetime object
    """
    in_date_format = DATE_FORMAT
    
    return datetime.strptime(date_string, in_date_format)


def is_valid_datetime_format(date_str, date_format=DATE_FORMAT):
    """ Check if a date string is of a given format

    Args:
        date_str (str): Date string to check
        date_format (str, optional): Date format to check against. Defaults to "%Y-%m-%d".

    Returns:
        bool: True if the date string is of the given format, False otherwise
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
    
    
def get_current_date():
    """ Get the current date
    
    Date is of the form 'AAAA-MM-DD'
    
    Returns:
        str: The current date
    """
    return datetime.now().strftime(DATE_FORMAT)