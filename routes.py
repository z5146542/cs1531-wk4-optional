from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
'''
 write(name, zID, desc)
 Writes on a given csv file on append mode
 @param name : name of the user input provided from form
 @param zID : zID of the user input provided from form
 @param desc : description of the user input provided from form
 @return void
'''
def write(name, zID, desc):
	with open('example.csv','a') as csv_out:
		writer = csv.writer(csv_out)
		writer.writerow([name,zID,desc])
'''
 read()
 Reads a given csv file
 @return readFile 2-dimensional list that contains user information of format n*3
'''
def read():
	readFile = []
	with open('example.csv','r') as csv_in:
		reader = csv.reader(csv_in)
		for row in reader:
			readFile.append(row)
	return readFile
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		name = request.form["name"]
		zID = int(request.form["zID"])
		description = request.form["desc"]
		#user_input.append([name, zID, description])
		write(name, zID, description)
		return redirect(url_for("hello"))
	return render_template("index.html")
@app.route("/Hello")
def hello():
	return render_template("hello.html", all_users=read())
'''
	<name>,<zID>,<description> are variables given from clicking on the hyperlink in hello.html
	aname, azID, adescription are variables to be used in user.html
		you can see in user.html that it uses the variables aname, azid, adescription
'''
@app.route("/Hello/<name>/<zID>/<description>")
def user(name, zID, description):
	return render_template("user.html", aname=name, azID=zID, adescription=description)