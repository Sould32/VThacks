from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import login_required
from database import init_db
from model import User
from flask import jsonify
from database import db_session
import pdb
import tax

app = Flask(__name__)
CORS(app)

init_db()


@app.route('/api', methods=['GET', 'POST'])
def index():
	return "hello world"


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

@app.route('/api/get_saving_data', methods=['GET'])
def get_saving_data():
	print('saving data')
	username = request.args.get('username')
	#print(username)
	#print(User.query.all())
	u = User.query.filter(User.username == username).first()
	#print (u)
	if not u:
		abort(400)
	#ret = jsonify(u.serialize())

	#calc_tax_info(us_state, income, marital_status='single', dependents=0)
	tax_data = tax.calc_tax_info(u.get_state(), u.get_income(), u.get_marital_status(), u.get_number_of_dep())
	#print (tax_data)
	start1 = (0, 0)
	end1 = [5, 85000];
	start2 = [0, 1000]
	end2 = [5, 32000]
	recomandation = {
		'house': {
			'start': start1,
			'end': end1
		},
		'car': {
			'start': start2,
			'end': end2
		}
	}
	data = {'ret': u.serialize(), 'tax': tax_data, 'recomandation':recomandation}
	print(data)
	return jsonify(data)

@app.route('/api/create_user', methods = ['POST'])
def create_user():
	print ('create_user')
	print (request.json)
	#pdb.set_trace()
	if (not request.json or 'username' not in request.json):
		print('json or username')
		abort(400)
	if ('state' not in request.json or 'street' not in request.json):
		print('state error, street error')
		abort(400)
	if ('zip_code' not in request.json or 'marital_status' not in request.json):
		print('zip_code error or martial status')
		abort(400)
	if ('email' not in request.json or 'password' not in request.json):
		print('email error or password')
		abort(400)
	if ('number_of_dep' not in request.json):
		print('number_of_dep error')
		abort(400)
	
# grocery = None, 
#   	monthly_suscription = None, restaurant = None, other_spending = None, has_vehicule=None,
#   	make=None, model=None, year=None, car_payment=None, other_car_cost=None, fuel=None,
#   	public_transport=None, public_cost=None, morgage=None, rent=None, utulity=None, 
#   	maintenance=None, investment=None, saving_account =None, emrgency_saving = None)

	print('before saving')
	username = request.json['username']
	password = request.json['password']
	email = request.json['email']
	zip_code = request.json['zip_code']
	street = request.json['street']
	state = request.json['state']
	marital_status = request.json['marital_status']
	num_of_dep = request.json['number_of_dep']
	grocery =  request.json['grocery']
	monthly_suscription = request.json['monthly_suscription']
	restaurant = request.json['restaurant']
	other_spending = request.json['other_spending']
	has_vehicule = str2bool(request.json['has_vehicule'])
	car_make = request.json['car_make']
	car_model = request.json['car_model']
	car_year = request.json['car_year']
	car_payment = request.json['car_payment']
	other_car_cost = request.json['other_car_cost']
	fuel = request.json['fuel']
	public_transport = str2bool(request.json['public_transport'])
	public_cost = request.json['public_cost']
	morgage = request.json['morgage']
	rent = request.json['rent']
	utulity = request.json['utulity']
	house_maintenance = request.json['house_maintenance']
	investment = request.json['investment']
	saving_account = request.json['saving_account']
	emrgency_saving = request.json['emrgency_saving']
	own_house = str2bool(request.json['own_house'])
	yearly_income = request.json['yearly_income']

	u = User(username, email, password, street, zip_code, state, marital_status, num_of_dep, 
		grocery, monthly_suscription, restaurant, other_spending, has_vehicule, car_make, car_model, 
		car_year, car_payment, other_car_cost, fuel, public_transport, public_cost, morgage, 
		rent, utulity, yearly_income, house_maintenance, investment, saving_account, emrgency_saving,
		 own_house)

	db_session.add(u)
	db_session.commit()
	ret = jsonify(u.serialize())
	print (ret)
	return ret


if __name__ == '__main__':
	app.run()
