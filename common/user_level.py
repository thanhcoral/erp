SYSTEM_ADMIN = 0
SUB_ADMIN = 1
ACCOUNTANT = 2
AR_OFFICER = 3
AP_OFFICER = 4
PRODUCTION_MANAGER = 5
PURCHASE_MANAGER = 6
STOCK_MANAGER = 7
SALE_MAN = 8

INQUIRIES = 10


USER_LEVEL_CHOICES = (
    (SYSTEM_ADMIN, "System admin"),
    (SUB_ADMIN, "Sub admin"),
    (ACCOUNTANT, "Accountant"),
    (AR_OFFICER, "AR Officer"),
    (AP_OFFICER, "AP Officer"),
    (PRODUCTION_MANAGER, "Production manager"),
    (PURCHASE_MANAGER, "Purchase manager"),
    (STOCK_MANAGER, "Stock manager"),
    (SALE_MAN, "Sale man"),
    (INQUIRIES, "Inquiries"),
)