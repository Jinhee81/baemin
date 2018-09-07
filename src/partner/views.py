from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout
    )
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PartnerForm, MenuForm
from .models import Menu

# Create your views here.
def index(request):
    ctx = {}
    if request.method == "GET":
        partner_form = PartnerForm()
        ctx.update({ "form" : partner_form })
        print('index if get')
    elif request.method == "POST":
        partner_form = PartnerForm(request.POST)
        print('if post')
        if partner_form.is_valid():
            partner = partner_form.save(commit = False)
            partner.user = request.user
            partner.save()
            return redirect("/partner/")
            print('index if post valid')
        else:
            ctx.update({ "form" : partner_form })
            print('index if post unvalid')

    return render(request, "index.html", ctx)
    # print(444)

def login(request):
    ctx = {}

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect("/partner/")
            # Redirect to a success page.
        else:
            ctx.update({"error" : "사용자가 없습니다."})


    return render(request, "login.html", ctx)

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        # print(username, email, password)

    ctx = {}
    return render(request, "signup.html", ctx)

def logout(request):
    auth_logout(request)
    return redirect("/partner/")

def edit_info(request):
    ctx = {}
    # Article.objects.all()
    # partner = Partner.objects.get(user=request.user)
    # partner_form = PartnerForm(instance=request.user.partner)
    # ctx.update({ "form" : partner_form })

    if request.method == "GET":
        partner_form = PartnerForm(instance=request.user.partner)
        print('instance에불러옴')
        ctx.update({ "form" : partner_form })
        print('폼에저장')

    elif request.method == "POST":
        partner_form = PartnerForm(
            request.POST,
            instance=request.user.partner
        )
        if partner_form.is_valid():
            partner = partner_form.save(commit = False)
            partner.user = request.user
            partner.save()
            return redirect("/partner/")

        else:
            ctx.update({ "form" : partner_form })

    return render(request, "edit_info.html", ctx)

def menu(request):
    ctx = {}
    menu_list = Menu.objects.filter(partner = request.user.partner)
    ctx.update({"menu_list" : menu_list})
    return render(request, "menu_list.html", ctx)

def menu_add(request):
    ctx = {}

    if request.method == "GET":
        form = MenuForm() #form에 menuform을 활성화시키는거
        ctx.update({ 'form' : form }) #컨텍스트를 업데이트해준다.
    elif request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit = False)
            menu.partner = request.user.partner
            menu.save()
            return redirect('/partner/menu/')
        else:
            ctx.update({ 'form' : form })

        ctx.update({ 'form' : form })

    return render(request, "menu_add.html", ctx)
