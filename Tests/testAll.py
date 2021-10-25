from Tests.testCRUD import testadaugarezervare, teststergerezervare
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testadaugarezervare()
    teststergerezervare()