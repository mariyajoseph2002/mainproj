from flask import *
from database import *

staff=Blueprint('staff',__name__)

@staff.route('/staffhome')
def staffhome():
    data={}
    data['name']=session['name']

    return render_template('staffhome.html',data=data)

@staff.route('/spropertyadd',methods=['get','post'])
def spropertyadd():
      data={}

      
      sid=session['sid']
      if 'submit' in request.form:
        ptype_name=request.form['name']
        r="select * from tbl_propertytype where ptype_name='%s'"%(ptype_name)
        res=select(r)
        if res:
            flash("Property type already added")
            return redirect(url_for("staff.spropertyadd"))
        else:
       

         q="insert into tbl_propertytype values(null,'%s','%s')"%(ptype_name,sid)
         insert(q)
         flash("Property type added successfully")
         return redirect(url_for("staff.spropertyadd"))

      
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
        return redirect(url_for("staff.spropertyadd")) 

      return render_template('spropertyadd.html',data=data)
@staff.route('/scategoryadd',methods=['get','post'])
def scategoryadd():
      data={}
      sid=session['sid']
      if 'submit' in request.form:
        cat_name=request.form['name']
        r="select * from tbl_category where cat_name='%s'"%(cat_name)
        res=select(r)
        if res:
            flash("Category already added")
            return redirect(url_for("staff.scategoryadd"))
        else:

          q="insert into tbl_category values(null,'%s','%s')"%(cat_name,sid)
          insert(q)
          flash("Category added successfully")
          return redirect(url_for("staff.scategoryadd"))

      
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
        return redirect(url_for("staff.scategoryadd"))

      return render_template('scategoryadd.html',data=data)
      
@staff.route('/ssubcategoryadd',methods=['get','post'])
def ssubcategoryadd():
      data={}
      sid=session['sid']
      if 'submit' in request.form:
        subcat_name=request.form['name']
        r="select * from tbl_subcategory where subcat_name='%s'"%(subcat_name)
        res=select(r)
        if res:
            flash("Subcategory already added")
            return redirect(url_for("staff.ssubcategoryadd"))
        else:

         q="insert into tbl_subcategory values(null,'%s','%s')"%(subcat_name,sid)
         insert(q)
         flash("Subcategory added successfully")
         return redirect(url_for("staff.ssubcategoryadd"))

      
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
        return redirect(url_for("staff.ssubcategoryadd"))

      return render_template('ssubcategoryadd.html',data=data)