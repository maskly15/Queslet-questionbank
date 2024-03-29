from django.shortcuts import render,redirect
from django.http import HttpRequest
from ..models.models import Mcq,Subject,SubjectAccess
from django.core.paginator import Paginator
from django import template
from django.template.defaulttags import register


# Create your views here.



# get list of subjects 

def get_context(request):

    # text =" manh dep trai"
    # link = 'http://127.0.0.1:8000/model/encode?mcq=' + text
    # print(link)

    # basic = HTTPBasicAuth('manhpd15', 'Test1508')
    # response = requests.get(link,auth=basic)
    # print(response.json() )

    isManager = False

    User =  request.user
    print('current User',User.username)
    isManager = True if  User.groups.filter(name='manager').exists() else False

    result = Mcq.objects.all()

    if not isManager:
        subjects_access = SubjectAccess.objects.filter(teacher=User.username)
        subjects = [sub.subject for sub in subjects_access]
        print(subjects)
        if len(subjects) == 0:
            context = {"subjects":subjects,"isManager" :isManager}
            return context
        subjects_name = [sub.subject.subject for sub in subjects_access][0]
    else:
        subjects = Subject.objects.all()
    subjects_name = [sub.subject for sub in subjects][0]

    try:
        subject_session = request.session['subjects_selected']
        subjects_name = subject_session if subject_session is not None else subjects_name
    except:
        print("not have any subject selected in session")

    subjects_access_name = [sub.subject for sub in subjects]
    print(subjects_access_name)
    subjects_name_select =  request.GET.get("subject",subjects_name)

    if subjects_name_select in subjects_access_name:
        subjects_name = subjects_name_select

    # store in session 
    request.session['subjects_selected'] = subjects_name
    result = result.filter(subject=subjects_name)
    print(subjects)
    have_img = result.filter(contain_img =True)
    page_num = 1
    context ={"lst_mcqs":result,
      "total":len(result),
      "num_img":len(have_img),
      "num_subject":len(subjects),
      "page":page_num,
      "isManager" :isManager,
      "subjects":subjects,
      "subjects_selected":subjects_name
      }
    return context

    




def home(request):
    #   if not request.user.is_authenticated:
    #      return redirect('login')
      
      if request.method == "GET":
            context = get_context(request=request)
            return render(request, 'questionbank.html',context)
      else:
          return redirect('login')
      
def isManger(User):
    return User.groups.filter(name='manager').exists() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 