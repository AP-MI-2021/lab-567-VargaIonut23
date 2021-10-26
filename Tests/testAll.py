from Tests.testCRUD import testadaugarezervare, teststergerezervare, testmodificarezervare, testgetbyid
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testadaugarezervare()
    teststergerezervare()
    testmodificarezervare()
    testgetbyid()