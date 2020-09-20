import hashlib

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    # print(md5.hexdigest())
    return md5.hexdigest()

def login(user, password):
    if (db.get(user) == calc_md5(password)):
        return True
    else:
        return False

if __name__ == '__main__':
    db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')

    # 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”





