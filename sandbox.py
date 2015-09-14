# Python Sandbox
# Author: piyush.jadhav@nyu.edu
# Description: ...
import resource


resource.setrlimit(resource.RLIMIT_NOFILE, (4, 4))
resource.setrlimit(resource.RLIMIT_NPROC, (1, 1))
resource.setrlimit(resource.RLIMIT_AS, (128 * 1024, 128 * 1024))
resource.setrlimit(resource.RLIMIT_DATA, (128 * 1024, 128 * 1024))
resource.setrlimit(resource.RLIMIT_STACK, (128 * 1024, 128 * 1024))

safe_builtins = {}
for name in ['False', 'None', 'True', 'abs', 'basestring', 'bool', 'callable',
             'chr', 'cmp', 'complex', 'divmod', 'float', 'hash',
             'hex', 'id', 'int', 'isinstance', 'issubclass', 'len',
             'long', 'oct', 'ord', 'pow', 'range', 'repr', 'round',
             'str', 'tuple', 'unichr', 'unicode', 'xrange', 'zip']:
    safe_builtins[name] = getattr(__builtins__, name)
with open("program.input") as f:
    for line in f:
        if("__" in line):
            print "Invalid Syntax, use of '__' Not allowed"
            raise SystemExit(1)
        try:
            exec(line, {"__builtins__": None}, safe_builtins)
        except NameError, e:
            print "ERROR: ", e
        except ImportError, e:
            # Invalid Import
            print "ERROR: ", e
        except Exception, e:
            # General Exeptiom
            print "ERROR: ", e
