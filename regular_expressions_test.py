import re

l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""
m = re.findall("^If", zen, re.MULTILINE)

print(m)


string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t, re.IGNORECASE)
print(found)


line = "I love $"
m = re.findall("\$", line)
print(m)

line = "The ghost that says boo haunts the loo"
m = re.findall(".oo", line)
print(m)


#text = """Giraffes have aroused
# the curiosity of __PLURAL_NOUN__
# since earliest times. The
# giraffe is the tallest of all
# living __PLURAL_NOUN__, but
# scientists are unable to
# explain how it got its long
# __PART_OF_THE_BODY__. The
# giraffe's tremendous height,
# which might reach __NUMBER__
# __PLURAL_NOUN__, comes from
# it legs and __BODYPART__.
#"""
#
#
#def mad_libs(mls):
#    """
#    :param mls: String
#    with parts the user
#    should fill out surrounded
#    by double underscores.
#    Underscores cannot
#    be inside hint e.g., no
#    __hint_hint__ only
#    __hint__.
#    """
#    hints = re.findall("__.*?__", mls)
#    if hints is not None:
#        for word in hints:
#            q = "Enter a {}"\
#                   .format(word)
#            new = input(q)
#            mls = mls.replace(word,
#                              new,
#                              1)
#        print('\n')
#        mls = mls.replace("\n", "")
#        print(mls)
#    else:
#        print("invalid mls")
#
#mad_libs(text)