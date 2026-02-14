from django.http import HttpResponse
from django.shortcuts import render,redirect
from todo.models import todolist   

def save(request):
    s2 = todolist.objects.all()  

    if request.method == 'POST':
        listid = request.POST['listid']
        content = request.POST['content']

        s1 = todolist(listid=listid,content=content)
        s1.save()

    dict1 = {
        'data': s2
    }

    return render(request, "index.html", dict1)

def delete(request):
    listid = request.GET.get('listid')
    todolist.objects.filter(listid=listid).delete()
    return redirect('abc/')


# def delete(request):
   
#     listid=request.GET['listid']
#     s2=todolist.objects.get(listid=listid)
#     s2.delete()
#     s2=todolist.objects.all()
#     dict2={
#         'data':s2
#     }
#     return render(request,"index.html",dict2)

# def update1(request):
#     listid = request.GET['listid']
#     content = request.GET['content']
#     dict1={
#         'listid':listid,
#         'content':content
#     }


#     return render(request,'edit.html',dict1)

# def update2(request):
#     listid = request.POST['listid']
#     content = request.POST['content']

#     s2 = todolist.objects.filter(listid=listid)
#     s2.content=content
   
#     s3=todolist.object.all()

#     dict1={
#         'data':s3
#     }

#     return render(request,'edit.html',dict1)



def update1(request):
    listid = request.GET['listid']
    content = request.GET['content']

    return render(request, 'edit.html', {
        'listid': listid,
        'content': content
    })


def update2(request):
    listid = request.POST['listid']
    content = request.POST['content']

    # update ALL records with same listid (simple logic)
    todolist.objects.filter(listid=listid).update(content=content)

    s3 = todolist.objects.all()

    return render(request, 'index.html', {'data': s3})


