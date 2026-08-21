from RoleBean import RoleBean
from RoleMadel import RoleModel

def  testAdd_1():

    bean = RoleBean()
    bean.set_id(1)
    bean.set_name('Harshit')
    bean.set_description('developer')

    model = RoleModel()
    model.add(bean)

def  testAdd_2():

    bean = RoleBean()
    bean.set_id(2)
    bean.set_name('Harshit')
    bean.set_description('developer')

    model = RoleModel()
    model.add(bean)



testAdd_1()
testAdd_2()

