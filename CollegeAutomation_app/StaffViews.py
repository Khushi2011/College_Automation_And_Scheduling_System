from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from CollegeAutomation_app.models import Subjects
from django.http import HttpResponse, JsonResponse
def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

def staff_take_attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id) 
    return render(request,"staff_template/staff_take_attendance.html",{"subjects":subjects})

@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    
    subject=Subjects.objects.get(id=subject_id)
    students=Students.objectc.filter(course_id=subject.course_id)
    student_data=serilizers.serializer("pythpon",students)
    list_data=[]

    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
        
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
