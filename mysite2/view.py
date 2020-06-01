from django.shortcuts import render, redirect
import pymysql


def show_student(request):
    db = pymysql.connect("localhost", "testuser", "PlayStation5", "dbsclab2020", port=3306,
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    ctx = {}
    if request.POST:
        name = request.POST['name']
        sql = "select * from student where name like %s"
        cursor.execute(sql, ['%' + name + '%'])
    else:
        sql = "select * from student"
        cursor.execute(sql)
    data = cursor.fetchall()
    context = {}
    context['students'] = data
    return render(request, 'student.html', context)


def addStudent(request):
    db = pymysql.connect("localhost", "testuser", "PlayStation5", "dbsclab2020", port=3306,
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    ctx = {}
    if request.POST:
        ID = request.POST['ID']
        name = request.POST['name']
        dept_name = request.POST['dept_name']
        tot_cred = request.POST['tot_cred']
        sql = "insert into student values (%s,%s,%s,%s)"
        cursor.execute(sql, [ID, name, dept_name, tot_cred])
        db.commit()
        sql2 = "select * from student where ID=%s"
        cursor.execute(sql2, ID)
        data = cursor.fetchall()
        ctx['students'] = data

    return render(request, 'addStudent.html', ctx)


def modifyStudent(request, id):
    return render(request, 'modifyStudent.html')


def deleteStudent(request, id):
    return redirect('/search-student')


def show_instructor(request):
    db = pymysql.connect("localhost", "testuser", "PlayStation5", "dbsclab2020", port=3306,
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    ctx = {}
    if request.POST:
        name = request.POST['name']
        sql = "select * from instructor where name like %s"
        cursor.execute(sql, ['%' + name + '%'])
    else:
        sql = "select * from instructor"
        cursor.execute(sql)
    data = cursor.fetchall()
    context = {}
    context['instructors'] = data
    return render(request, 'instructors.html', context)


def addInstructor(request):
    db = pymysql.connect("localhost", "testuser", "PlayStation5", "dbsclab2020", port=3306,
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    ctx = {}
    if request.POST:
        ID = request.POST['ID']
        name = request.POST['name']
        dept_name = request.POST['dept_name']
        salary = request.POST['salary']
        sql = "insert into instructor values (%s,%s,%s,%s)"
        cursor.execute(sql, [ID, name, dept_name, salary])
        db.commit()
        sql2 = "select * from instructor where ID=%s"
        cursor.execute(sql2, ID)
        data = cursor.fetchall()
        ctx['instructors'] = data

    return render(request, 'addInstructor.html', ctx)


def modifyInstructor(request, id):
    return render(request, 'modifyInstructor.html')


def deleteInstructor(request, id):
    return redirect('/search-instructor')
