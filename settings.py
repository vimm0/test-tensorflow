from apistar.parsers import JSONParser

settings = {
    # 'TEMPLATES': {
    #     'ROOT_DIR': 'templates',
    #     'PACKAGE_DIRS': ['apistar']
    # },
    'PARSERS': [JSONParser()],
}
