from flask import *
from database import *
user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
	return render_template('user_home.html')

@user.route('/user_view_profile',methods=['get','post'])
def user_view_profile():
	data={}

	uid=session['uid']
	q="SELECT * FROM user inner join login using(login_id) where user_id='%s'"%(uid)
	res=select(q)
	data['tr']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="update":
		q="select * from user  where user_id='%s'"%(id)
		res=select(q)
		data['updated']=res


	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		# gender=request.form['gender']
		q="update user set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where user_id='%s'"%(fname,lname,place,phone,email,id)
		update(q)
		flash("updated successfully")
		
		return redirect(url_for('user.user_view_profile'))
	return render_template('user_view_profile.html',data=data)


@user.route('/user_view_doctor', methods=['GET', 'POST'])
def user_view_doctor():
    data = {}

    # Default query to fetch all active doctors
    q = """
        SELECT doctor.*, department.department 
        FROM doctor
        INNER JOIN department ON department.department_id = doctor.dept_id
        WHERE doctor.status = 'active'
    """

    if "search" in request.form:
        search_query = request.form.get('search_query', '').strip()

        # Search by department and location
        if search_query:
            q += """ AND (
                        department.department LIKE '%%%s%%' OR 
                        doctor.place LIKE '%%%s%%'
                    )""" % (search_query, search_query)

    res = select(q)
    data['tr'] = res

    return render_template('user_view_doctor.html', data=data)




@user.route('/user_select_timing',methods=['get','post'])
def user_select_timing():
	from datetime import date,datetime,timedelta

	data={}
	uid=session['uid']

	id=request.args['id']
	date=request.args['date']
	data['date']=date


	q="SELECT * FROM `schedule` where schedule_id='%s'"%(id)
	r=select(q)
	if r:
		print(q)
		data['con']=r


		x = r[0]['starting_time']
		y = r[0]['ending_time']
		ttt=r[0]['interval']
		ttime=int(ttt)
		hour_and_minute=x
		date_time_obj = datetime.strptime(x, '%H:%M')
		s=[]
		while hour_and_minute<y:
			if hour_and_minute<y:
				date_time_obj += timedelta(minutes=ttime)
				hour_and_minute = date_time_obj.strftime("%H:%M")
				print(hour_and_minute)

				s.append(hour_and_minute)
				
			else:
				break
		data['s']=s
		print(s)
		q = "SELECT atime FROM booking WHERE adate='%s' AND status='accept'" % (date)

		booked_slots = [row['atime'] for row in select(q)]
		data['booked'] = booked_slots  # Store booked slots in data	


	if 'time' in request.form:
		date=request.form['date']
		reason=request.form['reason']
		time=request.form['time']
		q="select * from booking where adate='%s' and atime='%s'"%(date,time)
		res=select(q)
		if res:
			flash("Please Choose Another Time")
		else:
			q="insert into booking values(null,'%s','%s','%s','%s','%s','%s')"%(id,session['uid'],date,time,reason,'pending')
			insert(q)
			print(q)
			flash("Appointment request has successfully send.....!!!")
			return redirect(url_for('user.user_view_booking'))
	return render_template('user_select_timing.html',data=data)

@user.route('/user_view_treatment',methods=['get','post'])
def user_view_treatment():
	data={}
	uid=session['uid']
	q="SELECT * FROM treatment INNER JOIN booking USING(booking_id)  INNER JOIN `schedule` USING(schedule_id) INNER JOIN DOCTOR USING(doctor_id) inner join login using(login_id) where user_id='%s'"%(uid) 
	res=select(q)
	data['tr']=res

	return render_template('user_view_treatment.html',data=data)



@user.route('/user_make_appoinment',methods=['get','post'])
def user_make_appoinment():
	data={}
	id=request.args['id']


	q="select * from schedule where doctor_id='%s'"%(id)
	res=select(q)
	data['sch']=res
	print(res)


	# q="select * from booking where user_id='%s'"%(session['uid'])
	# data['bok']=select(q)


	# if 'submit' in request.form:
	# 	det=request.form['detail']
	# 	id=request.args['id']
	# 	q="insert into booking values(null,'%s','%s','%s','pending',curdate())"%(id,session['uid'],det)
	# 	insert(q)
	# 	print(q)
	# 	return redirect(url_for('user.user_view_doctor'))

	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	id=request.args['id']

	# else:
	# 	action=None

	# if action=="delete":
	# 	q="delete from booking where booking_id='%s'"%(id)
	# 	delete(q)
	# 	return redirect(url_for('user.user_view_doctor'))

	return render_template('user_make_appoinment.html',data=data)

@user.route('/user_view_booking',methods=['get','post'])
def user_view_booking():
	data={}
	q="SELECT *,booking.status AS b_st FROM booking INNER JOIN SCHEDULE USING (schedule_id) INNER JOIN doctor USING (doctor_id) INNER JOIN department ON department.department_id=doctor.dept_id WHERE user_id='%s'"%(session['uid'])
	print(q)
	res=select(q)
	print(res)
	data['bok']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="delete":
		q="delete from booking where booking_id='%s'"%(id)
		delete(q)
		flash("refunded your amount..!")
		return redirect(url_for('user.user_view_doctor'))

	return render_template('user_view_booking.html',data=data)


@user.route('/user_make_payment',methods=['get','post'])
def user_make_payment():
	data={}
	amt=request.args['amt']
	data['amt']=amt
	

	if 'submit' in request.form:
		det=request.form['amt']
		exp=request.form['exp']
		card=request.form['card']
		cvv=request.form['cvv']
		id=request.args['id']
		q="insert into payment values(null,'%s',curdate(),'%s')"%(id,det)
		insert(q)
		q="update booking set status='paid' where booking_id='%s'"%(id)
		update(q)
		flash("paid successfully")
		print(q)
		return redirect(url_for('user.user_view_doctor'))

	return render_template('user_make_payment.html',data=data)

@user.route('/viewinvoice')
def viewinvoice():
    data={}
    from datetime import date,datetime 
    today=date.today()
    data['today']=today
    omid=request.args['id']
    q="SELECT *,payment.date as p_date FROM booking INNER JOIN payment USING (booking_id) INNER JOIN `schedule` USING(schedule_id) INNER JOIN doctor USING(doctor_id) INNER JOIN department ON doctor.dept_id=department.department_id WHERE user_id='%s' and booking_id='%s'"%(session['uid'],omid)
    print(q)
    data['pay']=select(q)
    return render_template("bill.html",data=data)



@user.route('/user_chat')
def psycho_chat():
	data={}
	q="select * from doctor where status='active'"
	res=select(q)
	data['tr']=res

	return render_template("user_chat.html",data=data)


@user.route('/user_message',methods=['get','post'])
def user_message():
	data={}

	
	id=request.args['id']
	uid=session['lid']
	
	data['user']=uid
	data['psycho'] =uid

	q="select * from chat where (sender_id='%s' and receiver_id='%s') or (receiver_id='%s' or sender_id='%s')"%(uid,id,uid,id)
	res1=select(q)
	data['msg']=res1
	if 'submit' in request.form:
		msg=request.form['message']
		q="insert into chat values(null,'%s','%s','%s')"%(uid,id,msg)
		insert(q)
		flash("send message..")
		return redirect(url_for('user.user_message',id=id))
	return render_template("user_message.html",data=data)



@user.route('/patient_add_feedback',methods=['get','post'])
def patient_add_feedback():
	data={}
	uid=session['uid']
	q="select * from feedback where user_id='%s'"%(session['uid'])
	data['feed']=select(q)

	if 'submit' in request.form:
		feed=request.form['feed']
		q="insert into feedback values(null,'%s','%s',curdate())"%(uid,feed)
		insert(q)
		print(q)
		flash("send successfully..")
		return redirect(url_for('user.patient_add_feedback'))

	

	return render_template('patient_add_feedback.html',data=data)