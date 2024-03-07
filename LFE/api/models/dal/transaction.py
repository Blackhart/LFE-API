from api.core.uuid import generate_time_based_uuid
from api.models.poco.transaction import Transaction


def record_transaction(date, label, amount, bank_account):
    """ Record a transaction

    Args:
        date (str): Date of the transaction. Should be of the form 'AAAA-MM-DD'
        label (str): Label of the transaction
        amount (float): Amount of the transaction
        bank_account (BankAccount): Bank account to link to

    Returns:
        Transaction: The created transaction
    """
    uid = generate_time_based_uuid()

    return Transaction.objects.create(
        id=uid,
        date=date,
        label=label,
        amount=amount,
        bank_account=bank_account
    )


def delete_transaction(id):
    """ Delete a transaction

    Args:
        id (str): ID of the transaction
    """
    transaction = Transaction.objects.get(id=id)

    transaction.delete()


def update_transaction(id, date, label, amount, bank_account):
    """ Update a transaction

    Args:
        id (str): ID of the transaction
        date (str): Date of the transaction. Should be of the form 'AAAA-MM-DD'
        label (str): Label of the transaction
        amount (float): Amount of the transaction
        bank_account (BankAccount): Bank account to link to
    """
    transaction = get_transaction(id)

    transaction.date = date
    transaction.label = label
    transaction.amount = amount
    transaction.bank_account = bank_account
    transaction.save()


def get_transaction(id):
    """ Get a transaction by ID

    Args:
        id (str): ID of the transaction

    Returns:
        Transaction: The transaction
    """
    return Transaction.objects.get(id=id)


def is_transaction_exists(id):
    """ Check if a transaction exists

    Args:
        id (str): ID of the transaction

    Returns:
        bool: True if the transaction exists, False otherwise
    """
    return Transaction.objects.filter(id=id).exists()
