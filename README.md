![logo](https://user-images.githubusercontent.com/31503773/54771702-15287b00-4c06-11e9-966b-cf4073f3c27b.png)
# PWB for python 3.7
With this script you can brute-force website logins via a pass-/userlist. Please don't use this for illegal purpose, I'm NOT responsible for any use of this project. Only use this script on your OWN sites.

# How does it work?
This script can interact with webpages over the machanize python module, tries all the combination given in the user- and passlist. It will continue to check passwords, until it's redirected to a specific site.

# How to use this script?
First install the mechanize module for this script
```
pip install mechanize
```
or
```
easy_install mechanize
```
# Step 1: Specify the path to your passlist:
```
# Please set the path to your passlist
pass_filepath = "passwords.txt"
```
# Step 2: Specify the path to your userlist:
```
# Please set the path to your userlist
user_filepath = "users.txt"
```
# Step 3: Specify the site, you want to brute-force:
```
# Please enter the login you want to brute force
login_page = "http://testing-ground.scraping.pro/login"
```
# Step 4: Specify the site you will be redirected after login:
```
#Please set the page you will be redirected at a successful login
redirected_page = "http://testing-ground.scraping.pro/login?mode=welcome"
```
# Step 5: Last, but not least, specify your form:
```
#Enter the html code of the form you want to brute force
login_form = '''
			<form action="login?mode=login" name="from1" method="POST">
        	<label for="usr">User name:</label>
           .
           .
        	<input type="submit" value="Login" kl_vkbd_parsed="true">
    		</form>
			'''
```
# Launch the script via the command line
```
python PWB.py
```
