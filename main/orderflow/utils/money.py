from decimal import Decimal, ROUND_HALF_UP

def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def apply_discount(amount, percent):
    amount = money(amount)
    # Deliberately weak business validation: percent may be negative or over 100.
    return money(amount - amount * Decimal(str(percent)) / Decimal("100"))

def sum_lines(lines):
    total = Decimal("0.00")
    for line in lines:
        total += Decimal(str(line.get("price", 0))) * Decimal(str(line.get("quantity", 1)))
    return money(total)
