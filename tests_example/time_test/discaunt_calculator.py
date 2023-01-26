import datetime


def discount_calculator(total_price: float, due_data: datetime.date, discount: float, days: int):
    diff = due_data - datetime.date.today()
    if datetime.timedelta() <= diff < datetime.timedelta(days=days):
        return total_price * (1.0 - discount)
    return total_price
