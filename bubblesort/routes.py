from flask import Flask, redirect, render_template, request, url_for
from server import app
user_input = []
sorted_seq = []

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		numbers = request.form["numbers"]
		numbers.split(",")
		user_input = [int(i) for i in numbers.split(',')]
		print(user_input)
		global sorted_seq
		sorted_seq = bubblesort(user_input)
		print(sorted_seq)
		return redirect(url_for("sort"))
	return render_template("index.html")
def bubblesort(seq):
	sequence = []
	sequence.append([int(j) for j in seq])
	while True:
		isSorted = True
		for i in range(len(seq)-1):
			if seq[i] > seq[i+1]:
				temp = seq[i]
				seq[i] = seq[i+1]
				seq[i+1] = temp
				isSorted = False
				tempList = [int(j) for j in seq]
				sequence.append(tempList)
			i = i + 1
		if isSorted:
			break
	return sequence
@app.route("/sorted")
def sort():
	return render_template("sort.html", sorted_seq=sorted_seq)