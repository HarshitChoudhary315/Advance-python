from MarksheetBean import MarksheetBean
from MarksheetModel import MarksheetModel


def  testAdd():

    bean = MarksheetBean()
    bean.set_rollNo(111)
    bean.set_name('abc')
    bean.set_maths(78)
    bean.set_physics(76)
    bean.set_chemistry(56)

    model = MarksheetModel()
    model.add(bean)

#testAdd()

def testUpdate():
    bean = MarksheetBean()

    bean.set_id(1)
    bean.set_rollNo(101)
    bean.set_name("Harshit")
    bean.set_physics(80)
    bean.set_chemistry(85)
    bean.set_maths(90)
    model = MarksheetModel()
    model.Update(bean)

testUpdate()

