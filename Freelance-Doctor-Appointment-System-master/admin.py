from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_department',methods=['get','post'])
def admin_manage_department():
	data={}
	q="select * from department"
	data['tr']=select(q)
	if 'submit' in request.form:
		fname=request.form['fname']
		des=request.form['des']
		
		q="insert into department values(null,'%s','%s')"%(fname,des)
		insert(q)
		print(q)
		return redirect(url_for('admin.admin_manage_department'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="delete":
		q="delete from department where department_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_department'))

	if action=="update":
		q="select * from department where department_id='%s'"%(id)
		res=select(q)
		data['up']=res


	if 'update' in request.form:
		fname=request.form['fname']
		des=request.form['des']
		q="update department set department='%s',description='%s' where department_id='%s'"%(fname,des,id)
		update(q)
		flash("updated")
		return redirect(url_for('admin.admin_manage_department'))
		

	return render_template("admin_manage_department.html",data=data)

@admin.route('/admin_view_request',methods=['get','post'])
def admin_view_request():
	data={}
	q="SELECT * FROM doctor inner join request using(doctor_id) "
	res=select(q)
	data['tr']=res


	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="accept":
		q="update request set status='accept' where request_id='%s'"%(id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_view_request'))

	if action=="reject":
		q="update login set status='reject'   where request_id='%s'"%(id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_view_request'))

	return render_template('admin_view_request.html',data=data)


@admin.route('/admin_view_patient',methods=['get','post'])
def admin_view_patient():
	data={}
	q="SELECT * FROM user  "
	res=select(q)
	data['tr']=res

	return render_template('admin_view_patient.html',data=data)

@admin.route('/admin_view_doctor',methods=['get','post'])
def admin_view_doctor():
	data={}
	q="SELECT * FROM doctor inner join login using(login_id) inner join department on department.department_id=doctor.dept_id "
	res=select(q)
	data['tr']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="accept":
		q="update login set usertype='doctor' where login_id='%s'"%(id)
		update(q)
		q="update doctor set status='active' where login_id='%s'"%(id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_view_doctor'))

	if action=="reject":
		q="update login set usertype='reject'  where login_id='%s'"%(id)
		update(q)
		q="update doctor set status='inactive'  where login_id='%s'"%(id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_view_doctor'))

	if action=="delete":
		q="delete from doctor  where login_id='%s'"%(id)
		delete(q)
		flash('deleted successfully')
		return redirect(url_for('admin.admin_view_doctor'))

	return render_template('admin_view_doctor.html',data=data)


@admin.route('/admin_view_booking',methods=['get','post'])
def admin_view_booking():
	data={}
	q="SELECT * FROM booking INNER JOIN USER USING(user_id) INNER JOIN `payment` USING(booking_id)"
	res=select(q)
	data['tr']=res

	return render_template('admin_view_booking.html',data=data)

@admin.route('/admin_view_payment',methods=['get','post'])
def admin_view_payment():
	data={}
	q="SELECT * FROM payment inner join booking using(booking_id) inner join user using(user_id) "
	res=select(q)
	data['tr']=res

	return render_template('admin_view_payment.html',data=data)


@admin.route('/admin_view_treatment',methods=['get','post'])
def admin_view_treatment():
	data={}
	q="SELECT * FROM treatment INNER JOIN booking USING(booking_id) INNER JOIN USER USING(user_id)  "
	res=select(q)
	data['tr']=res

	return render_template('admin_view_treatment.html',data=data)

@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	q="SELECT * FROM feedback inner join user using(user_id)  "
	res=select(q)
	data['tr']=res

	return render_template('admin_view_feedback.html',data=data)




@admin.route('/admin_add_doc_salary',methods=['get','post'])
def admin_add_doc_salary():
	data={}
	q="select * from department"
	print(q)
	res=select(q)
	data['sals']=res

	if 'next' in request.form:
		dept=request.form['dept']
		return redirect(url_for('admin.select_doctor',dept=dept))

	q="SELECT * FROM `salary` INNER JOIN `doctor` USING(doctor_id) INNER JOIN `department` ON `department`.`department_id`=`doctor`.`dept_id`"
	res=select(q)
	data['sal']=res
	return render_template('admin_add_doc_salary.html',data=data)



@admin.route('/select_doctor',methods=['get','post'])
def select_doctor():
	data={}
	dept=request.args['dept']

	q="select * from doctor where dept_id='%s'"%(dept)
	res=select(q)
	data['doc']=res

	if 'pay' in request.form:
		doc=request.form['doc']
		sal=request.form['sal']
		mon=request.form['mon']
		q="select * from salary where month='%s' and doctor_id='%s'"%(mon,doc)
		res=select(q)
		if res:
			flash("Already Paid")
		else:
			return redirect(url_for('admin.pay_salary',doc=doc,sal=sal,mon=mon))
	return render_template('select_doctor.html',data=data)




@admin.route('/pay_salary',methods=['get','post'])
def pay_salary():
	data={}
	doc=request.args['doc']
	sal=request.args['sal']
	mon=request.args['mon']
	data['amt']=sal
	

	if 'submit' in request.form:

		q="insert into salary values(null,'%s','%s',curdate(),'%s')"%(doc,sal,mon)
		insert(q)
		flash("Paid successfully")
		return redirect(url_for('admin.admin_add_doc_salary'))
		return redirect(url_for('admin.pay_salary',doc=doc,sal=sal))


	return render_template('pay_salary.html',data=data)



@admin.route('/admin_managereport',methods=['post','get'])	
def admin_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		doc=request.form['doctor']
		user=request.form['user']	
		q="SELECT *,doctor.fname AS doctor,`user`.fname AS `USER` FROM booking INNER JOIN `schedule` USING (schedule_id) inner join payment using(booking_id)INNER JOIN treatment USING(booking_id)  INNER JOIN `user` USING(user_id) INNER JOIN doctor USING(doctor_id) INNER JOIN department ON department.department_id=doctor.dept_id where (`doctor`.fname like '%s')or (`USER`.fname like '%s') or (`treatment`.date like '%s'  ) or (`treatment`.date like '%s' ) "%(doc,user,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT *,doctor.fname AS doctor,`user`.fname AS `USER` FROM booking INNER JOIN `schedule` USING (schedule_id)INNER JOIN treatment USING(booking_id)  INNER JOIN `user` USING(user_id) INNER JOIN doctor USING(doctor_id) INNER JOIN department ON department.department_id=doctor.dept_id"
		res=select(q)
		data['report']=res
	
	return render_template('admin_manage_report.html',data=data)