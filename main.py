from Tests.testAll import runAllTests
from UserInterface.command_line_console import command_line_console
from UserInterface.console import runmenu


def main():
    runAllTests()

    print("1)Interfata clasica:")
    print("2)Interfata modificata:")
    optiune =input("Dati codul de interfata pe care doriti sa o accesati: ")

    if optiune == '1':
        runmenu([])
    else:
        command_line_console([])

if __name__ == "__main__":
    main()
