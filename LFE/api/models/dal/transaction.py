from api.core.uuid import generate_time_based_uuid
from api.core.date import convert_to_datetime
from api.models.poco.transaction import Transaction


def record_transaction(date, label, amount, bank_account_id):
    """ Record a transaction
    
    Args:
        date (str): Date of the transaction. Should be of the form 'AAAA-MM-DD'
        label (str): Label of the transaction
        amount (float): Amount of the transaction
        bank_account_id (str): Bank account ID to link to

    Returns:
        Transaction: The created transaction
    """
    uid = generate_time_based_uuid()

    return Transaction.objects.create(id=uid, date=date, label=label, amount=amount, bank_account_id=bank_account_id)
