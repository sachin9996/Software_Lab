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

def add_venue(request):
    data = request.body
    s=data.split()
    venue_name = s[0]
    v_n=str(venue_name).replace("b'","\"").replace("'","\"")
    venue_cap = s[1]
    v_c=str(venue_cap).replace("b'","\"").replace("'","\"")
    venue_proj = s[2]
    v_p=str(venue_proj).replace("b'","\"").replace("'","\"")
    venue_ac = s[3]
    v_a=str(venue_ac).replace("b'","\"").replace("'","\"")
    connav = sq.connect('realoffice.db')
    connav.execute("INSERT INTO VENUE(VENUE_NAME,VENUE_CAP,VENUE_PROJ,VENUE_AC) \ VALUES('"+str(v_n)+"','"+int(v_c)+"','"+int(v_p)+"','"+int(v_a)+"')");
    connav.commit()
    connav.close()

def delete_venue(request):
    data = request.body
    venue_name = s[0]
    v_n=str(venue_name).replace("b'","\"").replace("'","\"")
    conndv = sq.connect('realoffice.db')
    conndv.execute("DELETE FROM VENUE WHERE VENUE_NAME=?",('str(v_n)',));# \ VALUES('"+str(v_n)+"')");
    conndv.commit()
    conndv.close()

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
   # cursor = conn.execute('SELECT * FROM VENUE WHERE VENUE_NAME = ' + str(v) + ' AND VENUE_CAP = 150')
    print(cursor)
    for row in cursor:
        print("ID = ",row[0])
        print("VENUE_NAME = ",row[1])
        print("VENUE_CAP = ",row[2],"\n")
    conn.close()
    output = row[1]+str(row[2])
    return HttpResponse(output)

def delete_event(reuest):
    data=request.body
    l=data.split()
    e_name=l[0]
    e_n=str(e_name).replace("b'","\"").replace("'","\"")
    connde = sq.connect('realoffice.db')
    connde.execute("DELETE FROM EVENT WHERE NAME =?" ,('str(e_n)',));#\ VALUES("+str(e_n)+");
    connde.commit()
    connde.close()


def add(request):
    data=request.body
    print(data)
    data_rep=str(data).replace("b'","\"").replace("'","\"")
    l=data.split()
    e_name=l[0]
    e_n=str(e_name).replace("b'","\"").replace("'","\"")
    e_venue=l[1]
    e_v=str(e_venue).replace("b'","\"").replace("'","\"")
    e_stime=l[2]
    e_s=str(e_stime).replace("b'","\"").replace("'","\"")
    e_etime=l[3]
    e_e=str(e_etime).replace("b'","\"").replace("'","\"")
    e_capacity=l[4]
    e_c=str(e_capacity).replace("b'","\"").replace("'","\"")
    e_proj=l[5]
    e_p=str(e_proj).replace("b'","\"").replace("'","\"")
    conna = sq.connect('realoffice.db')
    conna.execute("INSERT INTO EVENT(NAME,TYPE,HOST,PARTICIPANTS,VENUE,STARTTIME,ENDTIME,PROJ) \
        VALUES('"+str(e_n)+"','Meeting',1,'YOU', '"+str(e_v)+"', '"+str(e_s)+"', '"+str(e_e)+"' ,1)");
    conna.commit()
    conna.close()
    return HttpResponse(data_rep)

def find(request):
    data=request.body
    print(data)
    name=str(data).replace("b'","\"").replace("'","\"")
    conn2 = sq.connect('realoffice.db')
    cursor=conn2.execute('SELECT VENUE FROM EVENT WHERE NAME = '+str(name) + 'AND PROJ = 1')
    for row in cursor:
        print("VENUE = ",row[0])
    conn2.close()
    output=row[0]
    print(output)
    return HttpResponse(output)
