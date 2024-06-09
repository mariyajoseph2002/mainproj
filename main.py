from flask import Flask
from public import public
from admin import admin
from customer import customer
from staff import staff


app=Flask(__name__)
app.secret_key="heai"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(customer)
app.register_blueprint(staff)


app.run(debug=True,port=5062)