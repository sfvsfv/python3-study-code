
def length_param(name,age, **kwargs):
    print("name:", name)
    print("age:",age)
    print("kwargs=", kwargs)

    for value,key in kwargs.items():
        print(value,key)

length_param("lin", 20, xuehao="789486", dizhi="北京")