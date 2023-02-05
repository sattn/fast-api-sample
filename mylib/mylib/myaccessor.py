from mylib.mydata import MyData

class MyAccessor:
    def __init__(self, mydata: MyData):
        self.__mydata = mydata
    
    def add(self, v) -> None:
        self.__mydata.value.append(v)
    
    def get(self) -> list[int]:
        return self.__mydata.value

    def print(self) -> None:
        print(self.__mydata.value)
