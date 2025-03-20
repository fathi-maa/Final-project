from flask import *
from database import *
import uuid
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




@public.route('/reg',methods=['get','post'])
def reg():
	data={}
	dept=request.args['dept']

	if 'submit' in request.form:
		
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		gen=request.form['gender']
		pl=request.form['pl']
		# time=request.form['time']
		i=request.files['img']
		path='static/'+str(uuid.uuid4())+i.filename
		i.save(path)
		img=request.files['image']
		src='static/'+str(uuid.uuid4())+i.filename
		img.save(src)


		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','pending')"%(uname,pas)
		id=insert(q)
		print(q)
		q="insert into doctor values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active',curdate(),'%s')"%(id,dept,fname,lname,place,phone,email,gen,pl,path,src)
		insert(q)
		flash("Registered successfully..!")
		
		return redirect(url_for('public.login'))

	return render_template("reg.html",data=data)



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