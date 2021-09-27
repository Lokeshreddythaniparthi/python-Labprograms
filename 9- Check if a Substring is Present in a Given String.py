import re
MyString1 =str(input("enter the string:"))
MyString2 =str(input("enter the search string:"))
if re.search( MyString2, MyString1 ):
    print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1))
else:
    print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) )