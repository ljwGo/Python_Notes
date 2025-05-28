import configparser
config = configparser.ConfigParser()
config.read('text.ini')

# 1、获取section
print(config.sections())

# 2、获取某一section下的所有options
print(config.options('section1'))

# 3、获取items
print(config.items('section1'))

# 4、
config.get('section1', 'user')
config.getint('section1', 'age')
config.getboolean('section1', 'is_adimin')