# config.py - Configuration file
"""
Product configuration and test data
"""

# Product catalog - maps product names to their expected properties
PRODUCTS = {
    "HUMMUS": {
        "name": "חומוס",
        "index": 0,
        "price": "30"
    },
    "SHAKSHUKA": {
        "name": "שקשוקה",
        "index": 1,
        "price": "40"
    },
    "PITA": {
        "name": "פיתה",
        "index": 2,
        "price": "2"
    },
    "FALAFEL": {
        "name": "פלאפל",
        "index": 3,
        "price": "20"
    },
    "FALAFEL_BALLS": {
        "name": "חמש כדורי פלאפל",
        "index": 4,
        "price": "10"
    }
}

OPT = {
    "preparation": {
        "immediately": 0,      # מיד
        "half_hour": 1,        # חצי שעה
        "one_hour": 2,         # שעה
        "two_hours": 3         # שעתיים
    },

    "pickles": {
        "yes": 0,              # כן
        "no": 1                # לא
    },

    "chips": {
        "yes": 0,              # כן
        "no": 1                # לא
    },

    "shipping": {
        "pickup": 0,           # איסוף - ₪0
        "delivery": 1          # משלוחים - ₪10
    },

    "source": {
        "facebook": 0,         # פייסבוק
        "instagram": 1,        # אינסטגרם
        "other": 2             # אחר
    }
}
# Test constraints
MAX_ITEMS_IN_CART = 3

# URLs
PAYMENT_URL = "https://sandbox.grow.link/6f340bc4d18a0bcb559914d970ac2870-MTE4NjI"

# Test credit card
TEST_CARD = {
    "number": "4580458045804580",
    "exp_month": "03",
    "exp_year": "30",
    "cvv": "123"
}