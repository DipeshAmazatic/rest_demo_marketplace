import datetime

MAXIMUM_FILE_LOGS = 1024 * 1024 * 10  # 10 MB
BACKUP_COUNT = 5


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s] %(asctime)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'abc': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/dipesh/rest_demo_marketplace/src/core/logs/default.log',
            'maxBytes': MAXIMUM_FILE_LOGS,
            'backupCount': BACKUP_COUNT,
            'formatter': 'standard',
        },
        'request_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/dipesh/rest_demo_marketplace/src/core/logs/request_debug.log',
            'maxBytes': MAXIMUM_FILE_LOGS,
            'backupCount': BACKUP_COUNT,
            'formatter': 'standard',
        },
        'request_error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/dipesh/rest_demo_marketplace/src/core/logs/request_error.log',
            'maxBytes': MAXIMUM_FILE_LOGS,
            'backupCount': BACKUP_COUNT,
            'formatter': 'standard',
        },
        'mail_admins_handler': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend'
        },
    },
    # 'root': {
    #     'handlers': ['abc','request_debug_handler','request_error_handler']
    #     'level': 'DEBUG'
    # },
    'loggers': {
        'requestlogger': {
            'handlers': ['abc','request_debug_handler','request_error_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['abc'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': [
                'abc',
                'request_debug_handler',
                'request_error_handler',
                'mail_admins_handler'
            ],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}