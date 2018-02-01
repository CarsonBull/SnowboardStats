from requests import Session
#import requests
import re


username = ""
password = ""



def main():
	# cookie_req = requests.get("https://skihood.com/login")
	# #print(cookie_req.headers)
	# #print(cookie_req.cookies.get("ASP.NET_SessionId"))

	# cookie = cookie_req.cookies.get_dict()['ASP.NET_SessionId']

	# print(cookie)

	# test = "ASP.NET_SessionId=" + cookie + ";"
	s = Session()
	req1 = s.get("https://www.skihood.com/login")

	

	params = {}

	# params["__VIEWSTATE"] = get_view_state(str(req1.text))
	# params["__VIEWSTATEGENERATOR"] = get_view_state_gen(str(req1.text))
	# validator = get_even_validation(str(req1.text))
	# params["__EVENTVALIDATION"] = validator + "&ctl18%24ctl01%24searchValue=&ctl19%24ctl00%24searchValue="
	# params["&body_0%24username"] = username 
	# params["&body_0%24password"] = password 
	# params["&body_0%24loginButton"] = "Sign+in"
	# print(params)

	params["__EVENTTARGET"] = ""
	params["__EVENTARGUMENT"] = ""
	params["__VIEWSTATE"] = get_view_state(str(req1.text))
	params["__VIEWSTATEGENERATOR"] = get_view_state_gen(str(req1.text))
	params["__EVENTVALIDATION"] = get_even_validation(str(req1.text))
	params["ctl18$ctl01$searchValue"] = ""
	params["ctl19$ctl00$searchValue"] = ""
	params["body_0$username"] = username
	params["body_0$password"] = password
	params["body_0$loginButton"] = "Sign in"

	#print(params)

	req = s.get("https://www.skihood.com/login" , params = params)


	# print(s.headers)
	# print(s.cookies)
	# #sprint(s.history)
	# print('----------------')
	# print(req.headers)
	# print(req.cookies)
	print(req.history)
	print("----------------------")
	print(req.url)
	print("----------------------")

	# print(login_req.history)
	# cookie2 = login_req.cookies.get('ASP.NET_SessionId')
	# print(login_req)
	# print(login_req.headers)
	# print(login_req.cookies)
	# temp = "ASP.NET_SessionId=" + cookie2 + ";"
	# print(temp)

	req4 = s.get("https://www.skihood.com/resort-services/passholder-benefits-and-services/track-your-turns" )
	print(req4)
	print(req4.headers)
	print(s)
	print(s.headers)

	print()
	print("2018" in req4.text )


def get_even_validation(text):
	''' This function takes the login page and returns the tag tokent hat is needed to build a login url'''
	match = re.search(r'.*id="__EVENTVALIDATION" value="(.*)".*' , text)
	if match:
		return match.group(1)
	else:
		return None

def get_view_state_gen(text):
	match = re.search(r'id="__VIEWSTATEGENERATOR".*value="(.*)"' , text)
	if match:
		return match.group(1)
	else:
		return None

def get_view_state(text):
	match = re.search(r'.*id="__VIEWSTATE" value="(.*)".*' , text)
	if match:
		return match.group(1)
	else:
		return None


def get_user():
	'''This fucntion get the username and password from a file that is stored in the directory
	This is not the best way to handle this. Encryption and decryption should be used or have
	the user enter their username and password'''
	with open('usernames.txt' , 'r') as f:
		for line in f:
			match = re.match(r'^username: (.*)$' , line , re.M)
			if match:
				temp_username = match.group(1)
				#print(username)
				break

		if temp_username == "":
			print("------------------------------------------------------------\nAdd a username or the usernames.txt file to continue.\n Format: \"username: [username]\"\n------------------------------------------------------------")
			return None

		for line in f:
			match = re.match(r'^password: (.*)$' , line , re.M)
			if match:
				temp_password = match.group(1)
				#print(password)
				break
				
		if temp_password == "":
			print("Add a password\n Format: \"password: [password]\"")
			return None

	return temp_username , temp_password







if __name__ == "__main__":
	temp = get_user()
	if temp != None:
		username = temp[0]
		password = temp[1]
	else:
		exit()
	main()