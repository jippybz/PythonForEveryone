Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print('jippy')
jippy
>>> print('jippy')
jippy
>>> name = 'jippy'
>>> lastname = 'brezzy'
>>> fulname = name + ' ' + lastname
>>> fullname = name + ' ' + lastname
>>> print(fullname)
jippy brezzy
>>> name = 'กนกอร'
>>> lastname = 'รัตนสมลาภ'
>>> fullname = name + lastname
>>> print(fullname)
กนกอรรัตนสมลาภ
>>> type(name)
<class 'str'>
>>> age =  10
>>> type(age)
<class 'int'>
>>> name = 'jippy'
>>> name.upper()
'JIPPY'
>>> name.lower()
'jippy'
>>> print(name)
jippy
>>> name = name.upper()
>>> print(name)
JIPPY
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อJIPPY นามสกุลรัตนสมลาภ อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ{name} นามสกุล{lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อJIPPY นามสกุลรัตนสมลาภ อายุ 10 ขวบ
