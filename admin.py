from flask import *
from database import *
import uuid
import pprint
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    data={}
    s="select count(c_id) as ccount from tbl_customer"
    re=select(s)
    print(re)
    data['c']=re[0]['ccount']
    s="select count(buil_id)  as bcount from tbl_building where status=1"
    re=select(s)
    data['b']=re[0]['bcount']
    s="select b_id from tbl_sales where salesstatus='booked'"
    re=select(s)
    r=re.count
    print(r)
    data['s']=re

    return render_template('adminhome.html',data=data)
@admin.route('/customerdisp',methods=['get','post'])
def customerdisp():
  data={}
  if 'search' in request.form:
   name=request.form['name']
   print(name)
   q="select * from tbl_customer where c_fname LIKE '%s'"%(name)
   res=select(q)
   data['res']=res
  else:
   q="select * from tbl_customer"
   res=select(q)
   data['res']=res

  if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

  else:
          action=None
    
  if action=="inactive":
          q="update tbl_customer set c_status='0' where c_id='%s'"%(cid)
          update(q)
          return redirect(url_for("admin.customerdisp"))
  if action=="active":
          s="update tbl_customer set c_status='1' where c_id='%s'"%(cid)
          update(s)
          return redirect(url_for("admin.customerdisp"))
  return render_template('customerdisp.html',data=data)

@admin.route('/cusreport')
def cusreport():
  data={}
  q="select * from tbl_customer"
  res=select(q)
  data['res']=res
  
  return render_template('cusreport.html',data=data)

@admin.route('/staffreport')
def staffreport():
  data={}
  pprint.pprint(session)
  q="select * from tbl_staff"
  res=select(q)
  data['res']=res
  
  return render_template('staffreport.html',data=data)

@admin.route('/staffadd',methods=['get','post'])
def staffadd():
      if 'submit' in request.form:
        username=request.form['uname']
        s_fname=request.form['fname']
        s_lname=request.form['lname']
        s_phno=request.form['phno']
        s_city=request.form['city']
        password=request.form['password']
        re="select * from tbl_staff where username='%s'"%(username)
        es=select(re)
        if es:
            flash("Staff already added")
            return redirect(url_for("admin.staffadd"))
        else:

            q="insert into login values('%s','%s','staff')"%(username,password)
            insert(q)

            username=request.form['uname']
            q="insert into tbl_staff values(null,'%s','%s','%s','%s','%s','%s','1')"%(username,s_fname,s_lname,s_phno,s_city,password)

            insert(q)
            flash("successfully added")
            return redirect(url_for("admin.staffadd"))

      data={}
      q="select * from tbl_staff"
      res=select(q)
      data['res']=res
      if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

      else:
          action=None
    
      if action=="inactive":
          q="update tbl_staff set s_status='0' where s_id='%s'"%(cid)
          update(q)
          return redirect(url_for("admin.staffadd"))
      if action=="active":
          s="update tbl_staff set s_status='1' where s_id='%s'"%(cid)
          update(s)
          return redirect(url_for("admin.staffadd"))
    
      if action=="update":
          q="select * from tbl_staff where s_id='%s'"%(cid)
          res=select(q)
          data['up']=res
        
      if 'update' in request.form:
        username=request.form['uname']
        s_fname=request.form['fname']
        s_lname=request.form['lname']
        s_phno=request.form['phno']
        s_city=request.form['city']
        password=request.form['password']
        q="update tbl_staff set username='%s',s_fname='%s',s_lname='%s',s_phno='%s',s_city='%s' where s_id='%s'"%(username,s_fname,s_lname,s_phno,s_city,cid)
        update(q)
        flash("successfully updated")
        return redirect(url_for("admin.staffadd"))
      return render_template('staffadd.html',data=data)

   
      
@admin.route('/propertyadd',methods=['get','post'])
def propertyadd():
      if 'submit' in request.form:
        ptype_name=request.form['name']
        r="select * from tbl_propertytype where ptype_name='%s'"%(ptype_name)
        res=select(r)
        if res:
            flash("Property type already added")
            return redirect(url_for("admin.propertyadd"))
        else:
       

         q="insert into tbl_propertytype values(null,'%s',null)"%(ptype_name)
         insert(q)
         flash("Property type added successfully")
         return redirect(url_for("admin.propertyadd"))

      data={}
      q="select * from tbl_propertytype"
      res=select(q)
      data['res']=res
      if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

      else:
          action=None
      if action=="update":
          q="select * from tbl_propertytype where ptype_id='%s'"%(cid)
          res=select(q)
          data['up']=res
        
      if 'update' in request.form:
        ptype_name=request.form['name']
        q="update tbl_propertytype set ptype_name='%s'where ptype_id='%s'"%(ptype_name,cid)
        update(q)
        flash("successfully updated")
        return redirect(url_for("admin.propertyadd")) 

      return render_template('propertyadd.html',data=data)
@admin.route('/categoryadd',methods=['get','post'])
def categoryadd():
      if 'submit' in request.form:
        cat_name=request.form['name']
        r="select * from tbl_category where Cat_Name='%s'"%(cat_name)
        res=select(r)
        if res:
            flash("Category already added")
            return redirect(url_for("admin.categoryadd"))
        else:

          q="insert into tbl_category values(null,'%s',null)"%(cat_name)
          insert(q)
          flash("Category added successfully")
          return redirect(url_for("admin.categoryadd"))

      data={}
      q="select * from tbl_category"
      res=select(q)
      data['res']=res
      if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

      else:
          action=None
      if action=="update":
          q="select * from tbl_category where cat_id='%s'"%(cid)
          res=select(q)
          data['up']=res
        
      if 'update' in request.form:
        cat_name=request.form['name']
        q="update tbl_category set cat_name='%s'where cat_id='%s'"%(cat_name,cid)
        update(q)
        flash("successfully updated")
        return redirect(url_for("admin.categoryadd"))

      return render_template('categoryadd.html',data=data)
      
@admin.route('/subcategoryadd',methods=['get','post'])
def subcategoryadd():
      if 'submit' in request.form:
        subcat_name=request.form['name']
        r="select * from tbl_subcategory where subcat_name='%s'"%(subcat_name)
        res=select(r)
        if res:
            flash("Subcategory already added")
            return redirect(url_for("admin.subcategoryadd"))
        else:

         q="insert into tbl_subcategory values(null,'%s',null)"%(subcat_name)
         insert(q)
         flash("Subcategory added successfully")
         return redirect(url_for("admin.subcategoryadd"))

      data={}
      q="select * from tbl_subcategory"
      res=select(q)
      data['res']=res
      if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

      else:
          action=None
      if action=="update":
          q="select * from tbl_subcategory where subcat_id='%s'"%(cid)
          res=select(q)
          data['up']=res
        
      if 'update' in request.form:
        subcat_name=request.form['name']
        q="update tbl_subcategory set subcat_name='%s'where subcat_id='%s'"%(subcat_name,cid)
        update(q)
        flash("successfully updated")
        return redirect(url_for("admin.subcategoryadd"))

      return render_template('subcategoryadd.html',data=data)

@admin.route('/buildingadd',methods=['get','post'])
def buildingadd():
    data={}
    q="select * from tbl_propertytype"
    res=select(q)
    data['ptype']=res
    q1="select * from tbl_category"
    res=select(q1)
    data['cat']=res

    q2="select * from tbl_subcategory"
    res=select(q2)
    data['subcat']=res
    
   
    
    if 'submit' in request.form:
        ptype=request.form['ptype']
        cat=request.form['cat']
        subcat=request.form['subcat']
        sq=request.form['sq']
        price=request.form['price']
        img=request.files['img']
        path='static/uploads/'+str(uuid.uuid4())+img.filename 
        img.save(path)
        place=request.form['place']
        district=request.form['district']
        houseno=request.form['houseno']
        img1=request.files['img1']
        path1='static/uploads/'+str(uuid.uuid4())+img1.filename 
        img1.save(path1)
        img2=request.files['img2']
        path2='static/uploads/'+str(uuid.uuid4())+img2.filename 
        img2.save(path2)
        q="insert into tbl_building values(null,'%s','%s','%s','%s',0,'%s','%s',1,'%s','%s','%s','%s','%s')"%(ptype,cat,subcat,sq,price,path,place,district,houseno,path1,path2)
        insert(q)
        flash("Building added successfully")
        return redirect(url_for("admin.buildingadd"))
        
    q="select * from tbl_building inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) inner join tbl_customer using(c_id)"
    res=select(q)
    data['res']=res
    if "action" in request.args:
        action=request.args['action']
        cid=request.args['cid']

    else:
        action=None
    
    
    
    if action=="update":
        q="select * from tbl_building where buil_id='%s'"%(cid)
        res=select(q)
        data['up']=res
        
    if 'update' in request.form:
        ptype=request.form['ptype']
        cat=request.form['cat']
        subcat=request.form['subcat']
        sq=request.form['sq']
        price=request.form['cat']
        
        img=request.files['img']
        q="update tbl_building set ptype_id='%s',cat_id='%s',subcat_id='%s',square_feet='%s','0',price='%s',image='%s' where buil_id='%s'"%(ptype,cat,subcat,sq,price,img)
        update(q)
        return redirect(url_for("admin.buildingadd"))
    
   
    
    return render_template('buildingadd.html',data=data)
@admin.route('/salesdisp',methods=['get','post'])
def salesdisp():
  data={}
  if "sale" in request.form:
     daily=request.form['daily']
     if request.form['monthly']=="":
       monthly=""
     else:
        monthly=request.form['monthly']+'%'
     print(monthly)
     customer=request.form['customer']	
     q="SELECT * FROM tbl_customer inner join tbl_card using(c_id) inner join tbl_payment using(card_id) INNER JOIN tbl_sales USING (`b_id`) INNER JOIN `tbl_building` USING (`buil_id`)   WHERE (`tbl_payment`.`payment_date` LIKE '%s' AND salesstatus='booked') OR (`tbl_payment`.`payment_date` LIKE '%s' AND salesstatus='booked') OR (`c_fname` LIKE '%s' AND salesstatus='booked')  "%(daily,monthly,customer)
     res=select(q)
     print(q)
     print(q)
     data['report']=res
  else:
   q="select * from tbl_customer inner join tbl_card using(c_id) inner join tbl_payment using(card_id) inner join tbl_sales using(b_id) inner join tbl_building using(buil_id)  "
   
   res=select(q)
   data['report']=res
   session['res']=res
   r=session['res']
  
  
         
  return render_template('salesdisp.html',data=data)
@admin.route('/paymentreport')
def paymentreport():
	data={}

	r=session['res']
	data['r']=r


	return render_template('paymentreport.html',data=data)

@admin.route('/report')
def report():
    data={}

    r=session['res']
    data['r']=r

    return render_template('report.html',data=data)

@admin.route('/proposalreport')
def proposalreport():
  data={}
        
  q="select * from tbl_customer inner join tbl_sales using(c_id) inner join tbl_building using (buil_id)  where salesstatus='booked' or salesstatus='accept'"
  res=select(q)
  data['report']=res
  

  q="select *from  tbl_customer inner join tbl_sales using(c_id) inner join tbl_building using (buil_id) where salesstatus='0'"
  re=select(q)
  data['rep']=re
  

  return render_template('proposalreport.html',data=data)

@admin.route('/proposalprint')
def proposalprint():
  data={}
        
  q="select * from tbl_customer inner join tbl_sales using(c_id) inner join tbl_building using (buil_id)  where salesstatus='booked' or salesstatus='accept'"
  res=select(q)
  data['report']=res
  buil=res[0]['buil_id']
  qe="select * from  tbl_building  inner join tbl_customer using(c_id) where buil_id='%s' "%(buil)
  re=select(qe)
  data['report1']=re

  q="select *from  tbl_customer inner join tbl_sales using(c_id) inner join tbl_building using (buil_id) where salesstatus='0'"
  re=select(q)
  data['rep']=re
  

  return render_template('proposalprint.html',data=data)



