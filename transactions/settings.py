from decimal import Decimal

from django.conf import settings

transactions_BILL_NUMBER_LENGTH = getattr(settings, 'transactions_BILL_NUMBER_LENGTH', 10)
transactions_INVOICE_NUMBER_LENGTH = getattr(settings, 'transactions_INVOICE_NUMBER_LENGTH', 10)
transactions_FORM_INPUT_CLASSES = getattr(settings, 'transactions_FORM_INPUT_CLASSES', 'input')
transactions_CURRENCY_SYMBOL = getattr(settings, 'transactions_CURRENCY_SYMBOL', '$')
transactions_SPACED_CURRENCY_SYMBOL = getattr(settings, 'transactions_SPACED_CURRENCY_SYMBOL', False)
transactions_SHOW_FEEDBACK_BUTTON = getattr(settings, 'transactions_SHOW_FEEDBACK_BUTTON', False)
transactions_FEEDBACK_EMAIL_LIST = getattr(settings, 'transactions_FEEDBACK_EMAIL_LIST', [])
transactions_FEEDBACK_FROM_EMAIL = getattr(settings, 'transactions_FEEDBACK_FROM_EMAIL', None)
transactions_VALIDATE_SCHEMAS_AT_RUNTIME = getattr(settings, 'transactions_VALIDATE_SCHEMAS_AT_RUNTIME', False)
transactions_LOGIN_URL = getattr(settings, 'transactions_LOGIN_URL', settings.LOGIN_URL)

transactions_TRANSACTION_MAX_TOLERANCE = getattr(settings,
                                                  'transactions_TRANSACTION_MAX_TOLERANCE',
                                                  Decimal('0.02'))

transactions_TRANSACTION_CORRECTION = getattr(settings,
                                               'transactions_TRANSACTION_CORRECTION',
                                               Decimal('0.01'))

transactions_FINANCIAL_ANALYSIS = {
    'ratios': {
        'current_ratio': {
            'good_incremental': True,
            'ranges': {
                'healthy': 2,
                'watch': 1,
                'warning': .5,
                'critical': .25
            }
        },
        'quick_ratio': {
            'good_incremental': True,
            'ranges': {
                'healthy': 2,
                'watch': 1,
                'warning': .5,
                'critical': .25
            }
        },
        'debt_to_equity': {
            'good_incremental': False,
            'ranges': {
                'healthy': 0,
                'watch': .25,
                'warning': .5,
                'critical': 1
            }
        },
        'return_on_equity': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .07,
                'warning': .04,
                'critical': .02
            }
        },
        'return_on_assets': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
        'net_profit_margin': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
        'gross_profit_margin': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
    }
}
