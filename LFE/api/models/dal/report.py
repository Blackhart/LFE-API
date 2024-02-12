import pandas as pd

from api.models.poco.transaction import Transaction


def get_net_worth_report(bank_accounts, start_date, end_date):
    """
    Retrieves the net worth report based on the provided bank accounts, start date, and end date.

    Args:
        bank_accounts (list): A list of bank account IDs. Can be empty.
        start_date (datetime): The start date of the report. Optional, can be None.
        end_date (datetime): The end date of the report. Optional, can be None.

    Returns:
        dict: The net worth report.

    """
    filters = []
    
    if bank_accounts:
        filters.append(('bank_account__in', bank_accounts))
    else:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    
    if start_date:
        filters.append(('date__gte', start_date))
        
    if end_date:
        filters.append(('date__lte', end_date))
        
    transactions = Transaction.objects.filter(**dict(filters))
    if not transactions:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    transactions = pd.DataFrame(transactions.values('id', 'date', 'amount'))

    transactions['date'] = pd.to_datetime(transactions['date'])

    daily = transactions.groupby(transactions['date'].dt.date)[
        'amount'].sum().cumsum()
    monthly = transactions.groupby(transactions['date'].dt.to_period("M"))[
        'amount'].sum().cumsum()
    yearly = transactions.groupby(transactions['date'].dt.to_period("Y"))[
        'amount'].sum().cumsum()

    return daily, monthly, yearly
