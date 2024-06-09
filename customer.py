from flask import *
from database import *
import uuid

customer=Blueprint('customer',__name__)
@customer.route('/custhome',methods=['get','post'])
def custhome():
    data={}
    if 'search' in request.form:
      name=request.form['name']
      print(name)
      q="select * from tbl_customer where _fname LIKE '%s'"%(name)
      res=select(q)
      data['res']=res
    else:
      
       cid=session['cid']
       username=session['username']
	
    
       q="select * from tbl_building inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where c_id!='%s' and  status=1"%(cid)
       res=select(q)
       data['res']=res
    
       data['name']=session['name']

    return render_template('custhome.html',data=data)

@customer.route('/buildingview')
def buildingview():
    data={}
    id=request.args['id']
    q="select * from tbl_building inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where buil_id='%s'"%(id)
    res=select(q)
    data['spro']=res


    return render_template('buildingview.html',data=data)
@customer.route('/notification')
def notification():
    data={}
    cid=session['cid']
    q="select * from tbl_customer inner join tbl_sales using(c_id) inner join tbl_building using(buil_id) inner join  tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where tbl_building.c_id='%s' and tbl_sales.salesstatus='1'"%(cid) 
    print(q)
    res=select(q)
    print(res)
    if res:
     
     data['spro']=res
     builid=res[0]['buil_id']

   
    else:
       flash("no new notifications") 
       return redirect(url_for("customer.custhome"))
     
    if "action" in request.args:
          action=request.args['action']
          cid=request.args['cid']

    else:
          action=None
    
    if action=="active":

            q="update tbl_sales set salesstatus='accept' where b_id='%s'"%(cid)
            update(q)
            flash("property allowed to buy")
            return redirect(url_for("customer.custhome"))
    if action=="inactive":
            s="update tbl_sales set salesstatus='0' where b_id='%s'"%(cid)
            update(s)
            return redirect(url_for("customer.custhome"))
    
        

    return render_template('notification.html',data=data)  
@customer.route('/viewcart')
def viewcart():
    data={}
    cid=session['cid']
    q="select * from tbl_sales inner join tbl_building using(buil_id) inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where tbl_sales.c_id='%s'and tbl_building.status='1' and tbl_sales.salesstatus='accept'"%(cid) 
    res=select(q)
    if res:
     data['spro']=res
     builid=data['spro'][0]['buil_id']
     w="select * from tbl_building inner join tbl_customer using(c_id) where buil_id='%s'"%(builid)
     sp=select(w)
     data['s']=sp
    else:
        flash("no bookings")
        return redirect(url_for("customer.custhome"))
        

    return render_template('viewcart.html',data=data)  

@customer.route('/addbuildcus',methods=['get','post'])
def addbuildcus():
    data={}
    cid=session['cid']
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
        


        q="insert into tbl_building values(null,'%s','%s','%s','%s','%s','%s','%s',1,'%s','%s','%s','%s','%s')"%(ptype,cat,subcat,sq,cid,price,path,place,district,houseno,path1,path2)
        insert(q)
        flash("Building added successfully")
        return redirect(url_for("customer.custhome"))
        
    


    return render_template('addbuildcus.html',data=data)    

@customer.route('/cart',methods=['get','post'])
def cart():
    data={}
    id=request.args['id']
    price=request.args['price']
    data['price']=price
    
    cid=session['cid']
    builid=request.args['id']
    price=request.args['price'] 
    q="insert into tbl_sales values(null,'%s','%s','%s','%s')"%(cid,builid,price,'1')
    insert(q)
    flash("successful in sending the proposal to the owner")
    return redirect(url_for("customer.custhome"))    

    
    
    
    return render_template('cart.html',data=data)
@customer.route('/buildview2',methods=['get','post'])
def buildview2():
    data={}
    id=request.args['id']
    q="select * from tbl_building inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where buil_id='%s'"%(id)
    res=select(q)
    data['spro']=res    
    
    
    return render_template('buildview2.html',data=data)
@customer.route('/addcard',methods=['get','post'])
def addcard():
    data={}
    d={}
    cid=session['cid']
    
    q="SELECT tbl_building.price,tbl_building.buil_id,tbl_sales.b_id FROM tbl_sales INNER JOIN tbl_building USING(buil_id) where tbl_sales.c_id='%s' and tbl_sales.salesstatus='accept'"%(cid) 
    print(q)
    res=select(q)
    data['spro']=res
    price=data['spro'][0]['price']
    rem=price-100000
    
    builid=data['spro'][0]['buil_id']
    salesid=data['spro'][0]['b_id']

    print(rem)

    if 'submit' in request.form:
        cardno=request.form['cardno']
        expiry=request.form['expiry']
        re="select * from tbl_card where card_no='%s'"%(cardno)
        resu=select(re)
        if resu:
            flash("Card already added")
        else:
         r="insert into tbl_card values(null,'%s','%s','%s')"%(cid,cardno,expiry)
         c=insert(r)
         print(c)
        u="select * from tbl_card where c_id='%s'"%(cid)
        t=select(u)
        print(t)
        
        re="insert into tbl_payment values(null,'%s','%s',curdate())"%(salesid,c)
        insert(re)
        w="update tbl_building set status='0' where buil_id='%s'"%(builid) 
        update(w)
        w="update tbl_sales set salesstatus='booked' where b_id='%s'"%(salesid) 
        update(w)

        flash("Payment successful")
        return redirect(url_for("customer.bill"))




    return render_template('addcard.html',data=data)  
@customer.route('/myproperties',methods=['get','post'])
def cmyproperties():
    data={}
    cid=session['cid']
    username=session['username']
	
    
    q="select * from tbl_building inner join tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where c_id='%s' and  status=1"%(cid)
    res=select(q)
    data['res']=res
    
    

    return render_template('myproperties.html',data=data)

@customer.route('/bill',methods=['get','post'])
def bill():
    data={}
    cid=session['cid']
    username=session['username']
	
    
    q="select * from tbl_customer inner join tbl_card using(c_id) inner join tbl_payment using(card_id) inner join tbl_sales using(b_id) inner join tbl_building using(buil_id) where salesstatus='booked' and tbl_sales.c_id='%s'"%(cid)
    res=select(q)
    data['spro']=res
    builid=res[0]['buil_id']

    w="select * from tbl_building inner join  tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where buil_id='%s'"%(builid)
    re=select(w)
    data['t']=re

    return render_template('bill.html',data=data)

@customer.route('/billprint',methods=['get','post'])
def billprint():
    data={}
    cid=session['cid']
    username=session['username']
	
    
    q="select * from tbl_customer inner join tbl_card using(c_id) inner join tbl_payment using(card_id) inner join tbl_sales using(b_id) inner join tbl_building using(buil_id) where salesstatus='booked' and tbl_sales.c_id='%s'"%(cid)
    res=select(q)
    data['spro']=res
    builid=res[0]['buil_id']

    w="select * from tbl_building inner join  tbl_propertytype using(ptype_id) inner join tbl_category using(cat_id) inner join tbl_subcategory using(subcat_id) where buil_id='%s'"%(builid)
    re=select(w)
    data['t']=re

    return render_template('billprint.html',data=data)
