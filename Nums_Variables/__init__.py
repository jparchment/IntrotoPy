import check50

@check50.check()
def exists():
    """nums_variables.py exists."""
    check50.exists("num_variables.py")
    
@check50.check(exists)
def compiles():
    """no syntax errors in num_variables.py."""
    check50.run("python num_variables.py").exit(0)
    
#@check50.check(compiles)
#def prints_variables():
#    """prints variables"""
#   check50.run("python nums_variables.py").stdout("print(years)", "print(years_str)", print("years"), "10", "10", "20").exit(0)   
