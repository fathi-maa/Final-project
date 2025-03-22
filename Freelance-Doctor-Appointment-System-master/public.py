from flask import *
from database import *
import uuid
import os
from flask import Flask, request, render_template, redirect, url_for, flash
from database import insert
public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if "submit" in request.form:
		u=request.form['uname']
		p=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(u,p)
		print(q)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				flash("Logging in")			
				return redirect(url_for("admin.admin_home"))

			elif res[0]['usertype']=="doctor":
				q="select * from doctor where login_id='%s'"%(session['lid'])
				res1=select(q)
				if res1:
					session['did']=res1[0]['doctor_id']
					print(session['did'])
					flash("Logging in")
					return redirect(url_for("doctor.doctor_home"))

			elif res[0]['usertype']=="user":
				q="select * from user where login_id='%s'"%(session['lid'])
				res1=select(q)
				if res1:
					session['uid']=res1[0]['user_id']
					print(session['uid'])
					flash("Logging in")
					return redirect(url_for("user.user_home"))

			# elif res[0]['usertype']=="seller":
			# 	q="select * from seller where login_id='%s'"%(res[0]['login_id'])
			# 	res1=select(q)
			# 	if res1:
			# 		session['sid']=res1[0]['seller_id']
			# 		print(session['sid'])
			# 		flash("Logging in")
			# 		return redirect(url_for("rescue.rescue_home"))

			



			# elif res[0]['type']=="customer":
			# 	q="select * from customer inner join login using (username) where username='%s' and status='0'"%(u)
			# 	res=select(q)
			# 	if res:
			# 		flash('inactive')
			# 	else:


			# 		q="select * from customer where username='%s'"%(lid)
			# 		res=select(q)
			# 		if res:
			# 			session['customer_id']=res[0]['customer_id']
			# 			cid=session['customer_id']
			# 		return redirect(url_for('customer.customer_home'))

			else:
				flash("Registration Under Process")
		flash("You are Not Registered")

	return render_template('login.html')



# import os
# import uuid
# from flask import Flask, request, render_template, redirect, url_for, flash

# # Initialize Flask App
# app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Required for flash messages

# # Ensure 'static' directory exists
# if not os.path.exists('static'):
#     os.makedirs('static')

# @app.route('/reg', methods=['GET', 'POST'])
# def reg():
#     data = {}

#     if 'submit' in request.form:
#         fname = request.form['fname']
#         lname = request.form['lname']

#         # Handle Image Upload
#         if 'image' in request.files and request.files['image'].filename:
#             img = request.files['image']
#             img_path = os.path.join('static', str(uuid.uuid4()) + "_" + img.filename)
#             img.save(img_path)
#         else:
#             img_path = None

#         # Handle Certificate Upload
#         if 'img' in request.files and request.files['img'].filename:
#             cert = request.files['img']
#             cert_path = os.path.join('static', str(uuid.uuid4()) + "_" + cert.filename)
#             cert.save(cert_path)
#         else:
#             cert_path = None

#         place = request.form['place']
#         phone = request.form['phone']
#         email = request.form['email']
#         gender = request.form['gender']
#         consulting_place = request.form['pl']
#         username = request.form['username']
#         password = request.form['password']

#         # Dummy database insert (Replace with actual DB insertion)
#         flash("Registered successfully!")
#         return redirect(url_for('reg'))

#     return render_template("reg.html", data=data)

# # Run Flask App
# if __name__ == "__main__":
#     app.run(debug=True)

import os
import uuid

@public.route('/reg', methods=['GET', 'POST'])
def reg():
    data = {}
    dept = request.args.get('dept', '')

    if 'submit' in request.form:
        print(request.files)
        fname = request.form['fname']
        lname = request.form['lname']

        # Get the absolute path to the "static" folder inside your project
        static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)  # Ensure the folder exists

        # Save the profile image
        profile_image = request.files['image']
        profile_filename = str(uuid.uuid4()) + "_" + profile_image.filename
        profile_path = os.path.join(static_folder, profile_filename)
        profile_image.save(profile_path)

        # Save the certificate image
        certificate = request.files['img']
        cert_filename = str(uuid.uuid4()) + "_" + certificate.filename
        cert_path = os.path.join(static_folder, cert_filename)
        certificate.save(cert_path)

        place = request.form['place']
        phone = request.form['phone']
        email = request.form['email']
        gen = request.form['gender']
        pl = request.form['pl']
        uname = request.form['username']
        pas = request.form['password']

        # Insert into login table
        q = "INSERT INTO login VALUES (NULL, '%s', '%s', 'pending')" % (uname, pas)
        id = insert(q)
		

        # Insert into doctor table (store only filenames, not full paths)
        q = "INSERT INTO doctor VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 'active', CURDATE(), '%s')" % (
            id, dept, fname, lname, place, phone, email, gen, pl, cert_filename, profile_filename
        )
        insert(q)
        flash("Registered successfully..!")

        return redirect(url_for('public.login'))

    return render_template("reg.html", data=data)


# import os

# @public.route('/reg', methods=['GET', 'POST'])
# def reg():
#     data = {}
#     dept = request.args['dept']

#     if 'submit' in request.form:
#         print(request.files)
#         fname = request.form['fname']
#         lname = request.form['lname']
#         i = request.files['image']

#         # Define the correct path inside the project folder
#         static_folder = os.path.join(os.getcwd(), 'static')
#         if not os.path.exists(static_folder):
#             os.makedirs(static_folder)  # Create the folder if it doesn't exist
        
#         img_filename = str(uuid.uuid4()) + "_" + i.filename
#         img_path = os.path.join(static_folder, img_filename)
#         i.save(img_path)  # Save inside the correct static folder

#         place = request.form['place']
#         phone = request.form['phone']
#         email = request.form['email']
#         gen = request.form['gender']
#         pl = request.form['pl']
        
#         img = request.files['img']
#         cert_filename = str(uuid.uuid4()) + "_" + img.filename
#         cert_path = os.path.join(static_folder, cert_filename)
#         img.save(cert_path)

#         uname = request.form['username']
#         pas = request.form['password']

#         q = "INSERT INTO login VALUES (NULL, '%s', '%s', 'pending')" % (uname, pas)
#         id = insert(q)

#         q = "INSERT INTO doctor VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 'active', CURDATE(), '%s')" % (
#             id, dept, fname, lname, place, phone, email, gen, pl, cert_filename, img_filename
#         )
#         insert(q)
#         flash("Registered successfully..!")

#         return redirect(url_for('public.login'))

#     return render_template("reg.html", data=data)



@public.route('/userreg',methods=['get','post'])
def userreg():
	

	if 'submit' in request.form:
		
		fname=request.form['fname']
		lname=request.form['lname']
		
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','user')"%(uname,pas)
		id=insert(q)
		print(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
		insert(q)
		flash("Registered successfully..!")
	
		return redirect(url_for('public.login'))

	return render_template("userreg.html")



@public.route('/View_depts')
def View_depts():
	data={}
	q="SELECT * FROM department "
	res=select(q)
	data['dept']=res
	return render_template('View_depts.html',data=data)