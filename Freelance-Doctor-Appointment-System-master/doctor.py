from flask import *
from database import *
doctor=Blueprint('doctor',__name__)

@doctor.route('/doctor_home')
def doctor_home():
	return render_template('doctor_home.html')


@doctor.route('/doctor_view_booking',methods=['get','post'])
def doctor_view_booking():
	data={}
	q="select *,booking.status as st from booking inner join schedule using (schedule_id) inner join user using (user_id)  where doctor_id='%s' "%(session['did'])
	res=select(q)
	data['tr']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="accept":
		q="update booking set status='accept' where booking_id='%s'"%(id)
		update(q)
		flash('Appointment confirmed....!!')
		return redirect(url_for('doctor.doctor_view_booking'))

	if action=="reject":
		q="update booking set status='reject'   where booking_id='%s'"%(id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('doctor.doctor_view_booking'))

	return render_template('doctor_view_booking.html',data=data)

@doctor.route('/doctor_add_treatment',methods=['get','post'])
def doctor_add_treatment():
	data={}
	id=request.args['id']
	q="select * from treatment"
	data['tr']=select(q)
	if 'submit' in request.form:
		fname=request.form['fname']
		
		
		q="insert into treatment values(null,'%s','%s',curdate())"%(fname,id)
		insert(q)
		print(q)
		return redirect(url_for('doctor.doctor_add_treatment',id=id))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="delete":
		q="delete from department where department_id='%s'"%(id)
		delete(q)
		return redirect(url_for('doctor.doctor_add_treatment'))


	return render_template("doctor_add_treatment.html",data=data)


@doctor.route('/doctor_view_salary',methods=['get','post'])
def doctor_view_salary():
	data={}
	did=session['did']

	q="select * from salary where doctor_id='%s'"%(did)
	data['tr']=select(q)
	return render_template("doctor_view_salary.html",data=data)

@doctor.route('/doctor_send_application',methods=['get','post'])
def doctor_send_application():
	data={}
	q="select * from application"
	data['tr']=select(q)
	if 'submit' in request.form:
		date=request.form['date']
		place=request.args['palce']
		pl=request.form['pl']
		certi=request.form['img']
		
		q="insert into treatment values(null,'%s','%s','%s','%s','%s',curdate())"%(session['did'],date,place,pl,certi)
		insert(q)
		print(q)
		return redirect(url_for('doctor.doctor_send_application'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="delete":
		q="delete from department where department_id='%s'"%(id)
		delete(q)
		return redirect(url_for('doctor.doctor_send_application'))


	return render_template("doctor_send_application.html",data=data)


@doctor.route('/doctor_view_profile',methods=['get','post'])
def doctor_view_profile():
	data={}
	did=session['did']
	q="SELECT * FROM doctor inner join login using(login_id) where doctor_id='%s'"%(did)
	res=select(q)
	data['tr']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="update":
		q="select * from doctor  where doctor_id='%s'"%(id)
		res=select(q)
		data['updated']=res


	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		# gender=request.form['gender']
		q="update doctor set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where doctor_id='%s'"%(fname,lname,place,phone,email,id)
		update(q)
		flash("updated successfully")
		
		return redirect(url_for('doctor.doctor_view_profile'))

	return render_template("doctor_view_profile.html",data=data)


@doctor.route('/doctor_chat')
def psycho_chat():
	data={}
	q="select * from user "
	res=select(q)
	data['tr']=res

	return render_template("doctor_chat.html",data=data)


@doctor.route('/doctor_message',methods=['get','post'])
def doctor_message():
	data={}
	receiver_id=request.args['receiver_id']
	sender_id=session['lid']
	data['psycho']=sender_id

	q="select * from chat where (sender_id='%s' and receiver_id='%s') or (receiver_id='%s' and sender_id='%s')"%(sender_id,receiver_id,sender_id,receiver_id)
	print(q)
	res1=select(q)
	data['msg']=res1

	
	if 'submit' in request.form:
		msg=request.form['message']
		q="insert into chat values(null,'%s','%s','%s')"%(sender_id,receiver_id,msg)
		insert(q)
		return redirect(url_for('doctor.doctor_message',receiver_id=receiver_id))
	return render_template("doctor_message.html",data=data)


@doctor.route('/doctor_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	q="SELECT * FROM feedback inner join user using(user_id)  "
	res=select(q)
	data['tr']=res

	return render_template('doctor_view_feedback.html',data=data)


@doctor.route('/doctor_schedule',methods=['get','post'])
def doctor_schedule():
	data={}
	did=session['did']

	from datetime import date,datetime 
	today=date.today() 
	data['today']=today


	q3="select * from schedule where doctor_id='%s'"%(did)
	res=select(q3)
	data['sch']=res

	

	if 'submit' in request.form:
		dt=request.form['date']
		st=request.form['st']
		et=request.form['et']
		inte=request.form['inte']
		fee=request.form['fee']

           

		dss = dt

		# Split the string into a list using comma as separator
		new_dss = dss.split(",")

		# Join the list elements with a comma separator and print
		print(",".join(new_dss))

		for i in new_dss:
			print(i)

			q="select * from schedule where available_date='%s' and doctor_id='%s'"%(dt,did)
			res=select(q)
			if res:
				return HttpResponse("<script>alert('Choose Another Date....!!');window.location='/doctor_schedule';</script>")
			else:
				q="insert into schedule values(null,'%s','%s','%s','%s','%s','%s')"%(did,i,st,et,inte,fee)
				insert(q)
				# return HttpResponse("<script>alert('Added Successfully....!!');window.location='/doctor_schedule_time';</script>")
	return render_template("doctor_schedule.html",data=data)

