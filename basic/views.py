from django.shortcuts import render,HttpResponseRedirect
from basic.models import student,marks

# Create your views here.
def index(request):

    if request.method=='POST':
        id=request.POST.get('id')
        course=request.POST.get('course')
        fname=request.POST.get('Fname')
        mname=request.POST.get('Mname')
        lname=request.POST.get('Lname')
        Student=student(stdid=id,Fname=fname,Lname=lname,Mname=mname,course=course)
        Student.save()
    stud = student.objects.all()
    return render(request,'index.html',{'stud':stud})
def display(request):
    return render(request,'data.html')

def delete(request,id):
    if request.method=="POST":
        pi=student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update(request,id):
    st=student.objects.get(pk=id)
    fname=st.Fname
    mname=st.Mname
    lname=st.Lname
    course=st.course
    return render(request,'update.html',{'id':id,'fname':fname,'mname':mname,'lname':lname,'course':course})

def updatedata(request,id):
    first = request.POST['Fname']
    middle = request.POST['Mname']
    last = request.POST['Lname']
    course = request.POST['course']
    member = student.objects.get(id=id)
    member.Fname = first
    member.Mname = middle
    member.Lname = last
    member.course = course
    member.save()
    return HttpResponseRedirect('/')
def addmarks(request,id):
    st = student.objects.get(stdid=id)
    fname = st.Fname
    mname = st.Mname
    lname = st.Lname
    if marks.objects.filter(stdid=st).exists():
        member = marks.objects.get(stdid=st)

        c = member.cmark
        cpp = member.cppmark
        p = member.pymark
        return render(request, 'addmarks.html', {'stdid': id, 'fname': fname, 'mname': mname, 'lname': lname,'c':c,'cpp':cpp,'py':p})
    else:
        return render(request,'addmarks.html',{'stdid':id,'fname':fname,'mname':mname,'lname':lname})
def insertmarks(request,id):
    c = request.POST['cMark']
    cpp = request.POST['cppMarks']
    py = request.POST['pyMarks']
    st = student.objects.get(stdid=id)
    fname = st.Fname
    if marks.objects.filter(stdid=st).exists():

        member = marks.objects.get(stdid=st)
        member.cmark = c
        member.cppmark = cpp
        member.Lname = py
        member.pymark = id
        member.save()
    else:

        c = request.POST.get('cMark')
        cpp = request.POST.get('cppMarks')
        py = request.POST.get('pyMarks')

        mark = marks(stdid=st,cmark=c, cppmark=cpp, pymark=py)
        mark.save()
    return HttpResponseRedirect('/')
