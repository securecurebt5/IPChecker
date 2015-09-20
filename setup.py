from distutils.core import setup
setup(
	name="IPChecker",
	version="1.0",
	author = "Boumediene Kaddour",
	author_email="snboumediene@gmail.com",
	packages=["IPChecker"],
	scripts=[],
	url='http://pypi.python.org/pypi/IPchecker',
	license="LICENSE.txt",
	description="Check if IP is Private, Public or Invalid"
	long_description=open('README.rst').read(),
	install_requires=[],)
