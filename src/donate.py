import segno
from urllib.parse import urlencode
from config import _config_
from decimal import Decimal, InvalidOperation
from time import sleep
from actions import register


@register("donate")
def donate(args):
    cfg = _config_()

    if not cfg.get("donationUPI") or not cfg.get("donationName"):
        print("Donations are not configured.")
        return

    amount = args.paths[0] if args.paths else 0

    try:
        amount = Decimal(amount)
    except (InvalidOperation, ValueError):
        print("Please enter a valid donation amount.")
        return

    if not amount.is_finite() or amount < 0:
        print("Amount must be greater than zero.")
        return

    if amount.as_tuple().exponent < -2:
        print("Amount can have at most two decimal places.")
        return

    params = {
        "pa": cfg["donationUPI"],
        "pn": cfg["donationName"],
        "am": f"{amount:.2f}",
        "cu": "INR",
        "tn": cfg.get("donationMessage", "Support Boiler"),
    }

    payment_link = "upi://pay?" + urlencode(params)

    print("\nScan this QR code using your UPI app:\n")
    segno.make_qr(payment_link).terminal(compact=True)
    print("\nPlease complete the payment in your UPI app.")
    sleep(3)
    print("\nThank you for supporting Boiler!")