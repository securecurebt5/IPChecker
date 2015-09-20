##################################      IPChecker      ##################################

IPChecker is a tiny Python library that is used to check if an IP version address is Private, Public or Invalid,
The library returns Booleans and contains a couple of methods summurized as follows:

  isValid(): This method return True, if a valid IPv4's given, otherwise, it returns False.
  isPrivate(): This little method returns True if the given IP is private, otherwise, False is returned.
  isPublic(): This little method returns True if the given IP is Public, otherwise, False is returned.

Usage:
 >>> from IPChecker import IPChecker
 >>> obj = IPChecker("172.16.122.254")
 >>> obj.isValide()
 >>> True
 >>> obj.isPrivate()
 >>> True
 >>> obj.isPublic()
 >>> False
 
 Here is an example of how you can checkout for a valid IPv4 address using regular expressions
 in this example, i'm going to be using the built-in re module in python
 
 def isValid(ip):
      if findall( "(?i)^(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$" ,ip):
		        return True
	    else:
		        return False
 

 
 
 
 
 
