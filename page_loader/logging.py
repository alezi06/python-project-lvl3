import logging.config

CONFIG = {
    'version': 1,
    'formatters': {
        'console_formatter': {
            'format': '{levelname} - {message}',
            'style': '{'
        },
        'file_formatter': {
            'format': '{asctime} - {levelname} - {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'console_formatter'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'file_formatter',
            'filename': 'loader.log',
            'mode': 'w'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console_handler', 'file_handler']
        }
    }
}

logging.config.dictConfig(CONFIG)
