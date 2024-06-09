from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/about')
def about():
    return render_template('about.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        username=request.form['name']
        password=request.form['password']

        print(username,password)
        q="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(q)
        if res:
            session['username']=res[0]['username']
            uid=session['username']
            if res[0]['usertype']=="admin":
                return redirect(url_for("admin.adminhome"))
            elif res[0]['usertype']=="customer":
                
                q="select * from tbl_customer where username='%s' and c_status='1'"%(uid)
                val=select(q)
                if val:
                    session['cid']=val[0]['c_id']
                    cid=session['cid']
                
                    session['name']=val[0]['c_fname']
                    name=session['name']
                    return redirect(url_for("customer.custhome"))
                else:
                    flash("you are inactive")
                    return redirect(url_for("public.login"))
            elif res[0]['usertype']=="staff":
                q="select * from tbl_staff where username='%s' and s_status='1'"%(uid)
                val=select(q)
                if val:
                    session['sid']=val[0]['s_id']
                    sid=session['sid']
                
                    session['name']=val[0]['s_fname']
                    name=session['name']
                

                    return redirect(url_for("staff.staffhome"))
                else:
                    flash("you are inactive")
                    return redirect(url_for("public.login"))
                
        else:
             flash("Invalid Username or Password")
             return redirect(url_for('public.login'))
    return render_template("login.html")


    

@public.route('/reg',methods=['get','post'])
def reg():
    if 'submit' in request.form:
        c_fname=request.form['fname']
        c_lname=request.form['lname']
        c_housename=request.form['housename']
        c_place=request.form['place']
        c_pin=request.form['pin']
        c_phno=request.form['phno']
        username=request.form['uname']
        password=request.form['password']
        re="select * from tbl_customer where username='%s'"%(username)
        es=select(re)
        if es:
            flash("Customer already registered")
            return redirect(url_for("public.reg"))
        else:

            q="insert into login values('%s','%s','customer')"%(username,password)
            insert(q)

            username=request.form['uname']
            q="insert into tbl_customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s',null)"%(c_fname,c_lname, c_housename,c_place,c_pin,c_phno,username,password)
            insert(q)
            flash("successfully registerd")
            return redirect(url_for('public.login'))

    return render_template("reg.html")