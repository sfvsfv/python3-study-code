'''
构造学院人员的信息类，要求人员信息包括姓名、年龄、员工号、性别，并定义增、删、改、查方法，以及输出的方法。
'''

class Emp:
    def __init__(self,id,name,age,sex):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return "工号："+self.id+"--"+"姓名："+self.name+"--"+"年龄："+self.age+"--"+"性别："+self.sex+"--"
# from Emp import Emp
class EmpTest:
    arr = []
    var = 1
    while var == 1:
        print ('《欢迎来到员工管理系统》')
        print ('请输入以下数字：')
        print ('1、员工录入')
        print ('2、查询员工信息')
        print ('3、修改员工信息')
        print ('4、删除')
        print ('5、根据工号查看')
        print ('6、退出')
        s = input('请输入一个数字（1~6）：')

        while s == "1":
            print ('请分别输入员工的工号、姓名、年龄、性别、工资(添加信息):')
            id = input("请输入工号：")
            for x in arr:
                if x.id == id:
                    print ("该工号已经存在")
                    id = input("请输入新工号：")

            name = input("请输入姓名")
            age = input("请输入年龄")
            sex = input("请输入性别")

            emp = Emp(id, name, age, sex)
            arr.append(emp)

            break

        while s == "2":

            for x in arr:
                print(x)
            break
        while s == "3":

            id = input("请输入工号（修改其信息：）")
            name = input("请输入姓名")
            age = input("请输入年龄")
            sex = input("请输入性别")

            for x in arr:
                if x.id == id:
                    x.name = name
                    x.age = age
                    x.sex = sex
                    print ("修改成功")
            break
        while s == "4":
            id = input('请输入员工的工号（删除）：')
            for x in arr:
                if x.id == id:
                    arr.remove(x)
                    print ("删除成功")
            break


        while s == "5":
            id = input("请分别输入员工的工号（根据工号查看）：")
            for x in arr:
                if x.id == id:
                    print(x)
            break
        while s == "6":
            print('已成功退出')
            var = 0
            break