from django.shortcuts import render
from .models import students
from django.db.models import Q
# Create your views here.
def home(request):

    context = {
        'students' : students.objects.all()
    }
    print(students)

    return render(request,'students.html',context)
def search(request):
    queryset = []
    Roll = []
    names = []
    nam = request.GET.get('search')
    ss = nam

    def num_there(nam):
        return any(i.isdigit() for i in nam)

    if(type(nam)==str):
        print("work str")
        names = students.objects.filter(name=nam)

        if(num_there(nam)):

            print("work")
            Roll = students.objects.filter(roll_no=int(nam))

    context = {'result': names,'result2':Roll, 'title': "search", 'name': ss}
    return render(request, 'search.html', context)
def racks(request):
    nam = request.GET.get('rack')

    # for r in rack:
    student = students.objects.filter(Q(rack1=nam) | Q(rack2=nam) | Q(rack3=nam) | Q(rack4=nam))
    context = {'result': student,'rck':nam}
    return render(request,'racks.html',context)
def rckres(request):
    return (request,'rck_res.html')