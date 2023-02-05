import pathlib
import pickle
import sys
from injector import singleton, inject
from src.app.usecases.i_call_myaccessor import ICallMyAccessor
from mylib.myaccessor import MyAccessor
from mylib import mydata
sys.modules['mydata'] = mydata

@singleton
class CallMyAccessor(ICallMyAccessor):
    @inject
    def __init__(self):
        path = pathlib.Path('src/app/mydata.pkl')
        mydata = pickle.loads(path.read_bytes())
        self.__accessor = MyAccessor(mydata)

    def add(self, v: int) -> None:
        self.__accessor.add(v)

    def get(self) -> list[int]:
        return self.__accessor.get()

    def print(self) -> None:
        self.__accessor.print()
