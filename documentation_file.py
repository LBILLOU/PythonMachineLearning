import random
import sys
import os
from string import maketrans


# Built-in functions functions
def builtinAbs():
    print '-- abs(x) --'
    print 'Returns absolut value of x.'
    x = -666
    print '-> x =', x
    print '->', abs(x)
    return abs(x) == 666


def builtinAll():
    print '-- all(iterable) --'
    print 'Returns True if searched element is in iterable.'
    print '-> all(elem == \'F\' for elem in \'FFFF\')'
    print '->', all(elem == 'F' for elem in 'FFFF')
    return all(elem == 'F' for elem in 'FFFF')


def builtinAny():
    print '-- any(iterable) --'
    print 'Returns True if searched element is in iterable.'
    print '-> any(elem == \'o\' for elem in \'Dog\')'
    print '->', any(elem == 'o' for elem in 'Dog')
    return any(elem == 'o' for elem in 'Dog')


def builtinApply():
    print '-- apply --'
    print 'Deprecated since Python 2.3'
    return True


def builtinBasestr():
    print '-- basestring --'
    print 'Superclass of str and unicode, eventually used for tests.',
    print 'Cannot be called or instantiated.'
    return True


def builtinBin():
    print '-- bin(x) --'
    print 'Converts an integer number to a binary string.'
    x = 11
    print '-> x =', x
    print '->', bin(x)
    return bin(x) == '0b1011'


def builtinBool():
    print '-- bool(x) --'
    print 'Returns a boolean value of x.'
    x = 1
    print '-> x =', x
    print '->', bool(x)
    return bool(x)


def builtinBuffer():
    print '-- buffer(object) --'
    print 'Creates a new buffer object which references the object argument'
    return True


def builtinBytearr():
    print '-- bytearray(...) --'
    print 'Returns a new array of bytes'
    return True


def builtinBytes():
    print '-- bytes --'
    print 'Returns a new byte object.'
    return True


def builtinCall():
    print '-- callable(object) --'
    print 'Returns true if object is callable (instance of a class).'
    return True


def builtinChr():
    print '--  chr(x) --'
    print 'Returns the string of ASCII code the integer x.'
    x = 97
    y = 66
    z = 2
    print '-> x =', x, y, z
    print '->', chr(x), chr(y), chr(z)
    return chr(x) == 'a'


def builtinClassm():
    print '-- classmethod(function) --'
    print 'Returns a class method for function.'
    return True


def builtinCmp():
    print '-- cmp(x,y) --'
    print 'Compares x and y. Returns negative if x < y, zero if x == y or',
    print 'positive if x > y.'
    x = 12
    y = 15
    print '-> x =', x, ', y =', y
    print '-> cmp(x,y), cmp(y,x), cmp(x,x)'
    print '->', cmp(x, y), cmp(y, x), cmp(x, x)
    return cmp(x, y) < 0


def builtinCoerce():
    print '-- coerce (x, y) --'
    print 'Returns a tuple of two numeric arguments converted to a common',
    print ' type.'
    return True


def builtinCompile():
    print '-- compile(source) --'
    print 'Compiles the source into a code.'
    return True


def builtinComplex():
    print '-- complex(x) --'
    print 'Returns the complex form of x.'
    x = 2
    y = '7+3j'
    print '-> x =', x, ', y =', y
    print '->', complex(x), complex(y)
    return True


def builtinCopyr():
    print '-- copyright --'
    print 'Displays copyright relative text in a pager-like fashion.'
    return True


def builtinCredits():
    print '-- credit --'
    print 'Displays credit relative text in a pager-like fashion.'
    return True


def builtinDelattr():
    print '-- delattr(object, name) --'
    print 'Relative of setattr(), the function deletes the named attribute',
    print ' provided with a gicen object.'
    return True


def builtinDict():
    print '-- dict() --'
    print 'Creates a new dictionary.'
    print '-> new_dict = dict()'
    new_dict = dict()
    print '->', new_dict
    return True


def builtinDir():
    print '-- dir(object) --'
    print 'Returns valid attributes of object.'
    return True


def builtinDivmod():
    print '-- divmod(x,y) --'
    print 'Returns quotient and remainder of the modulo division of x by y'
    return True


def builtinEnum():
    print '-- enumerate(sequence) --'
    print 'Return an enumerate object. sequence must be a sequence, ',
    print 'an iterator, or some other object which supports iteration.'
    return True


def builtinEval():
    print '-- eval(expression) --'
    print 'The expression argument is parsed and evaluated as a Python',
    print ' expression, the expression is executed in the environment where',
    print ' eval() is called. The return value is the result of the evaluated',
    print ' expression.'
    return True


def builtinExecf():
    print '-- execfile(filename) --'
    print 'Executes the file filename.'
    return True


def builtinExit():
    print '-- exit --'
    print 'Exits current running script.'
    return True


def builtinFile():
    print '-- file(name) --'
    print 'Constructor for a new file named name.'
    return True


def builtinFilter():
    print '-- filter(function, iterable) --'
    print 'Construct a list from those elements of iterable for which ',
    print 'function returns true.'
    return True


def builtinFloat():
    print '-- float([x]) --'
    print 'Return a floating point number constructed from a number or',
    print ' string x.'
    return True


def builtinFormat():
    print '-- format(value[, format_spec]) --'
    print 'Convert a value to a formatted representation.'
    return True


def builtinFroz():
    print '-- frozenset([iterable]) --'
    print 'Return a new frozenset object.'
    return True


def builtinGetattr():
    print '-- getattr(object) --'
    print 'Return the value of the named attribute of object.'
    return True


def builtinGlobals():
    print '-- globals() --'
    print 'Return a dictionary representing the current global symbol table.'
    return True


def builtinHasattr():
    print '-- hasattr(object, name) --'
    print 'Returns True if the string is in the object',
    print ' attributes'
    return True


def builtinHash():
    print '-- hash(object) --'
    print 'Returns the hash value (integers) of the object (if it has one).'
    return True


def builtinHelp():
    print '-- help(object) --'
    print 'Invokes the built-in help system for object.'
    return True


def builtinHex():
    print '-- hex(x) --'
    print 'Convert an integer number to a lowercase hexadecimal string '
    return True


def builtinId():
    print '-- id(object) --'
    print 'Return the identity of an object.'
    return True


def builtinInput():
    print '-- input([prompt]) --'
    print 'Equivalent to eval(raw_input(prompt)).',
    print 'Consider using the raw_input() function for general input',
    print ' from users.'
    return True


def builtinInt():
    print '-- int(x) --'
    print 'Return an integer object constructed from a number or string x.'
    return True


def builtinIntern():
    print '-- intern(string) --'
    print 'Enters string into a table of interned strings and returns',
    print 'the interned string.'
    return True


def builtinIsinst():
    print '-- isinstance(object,class) --'
    print 'Returns true if object is an instance of class.'
    return True


def builtinIssubc():
    print '-- issubclass(sclass,class) --'
    print 'Returns true if sclass is a subclass of class.'
    return True


def builtinIter():
    print '-- iter(...) --'
    print 'Return an iterator object.'
    return True


def builtinLen():
    print '-- len(object) --'
    print 'Returns the length of object.'
    return True


def builtinLicense():
    print '-- license --'
    print 'Displays license relative text in a pager-like fashion.'
    return True


def builtinList():
    print '-- list([iterable]) --'
    print 'Return a list whose items are the same and in the same order',
    print ' as iterable s items.'
    return True


def builtinLocals():
    print '-- locals --'
    print 'Updates and returns a dictionary representing the current local',
    print 'symbol table.'
    return True


def builtinLong():
    print '-- long(x) --'
    print 'Return a long integer object constructed from a string or number x.'
    return True


def builtinMap():
    print '-- map(function, iterable, ...) --'
    print 'Apply function to every item of iterable.'
    return True


def builtinMax():
    print '-- max(iterable[, key]) --'
    print 'Return the largest item in an iterable.'
    return True


def builtinMemview():
    print '-- memoryview(obj) --'
    print 'Return a memory view object created from the given argument.'
    return True


def builtinMin():
    print '-- min(iterable[, key]) --'
    print 'Return the smallest item in an iterable.'
    return True


def builtinNext():
    print '-- next(iterator[, default]) --'
    print 'Retrieve the next item from the iterator by calling its',
    print ' next() method.'
    return True


def builtinObject():
    print '-- object() --'
    print 'Return a new featureless object.'
    return True


def builtinOct():
    print '-- oct(x) --'
    print 'Convert an integer number to an octal string.'
    return True


def builtinOpen():
    print '-- open(filename) --'
    print 'Opens a file.'
    return True


def builtinOrd():
    print '-- ord (c) --'
    print 'Given a string of length one, return an integer representing the',
    print ' Unicode code point of the character when the argument is a',
    print ' unicode object, or the value of the byte when the argument is',
    print ' an 8-bit string.'
    return True


def builtinPow():
    print '-- pow(x, y) --'
    print 'Return x to the power y.'
    return True


def builtinPrint():
    print '-- print --'
    print 'Print objects to the stream file.'
    return True


def builtinProper():
    print '-- property([fget[, fset[, fdel[, doc]]]]) --'
    print 'Return a property attribute for new-style classes.'
    return True


def builtinQuit():
    print '-- quit --'
    print 'Quits current running script.'
    return True


def builtinRange():
    print '-- range(start, stop[, step]) --'
    print 'This is a versatile function to create lists containing',
    print ' arithmetic progressions.'
    return True


def builtinRawin():
    print '-- raw_input([prompt]) --'
    print 'If the prompt argument is present, it is written to standard',
    print ' output without a trailing newline. The function then reads a',
    print ' line from input, converts it to a string, and returns that.'
    return True


def builtinReduce():
    print '-- reduce(function, iterable[, initializer]) --'
    print 'Apply function of two arguments cumulatively to the items of',
    print ' iterable, from left to right, so as to reduce the iterable',
    print ' to a single value.'
    return True


def builtinReload():
    print '-- reload(module) --'
    print 'Reload a previously imported module.'
    return True


def builtinRepr():
    print '-- repr(object) --'
    print 'Return a string containing a printable representation of an object.'
    return True


def builtinRever():
    print '-- reversed(seq) --'
    print 'Return a reverse iterator.'
    return True


def builtinRound():
    print '-- round(number[, ndigits]) --'
    print 'Return the floating point value number rounded to ndigits digits',
    print ' after the decimal point. '
    return True


def builtinSet():
    print '-- set([iterable]) --'
    print 'Return a new set object.'
    return True


def builtinSetattr():
    print '-- setattr(object, name, value) --'
    print 'This is the counterpart of getattr().'
    return True


def builtinSlice():
    print '-- class slice(start, stop[, step]) --'
    print 'Return a slice object representing the set of indices',
    print ' specified by range(start, stop, step).'
    return True


def builtinSorted():
    print '-- sorted(iterable[, cmp[, key[, reverse]]]) --'
    print 'Returns a new sorted list from the items in iterable.'
    return True


def builtinStatic():
    print '-- staticmethod(function) --'
    print 'Return a static method for function.'
    return True


def builtinStr():
    print '-- str(object='') --'
    print 'Return a string containing a printable representation of an object.'
    return True


def builtinSum():
    print '-- sum(iterable[, start]) --'
    print 'Sums start and the items of an iterable from left to right and',
    print ' returns the total.'
    return True


def builtinSuper():
    print '-- super(type[, object-or-type]) --'
    print 'Return a proxy object that delegates method calls to a parent',
    print ' or sibling class of type. '
    return True


def builtinTuple():
    print '-- tuple([iterable]) --'
    print 'Return a tuple whose items are the same and in the same order',
    print ' as iterable s items.'
    return True


def builtinType():
    print '-- type(object) --'
    print 'Returns the type of an object.'
    return True


def builtinUnichr():
    print '-- unichr(i) --'
    print 'Return the Unicode string of one character whose Unicode code',
    print ' is the integer i.'
    return True


def builtinUnicode():
    print '-- unicode(object='') --'
    print 'Return the Unicode string version of object.'
    return True


def builtinVars():
    print '-- vars([object]) --'
    print 'Return the __dict__ attribute for a module, class, instance,',
    print ' or any other object with a __dict__ attribute.'
    return True


def builtinXrange():
    print '-- xrange(start, stop[, step]) --'
    print 'This function is very similar to range(), but returns an xrange',
    print ' object instead of a list.'
    return True


def builtinZip():
    print '-- zip([iterable, ...]) --'
    print 'This function returns a list of tuples, where the i-th tuple',
    print ' contains the i-th element from each of the argument sequences',
    print ' or iterables.'
    return True


builtinFunctions = [
    builtinAbs, builtinAll, builtinAny, builtinApply,
    builtinBasestr, builtinBin, builtinBool, builtinBuffer,
    builtinBytes, builtinBytearr, builtinCall, builtinChr,
    builtinClassm, builtinCmp, builtinCoerce, builtinCompile,
    builtinComplex,
    builtinCopyr, builtinCredits, builtinDelattr, builtinDict, builtinDir,
    builtinDivmod, builtinEnum, builtinEval, builtinExecf, builtinExit,
    builtinFile, builtinFilter, builtinFloat, builtinFormat, builtinFroz,
    builtinGetattr, builtinGlobals, builtinHasattr, builtinHash, builtinHelp,
    builtinHex, builtinId, builtinInput, builtinInt, builtinIntern,
    builtinIsinst, builtinIssubc, builtinIter, builtinLen,
    builtinLicense, builtinList, builtinLocals, builtinLong, builtinMap,
    builtinMax, builtinMemview, builtinMin, builtinNext, builtinObject,
    builtinOct, builtinOpen, builtinOrd, builtinPow, builtinPrint,
    builtinProper, builtinQuit, builtinRange, builtinRawin, builtinReduce,
    builtinReload, builtinRepr, builtinRever, builtinRound, builtinSet,
    builtinSetattr, builtinSlice, builtinSorted, builtinStatic,
    builtinStr, builtinSum, builtinSuper, builtinTuple, builtinType,
    builtinUnichr, builtinUnicode, builtinVars, builtinXrange, builtinZip
]


# String methods functions
def strCapitalize():
    print '-- str.capitalize() --'
    print 'First letter of string is changed to capital letter.'
    string = 'sentences start with a capital letter.'
    print '->', string
    print '->', string.capitalize()
    return string.capitalize()[0].isupper()


def strCenter():
    print '-- str.center(arg0) --'
    print 'Centers string using whitespaces, within arg0 size.'
    string = 'Centered text'
    arg0 = 36
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.center(arg0)
    return string.center(arg0)[0] == ' '


def strCount():
    print '-- str.count(arg0) --'
    print 'Counts the occurence of arg0 in string.'
    string = 'Count me in!'
    arg0 = 'n'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.count(arg0)
    return string.count(arg0) == 2


def strEncode():
    print '-- str.encode(arg0) --'
    print 'Encodes string to the desired codec as arg0.'
    string = 'Confidential Information'
    arg0 = 'base64'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.encode(arg0),
    return string == string.encode(arg0).decode(arg0)


def strDecode():
    print '-- str.decode(arg0) --'
    print 'Decodes string using codec as arg0.'
    string = 'Confidential Information'
    arg0 = 'base64'
    string = string.encode(arg0)
    print '-> str =', string,  # EEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRROOOOR \n
    print ', arg0 =', arg0
    print '->', string.decode(arg0)
    return string == string.decode(arg0).encode(arg0)


def strEndswith():
    print '-- str.endswith(arg0) --'
    print 'Determines if string finishes by a given arg0.'
    string = 'The end is where we begin'
    arg0 = 'end'
    arg1 = 'begin'
    arg2 = 'n'
    print '-> str =', string, ', arg0 =', arg0, ', arg0 =', arg1,
    print ', arg0 =', arg2
    print '->', string.endswith(arg0), string.endswith(arg1), string.endswith(
        arg2)
    return string[-1] == arg2


def strExpandtabs():
    print '-- str.expandtabs() --'
    print 'Expands tabs into multiple spaces defined by arg0.'
    string = 'left \t right'
    arg0 = 16
    print '-> str = ', string, ', arg0 =', arg0
    print '->', string.expandtabs(arg0)
    return len(string.expandtabs(arg0)) > len(string)


def strFind():
    print '-- str.find(arg0) --'
    print 'Returns the first index of arg0 in string.'
    string = 'What are you looking for?'
    arg0 = 'a'
    arg1 = 'you'
    print '-> str =', string, ', arg0 =', arg0, ', arg0 =', arg1
    print '->', string.find(arg0), ',', string.find(arg1)
    return string.find(arg0) == 2 and string.find(arg1) == 9


def strIndex():  # DIFFERENCE TO DEFINE FIND/INDEX
    print '-- str.index(arg0) --'
    print 'Returns index of first arg0 in the tested string.'
    string = 'Where is the first i?'
    arg0 = 'i'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.index(arg0)
    return string.index(arg0) == 6


def strFormat():
    print '-- str.format(arg0) --'
    print 'FORMAT***'
    string = 'I have {} points.'
    arg0 = 1000
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.format(arg0)
    return int(string.format(arg0)[7]) == 1


def strIsalnum():
    print '-- str.isalnum() --'
    print 'Returns true if string is only alphanumeric and not empty.'
    string = 'abcdef'
    string1 = '123456'
    string2 = 'one2three'
    print '->', string, string1, string2
    print '->', string.isalnum(), string1.isalnum(), string2.isalnum()
    return string2.isalnum()


def strIsalpha():
    print '-- str.isalpha() --'
    print 'Returns true if string is only alphabetic and not empty.'
    string = 'abcdef'
    string1 = '123456'
    string2 = 'one2three'
    print '->', string, string1, string2
    print '->', string.isalpha(), string1.isalpha(), string2.isalpha()
    return string.isalpha()


def strIsdigit():
    print '-- str.isdigit() --'
    print 'Returns true if string is only numeric and not empty.'
    string = 'abcdef'
    string1 = '123456'
    string2 = 'one2three'
    print '->', string, string1, string2
    print '->', string.isdigit(), string1.isdigit(), string2.isdigit()
    return string1.isdigit()


def strIslower():
    print '-- str.islower() --'
    print 'Returns true if string is only in lowercase and not empty.'
    string = 'small'
    string1 = 'MeDiUm'
    string2 = 'BIG'
    print '->', string, string1, string2
    print '->', string.islower(), string1.islower(), string2.islower()
    return string.islower()


def strIsspace():
    print '-- str.isspace() --'
    print 'Returns true if string is only whitespaces and not empty.'
    string = 'start   stop'
    string1 = '     '
    string2 = 'Go go go!'
    print '->', string, string1, string2
    print '->', string.isspace(), string1.isspace(), string2.isspace()
    return string1.isspace()


def strIstitle():
    print '-- str.istitle() --'
    print 'Returns true if string is in titlecase.'
    string = 'this is not a title'
    string1 = 'This is a sentence.'
    string2 = 'This Is A Title.'
    print '->', string, string1, string2
    print '->', string.istitle(), string1.istitle(), string2.istitle()
    return string2.istitle()


def strIsupper():
    print '-- str.isupper() --'
    print 'Returns true if string is only in uppercase and not empty.'
    string = 'small'
    string1 = 'MeDiUm'
    string2 = 'BIG'
    print '->', string, string1, string2
    print '->', string.isupper(), string1.isupper(), string2.isupper()
    return string2.isupper()


def strJoint():
    print '-- arg0.joint(str) --'
    print 'Concatenates string using defined seperator.'
    string = 'Sky full of stars!'
    arg0 = '*'
    print '-> str =', string, ', arg0 =', arg0
    print '->', arg0.join(string)
    return arg0.join(string)[1] == arg0


def strLjust():
    print '-- str.ljust(arg0, arg1) --'
    print('Fills in string to defined size using defined arg0,'
          ' ajusting original string on the left.')
    string = 'Give me some stars!'
    arg0 = 30
    arg1 = '*'
    print '-> str =', string, ', arg0 =', arg0, ', arg1 =', arg1
    print '->', string.ljust(arg0, arg1)
    return string.ljust(arg0, arg1)[-1] == arg1


def strLower():
    print '-- str.lower() --'
    print 'Concerts string to lowercase.'
    string = 'FiXtHiSStRinG'
    print '->', string
    print '->', string.lower()
    i = random.randint(0, len(string) - 1)
    return string[i].lower().islower()


def strLstrip():
    print '-- str.lstrip(arg0) --'
    print 'Strips leading arg0 from string.'
    string = 'impossible'
    arg0 = 'im'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.lstrip(arg0)
    return string.lstrip(arg0) == 'possible'


'''
def strMaximum():
    print '-- max(str) --'
    print 'Returns maximum alphanumeric character from string.'
    string = '5mqslkdjf132aghn6wbxvp8y4zoi987ucre'
    print '-> str =', string
    print '->', max(string)
    return max(string) == 'z'


def strMinimum():
    print '-- min(str) --'
    print 'Returns minimum alphanumeric character from string.'
    string = '5mqslkdjf132aghn6wbxvp8y4zoi987ucre'
    print '-> str =', string
    print '->', min(string)
    return min(string) == '1'
'''


def strPartition():
    print '-- str.partition(arg0) --'
    print 'Splits string at the first occurence of arg0.'
    string = 'Cut me here please.'
    arg0 = 'here'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.partition(arg0)
    return string.partition(arg0)[1] == arg0


def strReplace():
    print '-- str.replace(arg0, arg1) --'
    print 'Replaces all arg0 in string by arg.'
    string = 'Account balance 1061$'
    arg0 = '1'
    arg1 = '99'
    print '-> str =', string, ', arg0 =', arg0, ', arg1 =', arg1
    print '->', string.replace(arg0, arg1)
    return string.replace(arg0, arg1)[-2] == arg1[-1]


def strRfind():
    print '-- str.rfind(arg0) --'
    print 'Returns the index of arg0 in the tested string starting backwards.'
    string = 'Massachusetts'
    arg0 = 'a'
    arg1 = 's'
    print '-> str =', string, ', arg0 =', arg0, ', arg1 =', arg1
    print '->', string.rfind(arg0), ',', string.rfind(arg1)
    return string.rfind(arg0) == 4 and string.rfind(arg1) == 12


def strRindex():
    print '-- str.rindex(arg0) --'
    print 'Returns the index of arg0 in the tested string starting backwards.'
    string = 'Alibaba'
    arg0 = 'b'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.rindex(arg0)
    return string.rindex(arg0) == 5


def strRjust():
    print '-- str.rjust(arg0, arg1) --'
    print('Fills in string to defined size using defined arg0,'
          ' ajusting original string on the right.')
    string = 'Give me some stars!'
    arg0 = 30
    arg1 = '*'
    print '-> str =', string, ', arg0 =', arg0, ', arg1 =', arg1
    print '->', string.rjust(arg0, arg1)
    return string.rjust(arg0, arg1)[0] == arg1


def strRpartition():
    print '-- str.rpartition(arg0) --'
    print 'Splits string at the first occurence of arg0, starting from ',
    print 'the right.'
    string = 'Cleaner than clean!'
    arg0 = 'ea'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.rpartition(arg0)
    return len(string.rpartition(arg0)[0]) > len(string.rpartition(arg0)[2])


def strRsplit():
    print '-- str.rsplit(arg0) --'
    print 'Returns a list of substring by splitting string according to arg0,',
    print ' starting backwards.'
    string = 'Mississippi'
    arg0 = 'i'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.rsplit(arg0)
    return string.rsplit(arg0)[0] == 'M' and string.rsplit(arg0)[1] == 'ss'


def strRstrip():
    print '-- str.rstrip() --'
    print 'Strips arg0 from the end of string.'
    string = 'golden'
    arg0 = 'en'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.rstrip(arg0)
    return string.rstrip(arg0) == 'gold'


def strSplit():
    print '-- str.split(arg0) --'
    print 'Returns a list of substring by splitting string according to arg0.'
    string = 'Alabama'
    arg0 = 'a'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.split(arg0)
    return string.split(arg0)[0] == 'Al'


def strSplitlines():
    print '-- str.splitlines() --'
    string = 'first line\nsecond line\nthird line'
    print '-> string = first line\\nsecond line\\nthird line'
    print '->', string.splitlines()
    return string.splitlines()[2] == 'third line'


def strStartswith():
    print '-- str.startswith(arg0) --'
    print 'Determines if string starts with arg0 (case sensitive).'
    string = 'Pizzaiolo'
    arg0 = 'Pizza'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.startswith(arg0)
    return string.startswith(arg0)


def strStrip():
    print '-- str.strip(arg0) --'
    print 'Strips arg0 from left and right.'
    string = '***Your Title Here***'
    arg0 = '***'
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.strip(arg0)
    return string.strip(arg0) == 'Your Title Here'


def strSwapcase():
    print '-- str.swapcase() --'
    print 'Swaps the case of every character in string.'
    string = 'swap THIS'
    print '->', string
    print '->', string.swapcase()
    return string.swapcase()[0].isupper() and string.swapcase()[-1].islower()


def strTitle():
    print '-- str.title() --'
    print 'Capitalizes every first letter of any word.'
    string = 'turn this String to title.'
    print '->', string
    print '->', string.title()
    return string.title()[0].isupper() and string.title()[5].isupper()


def strTranslate():
    print '-- str.translate(arg0) --'
    string = 'DEFAULT'
    arg1 = 'OIEAS'
    arg2 = '01345'
    arg0 = maketrans(arg1, arg2)
    print '->', string, ', arg0 = maketrans(arg1, arg2), arg1 =', arg1,
    print ', arg2 =', arg2
    print '->', string.translate(arg0)
    return int(string.translate(arg0)[1]) == 3


def strUpper():
    print '-- str.upper() --'
    print 'Capitalizes every character in string.'
    string = 'make me big'
    print '->', string
    print '->', string.upper()
    return string.upper().isupper()


def strZfill():
    print '-- str.zfill(arg0) --'
    print 'Fills string with arg0 on the left to the width of arg0.'
    string = 'Give me zeros!'
    arg0 = 20
    print '-> str =', string, ', arg0 =', arg0
    print '->', string.zfill(arg0)
    return int(string.zfill(arg0)[0]) == 0 and int(string.zfill(arg0)[1]) == 0


strMethods = [
    strCapitalize, strCenter, strCount, strEncode, strDecode, strEndswith,
    strExpandtabs, strFind, strIndex, strFormat, strIsalnum, strIsalpha,
    strIsdigit, strIslower, strIsspace, strIstitle, strIsupper, strJoint,
    strLjust, strLower, strLstrip, strPartition, strReplace, strRfind,
    strRindex, strRjust, strRpartition, strRsplit, strRstrip, strSplit,
    strSplitlines, strStartswith, strStrip, strSwapcase, strTitle,
    strTranslate, strUpper, strZfill
]


# List methods functions
def listAppend():
    print '-- list.append(arg0) --'
    print 'Adds element arg0 to list.'
    mylist = ['var', 'var']
    arg0 = 'new var'
    print '-> list =', mylist, ', arg0 =', arg0
    mylist.append(arg0)
    print '->', mylist
    return len(mylist) == 3


def listCount():
    print '-- list.count(arg0) --'
    print 'Counts how many arg0 in list.'
    mylist = ['var', 'var', 'new var']
    arg0 = 'var'
    print '-> list =', mylist, ', arg0 =', arg0
    print '->', mylist.count(arg0)
    return mylist.count(arg0) == 2


def listExtend():
    print '-- list.extend(arg0) --'
    print 'Extends list with argument in arg0.'
    mylist = ['var', 'var']
    arg0 = ['new var', 'newer var']
    print '-> list =', mylist, ', arg0 =', arg0
    mylist.extend(arg0)
    print '->', mylist
    return len(mylist) == 4


def listIndex():
    print '-- list.index(arg0) --'
    print 'Returns index or arg0 in list.'
    mylist = ['good', 'to', 'go']
    arg0 = 'go'
    print '-> list =', mylist, ', arg0 =', arg0
    print '->', mylist.index(arg0)
    return mylist.index(arg0) == 2


def listInsert():
    print '-- list.insert(arg0, arg1) --'
    print 'Inserts arg1 in list at index arg0.'
    mylist = ['oh', 'oh', 'oh']
    arg0 = 1
    arg1 = 'yeah'
    print '-> list =', mylist, ', arg0 =', arg0, ', arg1 =', arg1
    mylist.insert(arg0, arg1)
    print '->', mylist
    return mylist[1] == 'yeah'


def listPop():
    print '-- list.pop(arg0) --'
    print 'Deletes and returns element from list at index arg0.'
    mylist = ['qwer', 'ty', 'uiop']
    arg0 = 1
    print '-> list =', mylist, ', arg0 =', arg0
    mylist.pop(arg0)
    print '->', mylist
    mylist = ['qwer', 'ty', 'uiop']
    return mylist.pop(arg0) == 'ty'


def listRemove():
    print '-- list.remove(arg0) --'
    print 'Removes first arg0 from list.'
    mylist = ['obj1', 'obj2', 'obj3']
    arg0 = 'obj1'
    print '-> list =', mylist, ', arg0 =', arg0
    mylist.remove(arg0)
    print '->', mylist
    return len(mylist) == 2


def listReverse():
    print '-- list.reverse() --'
    print 'Reverses objects in list.'
    mylist = [1, 2, 3]
    print '-> list =', mylist
    mylist.reverse()
    print '->', mylist
    return mylist[0] == 3 and mylist[2] == 1


def listSort():
    print '-- list.sort() --'
    print 'Sorts objects in list.'
    mylist = [99, 'x', 'd', 1, 'xyz']
    print '-> list =', mylist
    mylist.sort()
    print '->', mylist
    return mylist[0] == 1 and mylist[-1] == 'xyz'


listMethods = [
    listAppend, listCount, listExtend, listIndex, listInsert, listPop,
    listRemove, listReverse, listSort
]


# Dictionary methods functions
def dictClear():
    print '-- dict.clear() --'
    print 'Deletes all elements from dict.'
    dic0 = {'name': 'python', 'type': 'nonvenomous', 'color': 'brown'}
    print '-> dict =', dic0
    dic0.clear()
    print '->', dic0
    return len(dic0) == 0


def dictCopy():
    print '-- dict.copy() --'
    print 'Returns a copy of dict.'
    dic0 = {'name': 'bryan', 'location': 'kitchen'}
    dic1 = {}
    print '-> dict0 =', dic0, ', dict1 =', dic1
    print '-> dict1 = dic0.copy()'
    dic1 = dic0.copy()
    print '-> dict1 =', dic1
    return len(dic0) == len(dic1)


def dictFromkeys():
    print '-- dict.fromkeys(arg0, arg1) --'
    print 'Returns a dict with keys for every element of arg0 and values ',
    print 'set to arg1'
    dic0 = {}
    arg0 = ['keyOne', 'keyTwo']
    arg1 = 'valueForAll'
    print '-> dict =', dic0, ', arg0 =', arg0, ', arg1 =', arg1
    dic0 = dic0.fromkeys(arg0, arg1)
    print '->', dic0
    return dic0['keyOne'] == 'valueForAll'


def dictGet():
    print '-- dict.get(arg0) --'
    print 'Returns value of key arg0.'
    dic0 = {'name': 'John', 'surname': 'Doe'}
    arg0 = 'name'
    print '-> dict =', dic0, ', arg0 =', arg0
    print '->', dic0.get(arg0)
    return dic0.get(arg0) == 'John'


def dictHaskey():
    print '-- dict.has_key(arg0) --'
    print 'Returns True if dict contains key arg0.'
    print '.has_key() is deprecated, use \'in\' instead.'
    dic0 = {'name': 'Jane', 'surname': 'Doe'}
    arg0 = 'name'
    print '-> dict =', dic0, ', arg0 =', arg0
    print '->', arg0 in dic0
    return arg0 in dic0


def dictItems():
    print '-- dict.items() --'
    print 'Returns a list of elements of dict as tuple pairs.'
    dic0 = {'one': 1, 'two': 2, 'three': 3}
    print '-> dict =', dic0
    print '->', dic0.items()
    return len(dic0.items()) == len(dic0)


"""
print '-- dict.iteritems() --'
print 'Returns items in dict.'
dic0 = {'one':1, 'two':2, 'three':3}
print '-> dict =',dic0
print '->',dic0.iteritems()

print '-- dic0.iterkeys() --'
print 'Returns keys in dict.'
dic0 = {'one':1, 'two':2, 'three':3}
print '-> dict =',dic0
print '->',dic0.iterkeys()

print '-- dic0.itervalues() --'
print 'Returns values in dict.'
dic0 = {'one':1, 'two':2, 'three':3}
print '-> dict =',dic0
print '->',dic0.itervalues()
"""


def dictKeys():
    print '-- dict.keys() --'
    print 'Returns a list of dict\'s keys.'
    dic0 = {'apple': 15, 'kiwi': 10, 'banana': 12}
    print '-> dict =', dic0
    print '->', dic0.keys()
    return len(dic0.keys()) == len(dic0)


def dictPop():
    print '-- dict.pop(arg0) --'
    print 'Deletes arg0 key from dict and returns its value.'
    dic0 = {'france': 'paris', 'spain': 'madrid', 'italy': 'rome'}
    arg0 = 'italy'
    print '-> dict =', dic0, ', arg0 =', arg0
    print '->', dic0.pop(arg0)
    print '-> dict =', dic0
    return len(dic0) == 2


def dictPopitem():
    print '-- dict.popitem() --'
    print 'Deletes last value from dict.'
    dic0 = {'france': 'paris', 'spain': 'madrid', 'italy': 'rome'}
    print "-> dict0 = {'france':'paris', 'spain':'madrid', 'italy':'rome'}"
    print '-> dic0.popitem()'
    dic0.popitem()
    print '-> dict =', dic0
    return len(dic0) == 2


def dictSetdefault():
    print '-- dict.setdefault(arg0) --'
    print 'Returns value of key arg0 (similar to dictget()).'
    dic0 = {'name': 'Ricky', 'surname': 'Bobby'}
    arg0 = 'name'
    print '-> dict =', dic0, ', arg0 =', arg0
    print '->', dic0.setdefault(arg0)
    return dic0.setdefault(arg0) == 'Ricky'


def dictUpdate():
    print '-- dict.update(arg0)'
    print 'Adds arg0\'s keys:values to dict.'
    dic0 = {'fruit': 'lemon', 'color': 'yellow'}
    arg0 = {'fruit': 'tomato', 'color': 'red'}
    print '-> dict =', dic0, ', arg0 =', arg0
    dic0.update(arg0)
    print '->', dic0
    return len(dic0) >= len(arg0)


def dictValues():
    print '-- dict.values()'
    print 'Returns a list of dict values.'
    dic0 = {'Number': 636, 'number': 444, 'numbeR': 100}
    print '-> dict =', dic0
    print '->', dic0.values()
    return len(dic0.values()) == len(dic0)


def dictViewitems():
    print '-- dict.viewitems() --'
    print 'Returns items in dict.'
    dic0 = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3}
    print '-> dict =', dic0
    print '->', dic0.viewitems()
    return len(dic0.viewitems()) == 3


def dictViewkeys():
    print '-- dict.viewkeys() --'
    print 'Returns keys in dict.'
    dic0 = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3}
    print '-> dict =', dic0
    print '->', dic0.viewkeys()
    return len(dic0.viewitems()) == 3


def dictViewvalues():
    print '-- dict.viewvalues() --'
    print 'Returns values in dict.'
    dic0 = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3}
    print '-> dict =', dic0
    print '->', dic0.viewvalues()
    return len(dic0.viewitems()) == 3


dictMethods = [
    dictClear, dictCopy, dictFromkeys, dictGet, dictHaskey, dictItems,
    dictKeys, dictPop, dictPopitem, dictSetdefault, dictUpdate, dictValues,
    dictViewitems, dictViewkeys, dictViewvalues
]

# All methods
allMethods = builtinFunctions + strMethods + listMethods + dictMethods


# Disable print function
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore print function
def enablePrint():
    sys.stdout = sys.__stdout__


# Check for errors, if all functions do not return True, stop script.
print 'Checking for errors...'
error = 0
total = 0
blockPrint()
for meth in range(len(allMethods)):
    if allMethods[meth]() is True:
        total += 1
        enablePrint()
        print allMethods[meth].__name__, '\tOK'
        blockPrint()
    else:
        total += 1
        error += 1
        enablePrint()
        print allMethods[meth].__name__, '\tERROR'
        blockPrint()
enablePrint()
print 'Error checking finished. (', error, ')'
if len(allMethods) != total:
    sys.exit('Checksum error.')
else:
    if error > 0:
        sys.exit('Error(s) detected.')
    else:
        print 'No error.\n\n'

# Menu
ans = True
while ans:
    print '<> Python Built-In Methods Menu <>\n'
    print '1. Built-in Functions\t \t', len(builtinFunctions)
    print '2. Built-in String Methods\t', len(strMethods)
    print '3. Built-in List Methods\t', len(listMethods)
    print '4. Built-in Dictionary Methods\t', len(dictMethods)
    print '5. Display Random Method\t', len(allMethods)
    print '0. Exit\n'
    ans = raw_input("What would you like to do? ")
    if ans == "1":
        print '\n\n***** BUILT-IN FUNCTIONS *****'
        print dir(__builtins__)
        print '\nPress enter to go through functions.'
        raw_input('')
        for i in range(len(builtinFunctions)):
            print builtinFunctions[i]()
            raw_input('')
    elif ans == "2":
        print '\n\n***** STRING METHODS *****'
        print dir(str)
        print '\nPress enter to go through functions.'
        raw_input('')
        for i in range(len(strMethods)):
            print strMethods[i]()
            raw_input('')
    elif ans == "3":
        print '\n\n***** LIST METHODS *****'
        print dir(list)
        print '\nPress enter to go through functions.'
        raw_input('')
        for i in range(len(listMethods)):
            print listMethods[i]()
            raw_input('')
    elif ans == "4":
        print '\n\n***** DICTIONARY METHODS *****'
        print dir(dict)
        print '\nPress enter to go through functions.'
        raw_input('')
        for i in range(len(dictMethods)):
            print dictMethods[i]()
            raw_input('')
    elif ans == "5":
        print '\n\n***** RANDOM *****\n'
        random.choice(allMethods)()
        print '\nPress enter to go back to menu.'
        raw_input('')
        print ' '
    elif ans == "0":
        ans = None
    elif ans != '':
        print('Invalid choice, try again.\n\n')

# END
