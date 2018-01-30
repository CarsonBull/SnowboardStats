import requests
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

	login_req = requests.get('https://www.skihood.com/login')

	# print(login_req.history)
	# cookie2 = login_req.cookies.get('ASP.NET_SessionId')
	print(login_req)
	print(login_req.headers)
	print(login_req.cookies)
	# temp = "ASP.NET_SessionId=" + cookie2 + ";"
	# print(temp)

	# req4 = requests.get("https://www.skihood.com/resort-services/passholder-benefits-and-services/track-your-turns" , headers={"Cookie": temp})


	print()
	# print("2018" in req4.text )


def get_user():

	with open('usernames.txt' , 'r') as f:
		for line in f:
			match = re.match(r'^username: (.*)$' , line , re.M)
			if match:
				username = match.group(1)
				#print(username)
				break

		if username == "":
			print("Add a username or the usernames.txt file to continue.\n Format: \"username: [username]\"")

		for line in f:
			match = re.match(r'^password: (.*)$' , line , re.M)
			if match:
				password = match.group(1)
				#print(password)
				break
				
		if password == "":
			print("Add a password\n Format: \"password: [password]\"")







if __name__ == "__main__":
	get_user()
	main()