from flask import Flask, render_template
from flask import request, jsonify
from plotgraph import disease_pie, disease_death, disease_values
from plotgraph import medicine_pie, medicine_values
from flask import send_from_directory
from flask import flash, redirect, session, abort, url_for
import os
import random
import facts
from bcg import predict_polio, predict_pbm, predict_prox, predict_bcg_statewise, predict_measles_statewise, predict_dtp
from imgpil import create_imgs
import san_extract

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.errorhandler(400)
def badreq(e):
	return render_template('error_400.html')

@app.route('/')
def home():
	print(predict_polio(560950))
	# predict_polio(560950)
	return render_template('index.html')

@app.route('/analysis', methods = ['GET', 'POST'])
def analysis():
	global disease
	global state
	global year
	year = request.form['year']
	state = request.form['state']
	disease = request.form['disease']
	year = int(year)
	disease_death()
	medicine_pie(year)
	disease_pie(year) #just example variables. the function can also be modified.
	return render_template('analysis.html', year=year, state=state, disease=disease)

@app.route('/immune', methods = ['GET', 'POST'])
def immune():
	return render_template('immune.html')

@app.route('/immune-result', methods = ['GET', 'POST'])
def immune2():
	global input_1
	global input_2
	global vaccine
	vaccine = request.form['vaccine']
	input_2 = float(request.form['input-2'])
	input_1 = float(request.form['input-1'])
	polio = predict_polio(input_1)
	pbm = predict_pbm([input_1, input_2])
	prox = predict_prox([input_1, input_2])
	bcg_state = predict_bcg_statewise([input_1, input_2])
	measels_state = predict_measles_statewise([input_1, input_2])
	dtp = predict_dtp([input_1, input_2]) 
	return render_template('immune-result.html',polio=polio, dtp = dtp, pbm = pbm, prox = prox, bcg_state = bcg_state, measels_state = measels_state,vaccine = vaccine) 

@app.route('/prescribe', methods = ['GET', 'POST'])
def prescribe():
	foo = ['malaria', 'aids', 'arthritis', 'influenza']
	disease = random.choice(foo)
	img_list=create_imgs(disease)
	print len(img_list)
	return render_template('image.html',images=img_list)


@app.route('/plots')
def plots():
	return render_template('plots.html')

@app.route('/blood')
def blood():
	return render_template('blood.html')

@app.route('/ranking')
def ranking():
	states = ['Sikkim', 'Jammu & Kashmir' 'Tripura', 'Meghalaya' ,'Nagaland', 'West Bengal',

'Orissa', 'Uttar Pradesh' ,'Rajasthan', 'Himachal Pradesh', 'Andhra Pradesh',

'Telangana' ,'Kerala' ,'Madhya Pradesh', 'Haryana', 'Jharkhand', 'Assam',

'Tamil Nadu', 'Punjab', 'Chhattisgarh', 'Gujarat', 'Bihar', 'Mizoram',

'Arunachal Pradesh', 'Goa', 'Karnataka', 'Maharashtra', 'Manipur',

'Uttarakhand']

	return render_template('ranking.html', states = states)

@app.route('/fact', methods = ['GET','POST'])
def fact():
	img_url = facts.get_image(disease)
	# print card_text
	# text = sat_extract.fact_extract(user_input)
	text = facts.factract(disease).decode('utf-8')
	if text=='':
		return "Working"
	text = text.split('\n')
	return render_template('facts.html', text = text, img_url = img_url, disease = disease)

if __name__ == "__main__":
	# app.debug = True
	app.run(debug=True)