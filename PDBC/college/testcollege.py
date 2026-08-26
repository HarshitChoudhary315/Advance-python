from collegeModel import collegeModel


def testadd1():
    param = {}
    param['id'] = 1
    param['name'] = 'Harshit'
    param['address'] = 'Naryiakheda'
    param['state'] = 'madhya pradesh'
    param['city'] = 'dewas'
    param['phoneNo'] = '9770343083'
    print(param)
    model = collegeModel()
    model.add(param)
#testadd1()
def testadd2():
    param = {}
    param['id'] = 2
    param['name'] = 'amit'
    param['address'] = 'riva'
    param['state'] = 'madhya pradesh'
    param['city'] = 'dewas'
    param['phoneNo'] = '9770343083'
    model = collegeModel()
    model.add(param)
#testadd2()

def testadd3():
    param = {}
    param['id'] = 3
    param['name'] = 'kabir'
    param['address'] = 'indore'
    param['state'] = 'madhya pradesh'
    param['city'] = 'indore'
    param['phoneNo'] = '9772243083'
    model = collegeModel()
    model.add(param)
#testadd3()



def testupdate1():
    param = {}
    param['id'] = 1
    param['name'] = 'Harshit'
    param['address'] = 'Naryiakheda'
    param['state'] = 'madhya pradesh'
    param['city'] = 'indore'
    param['phoneNo'] = '9770343083'
    print(param)
    model = collegeModel()
    model.add(param)
#testupdate1()

def testDelete():
    model = collegeModel()
    model.delete(3)
#testDelete()

def testRead():

    param = {}

    param['name'] = 'H'
    param['address'] = 'N'
    param['pageNo'] = 1
    param['pageSize'] = 2

    model = collegeModel()
    model.read(param)
testRead()