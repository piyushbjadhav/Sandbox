# Python Sandbox
# Author: piyush.jadhav@nyu.edu
# Description: ...
import resource


resource.setrlimit(resource.RLIMIT_RSS, (4, 4))
resource.setrlimit(resource.RLIMIT_NOFILE, (4, 4))
resource.setrlimit(resource.RLIMIT_MEMLOCK, (256, 256))
resource.setrlimit(resource.RLIMIT_NPROC, (1, 1))
resource.setrlimit(resource.RLIMIT_AS, (128 * 1024, 128 * 1024))
resource.setrlimit(resource.RLIMIT_DATA, (128 * 1024, 128 * 1024))
resource.setrlimit(resource.RLIMIT_STACK, (128 * 1024, 128 * 1024))

whitelist = {}
for name in ['False', 'None', 'True', 'abs', 'basestring', 'bool', 'callable',
             'chr', 'cmp', 'complex', 'divmod', 'float', 'hash',
             'hex', 'id', 'int', 'isinstance', 'issubclass', 'len',
             'long', 'oct', 'ord', 'pow', 'range', 'repr', 'round',
             'str', 'tuple', 'unichr', 'unicode', 'xrange', 'zip']:
    whitelist[name] = getattr(__builtins__, name)
with open("program.input") as f:
    for line in f:
        try:
            exec(line, {"__builtins__": None}, whitelist)
        except NameError, e:
            print "ERROR: ", e
        except ImportError, e:
            # User has attempted to import an unwanted/unknown module
            print "ERROR: ", e
        except ZeroDivisionError, e:
            # User has attempted to divide by zero
            print "ERROR: ", e
        except Exception, e:
            # An error other than Name, Import or ZeroDivision has occurred
            print "ERROR: ", e
