from Tests.testAll import runAllTests
from UserInterface.command_line_console import command_line_console
from UserInterface.console import runmenu


def main():
    runAllTests()
    lista = []
    ui = input("Introduceti ui pentru console si cil pentru command in line: ")
    while True:
        if ui == "ui":
            runmenu(lista)
            break
        elif ui == "cil":
            command_line_console(lista)
            break
        else:
            print('Optiune inexistenta')


if __name__ == "__main__":
    main()

#add,1,test,economy,300,nu,showall,delete,2
#add,1,test,economy,300,nu,showall
#update,1,test1,economy plus,100,da,showall