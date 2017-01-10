# _*_ coding:utf-8 _*_
from django.shortcuts import render

from .models import UserMessage

# Create your views here.


def getform(request):

    # all_messages =UserMessage.objects.filter(name='zhaoyingjie',address='上海')
    # for message in all_messages:
    #     print message.name

    #从数据库中读数据

    # user_message = UserMessage()
    # user_message.name = 'zhaoyingjie2'
    # user_message.message = 'helloworld2'
    # user_message.address = '上海'
    # user_message.email = '2@2.com'
    # user_message.object_id = 'helloworld3'
    # user_message.save()

    #把数据存入数据库


    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     email = request.POST.get('email','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'helloworld5'
    #     user_message.save()

    #数据从页面进行保存


    # all_messages =UserMessage.objects.filter(name='zhaoyingjie',address='天津')
    # all_messages.delete()
    # for message in all_messages:
    #     message.delete()
    #     print message.name

    #从数据库中删除数据


    message = None
    all_messages = UserMessage.objects.filter(name='xinghezhao')
    if all_messages:
        message = all_messages[0]

    #从数据库展示数据


    return render(request, 'message_form.html', {
        'my_message':message
    })