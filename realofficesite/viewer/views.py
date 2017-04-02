from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import sqlite3 as sq

# Create your views here.
from django.http import HttpResponse

@csrf_exempt
def index(response):
    return render(response,'viewer/test.html')

def edit_favorites(request):
    if request.is_ajax():
        message = "YES,Ajax!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)

def test(request):
    data = request.body
    print(data)
    print(data.split())
    s=data.split()
    venue_name = s[0]
    capacity = s[1]
    conn = sq.connect('realoffice.db')
    print("Opened database successfully")
    print(venue_name)
    v=str(venue_name).replace("b'","\"").replace("'","\"")
    print(v)
    c_venue=venue_name[2:-1]
    print(c_venue)
    cursor = conn.execute('SELECT * FROM VENUE WHERE VENUE_NAME = ' + str(v) + ' AND VENUE_CAP = 150')
    print(cursor)
    for row in cursor:
        print("ID = ",row[0])
        print("VENUE_NAME = ",row[1])
        print("VENUE_CAP = ",row[2],"\n")
    conn.close()
    output = row[1]+str(row[2])
    return HttpResponse(output)
    
def event_exists(e_n):
	conn = sq.connect('realoffice.db')
    cursor=conn.execute("SELECT * FROM EVENT WHERE NAME = "+str(e_n))
    exists = False
    for row in cursor:
    	exists = True
    conn.close()
    return exists
    
def venue_exists(e_v):
	conn = sq.connect('realoffice.db')
    cursor=conn.execute("SELECT * FROM VENUE WHERE VENUE_NAME = "+str(e_v))
    exists = False
    for row in cursor:
    	exists = True
    conn.close()
    return exists
    
def venue_clash(e_v,e_s,e_e):

def cap_insuf(e_v,e_c):
	conn = sq.connect('realoffice.db')
    cursor=conn.execute("SELECT * FROM VENUE WHERE VENUE_NAME = "+str(e_v)+" AND VENUE_CAP < "+str(e_c))
    exists = False
    for row in cursor:
    	exists = True
    conn.close()
    return exists

def no_proj(e_v,e_p):
	if e_p==0:
		return False
	conn = sq.connect('realoffice.db')
    cursor=conn.execute("SELECT * FROM VENUE WHERE VENUE_NAME = "+str(e_v)+" AND VENUE_PROJ = 0")
    exists = False
    for row in cursor:
    	exists = True
    conn.close()
    return exists

def add(request):
    data=request.body
    print(data)
    data_rep=str(data).replace("b'","\"").replace("'","\"")
    l=data.split()
    e_name=l[0]
    e_n=str(e_name).replace("b'","\"").replace("'","\"")
    if(event_exists(e_n)):
    	
    e_venue=l[1]
    e_v=str(e_venue).replace("b'","\"").replace("'","\"")
    if(not venue_exists):
    	
    e_stime=l[2]
    e_s=str(e_stime).replace("b'","\"").replace("'","\"")
    e_etime=l[3]
    e_e=str(e_etime).replace("b'","\"").replace("'","\"")
    if(venue_clash(e_v,e_s,e_e)):
    
    e_capacity=l[4]
    e_c=str(e_capacity).replace("b'","\"").replace("'","\"")
    if(cap_insuf(e_v,e_c)):
    	
    e_proj=l[5]
    e_p=str(e_proj).replace("b'","\"").replace("'","\"")
    if(no_proj(e_v,e_p)):
    	
    conn1 = sq.connect('realoffice.db')
    conn1.execute("INSERT INTO EVENT(NAME,TYPE,HOST1,PARTICIPANTS,VENUE,STARTTIME,ENDTIME,PROJ) \
        VALUES("+str(e_n)+",'Meeting',1,'YOU',"+str(e_v)+","+str(e_s)+","+str(e_e)+","+str(e_p)")");
    conn1.commit()
    conn1.close()
    return HttpResponse(data_rep)

def find(request):
    data=request.body
    print(data)
    name=str(data).replace("b'","\"").replace("'","\"")
    if(not event_exists(name)):
    	
    conn2 = sq.connect('realoffice.db')
    cursor=conn2.execute('SELECT VENUE FROM EVENT WHERE NAME = '+str(name) + 'AND PROJ = 1')
    for row in cursor:
        print("VENUE = ",row[0])        
    conn2.close()
    output=row[0]
    print(output)
    return HttpResponse(output)
    
def delete(request):
	data=request.body
    print(data)
    name=str(data).replace("b'","\"").replace("'","\"")   
    if(not event_exists(name)):
    	
    conn3 = sq.connect('realoffice.db') 
    cursor = conn3.execute("DELETE FROM EVENT WHERE NAME = "+str(name))
    conn3.commit()
    conn3.close()
    return *******
