class Students(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if (gender == 'male' or gender == 'female'):
            self.__gender = gender
            print('set gender ok')
        else:
            print('wrong gender')

# 测试:
bart = Students('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

akie = Students('akie', 'male')
akie.set_gender('miaommiao')
print(akie.get_gender())



