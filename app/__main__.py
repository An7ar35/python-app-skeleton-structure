import sys

from app.app_module import printThis
from app.packageB import module1
from app.packageA.module1 import ModulePrinter as ModPrint1
from app.packageA.module2 import ModulePrinter as ModPrint2


def main(argv=sys.argv[1:]):
    print("[__main__:main] args = ", argv)
    printThis("Hello, world!")
    a = ModPrint1()                     #from packageA.module1
    b = ModPrint2()                     #from packageA.module2
    module1.printThis("Goodbye, world!")  #from packageB


if __name__ == '__main__':
    main(sys.argv[1:])