class Person:
    def __init__(self,code,name,family):
        self.code=code
        self.name=name
        self.family=family
    def __str__(self):
        return f'code={self.code},name={self.name}'    
p1=Person(100,'a','b')
print(p1)