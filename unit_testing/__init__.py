"""
unittest supports: 
    - test automation
    - setUp (and shutdown) sharing
    - aggregation of tests into collections ...
    - independence of tests from reporting framework ...
    
to achieve above, it supports some concepts in an OO way: 
    - test fixture:- setUp and/or tear-down needed to perform tests.
    - test case:- the individual unit of testing
    - test suite:- collection of test cases and/or test suites
    - test runner:- orchestrator component
    
unittest.main()
    
"""

a = 3
print('init the module!') 
