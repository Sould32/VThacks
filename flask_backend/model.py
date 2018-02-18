from sqlalchemy import Column, Integer, String, Float, BOOLEAN
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=False)
    email = Column(String(120), unique=False)
    password = Column(String(50), unique=False)
    street =  Column(String(120), unique=False)
    zip_code =  Column(Integer, unique=False)
    state = Column(String(70), unique=False)
    marital_status = Column(String(20), unique=False)
    number_of_dep = Column(Integer, unique=False)
    yearly_income = Column(Float, unique=False)

    #spending
    grocery = Column(Float, unique=False)
    monthly_suscription = Column(Float, unique=False)
    restaurant =  Column(Float, unique=False)
    other_spending = Column(Float, unique=False)

    #vehicule
    has_vehicule =  Column(BOOLEAN, unique=False)
    car_make = Column(String(120), unique=False)
    car_model = Column(String(120), unique=False)
    car_year = Column(Integer, unique=False)
    car_payment = Column(Float, unique=False)
    other_car_cost = Column(Float, unique=False)
    fuel = Column(Float, unique=False)
    public_transport = Column(BOOLEAN, unique=False)
    public_cost = Column(Float, unique=False)

    #house
    own_house = Column(BOOLEAN, unique=False)
    morgage = Column(Float, unique=False)
    rent = Column(Float, unique=False)
    utulity = Column(Float, unique=False)
    house_maintenance = Column(Float, unique=False)

    #saving
    investment  = Column(Float, unique=False)
    saving_account = Column(Float, unique=False)
    emrgency_saving = Column(Float, unique=False)


    def __init__(self, username=None, email=None, password =None, street = None, zip_code = None, 
    	state = None, marital_status=None, number_of_dep=None, grocery = None, 
    	monthly_suscription = None, restaurant = None, other_spending = None, has_vehicule=None,
    	car_make=None, car_model=None, car_year=None, car_payment=None, other_car_cost=None, fuel=None,
    	public_transport=None, public_cost=None, morgage=None, rent=None, utulity=None, yearly_income = None,
    	house_maintenance=None, investment=None, saving_account =None, emrgency_saving = None, own_house=None):

        self.username = username
        self.email = email
        self.password = password
        self.street = street
        self.zip_code = zip_code
        self.state = state
        self.marital_status = marital_status
        self.number_of_dep = number_of_dep
        self.yearly_income = yearly_income

        self.grocery = grocery
        self.monthly_suscription = monthly_suscription
        self.restaurant = restaurant
        self.other_spending = other_spending
        self.has_vehicule = has_vehicule
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.car_payment = car_payment
        self.other_car_cost = other_car_cost
        self.fuel = fuel
        self.public_transport = public_transport
        self.public_cost = public_cost
        self.morgage = morgage
        self.rent = rent
        self.utulity = utulity
        self.house_maintenance = house_maintenance
        self.investment = investment
        self.saving_account = saving_account
        self.emrgency_saving = emrgency_saving
        self.own_house = own_house

    def __repr__(self):
        return '<User %r>' % (self.username)

    def get_state(self):
    	return self.state

    def get_income(self):
    	return self.yearly_income

    def get_marital_status(self):
    	return self.marital_status

    def get_number_of_dep(self):
    	return self.number_of_dep
    	
    def serialize(self):
    	return {
	    	'user': {
	    		'username': self.username,
		    	'email': self.email,
		    	'street': self.street,
		    	'zip_code': self.zip_code,
		    	'state': self.state,
		    	'marital_status': self.marital_status,
		    	'number_of_dep': self.number_of_dep,
		    	'yearly_income': self.yearly_income,
		    	'house': {
		    		'own_house': self.own_house,
				    'morgage':self.morgage,
				    'rent' :self.rent,
				    'utulity': self.utulity,
				    'house_maintenance': self.house_maintenance
		    	},
		    	'vehicule': {
		    		'has_vehicule': self.has_vehicule,
		    		'car_make': self.car_make,
		    		'car_model': self.car_model,
		    		'car_year': self.car_year,
		    		'car_payment': self.car_payment,
		    		'other_car_cost': self.other_car_cost,
		    		'fuel':self.fuel,
				    'public_transport' :self.public_transport,
				    'public_cost' : self.public_cost
		    	},
		    	'spending': {
		    		'grocery': self.grocery,
				    'monthly_suscription': self.monthly_suscription,
				    'restaurant': self.restaurant,
				    'other_spending': self.other_spending
		    	},
		    	'saving': {
		    		'investment': self.investment,
				    'saving_account':self.saving_account,
				    'emrgency_saving': self.emrgency_saving
		    	}
	    	}
    	}

