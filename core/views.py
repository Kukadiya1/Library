from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import signUp_data, addBook, confirm_book,return_book,donate_book


# Sign up function
def signUp(request):
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['UserEmail']
        p = request.POST['UserPassword']
        model = signUp_data(first_name=f, last_name=l, email=e, password=p)
        # print(f,l,e,p)
        model.save()
        return HttpResponseRedirect('login/')
    else:
        return render(request, 'Signup.html')


def login(request):
    if request.method == 'POST':
        # print(type(signUp_data.objects.get(email=request.POST['userEmail'])))
        try:
            obj = signUp_data.objects.get(email=request.POST['userEmail'])
            # print(obj.email == request.POST['userEmail'])
            # print(obj.password == request.POST['userPassword'])
            if request.POST['userEmail'] == obj.email and request.POST['userPassword'] == obj.password:
                return HttpResponseRedirect('/home/')
            else:
                return render(request,'loginerror.html')
        except:
            return render(request,'loginerror.html')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def landBook(request):
    data = addBook.objects.all()
    # print(data)
    return render(request, 'landBook.html', {'var': data})


def confirmation(request):
    if request.method == "POST":
        try:
            book = request.POST['book']
            fname = request.POST['fname']
            lname = request.POST['lname']
            user_email = request.POST['email']
            user_password = request.POST['password']
            info = [fname, lname, book, user_email, user_password]
            # print(info)
            check_user = signUp_data.objects.get(pk=user_email)
            # print(check_user.first_name) 
            check_book = addBook.objects.get(pk=book)
            actual = [check_user.first_name,check_user.last_name,check_book.book_name,check_user.email,check_user.  password]
            # print(actual)
            # print(check_book)
            if info == actual:
                book_confirm = confirm_book(fname=request.POST['fname'],lname=request.POST['lname'],book=request.POST['book'],email=user_email,password=user_password)
                book_confirm.save()
                # print('Save successfull...')
                check_book.delete()
                # print('Delete successfull...')
                return render(request,'processdone.html',{'name':'taking','message':'take care of the book and return it after reading the book.'})
            else:
                return render(request,'reject.html',{'var':'your request rejected please check the user information and book name.'})
        except:
            return render(request,'reject.html',{'var':'your request rejected please check the user information and book name.'})
        # else:
        #     return HttpResponse('Thows error...')
    else:
        return render(request, 'confirmation.html')


def returnbook(request):
    if request.method == "POST":
        try:
            land_book = request.POST['book']
            f_name = request.POST['fname']
            l_name = request.POST['lname']
            user_email = request.POST['email']
            user_password = request.POST['password']
            # print('information data  --> ',f_name, l_name, land_book, user_email, user_password)
            info = [f_name, l_name, land_book, user_email, user_password]
            # print('Done...')
            obj = confirm_book.objects.get(pk=land_book)
            # obj = confirm_book(fname=f_name,lname=l_name,book=land_book,email=user_email,password=user_password)
            # print('\nObject save....\n')
            actual = [obj.fname,obj.lname,obj.book,obj.email,obj.password]
            # print('Information is',info)
            # print('Our actual data is',actual)
            if info == actual:
                # print('Enter in if')
                data_save = return_book(book=land_book,email=user_email,password=user_password)
                # print(data_save)
                # print('Data save succssesfully...')
                data_save.save()
                # print(obj)
                obj.delete()           
                # print('Data delete succssesfully...')
                return render(request,'processdone.html',{'name':'returning','message':'Visit again.'})
            else:
                return render(request,'reject.html',{'var':'your request rejected please check the user information and book name.'})
        except:
            return render(request,'reject.html',{'var':'your request rejected please check the user information and book name.'})
    else:
        return render(request, 'returnbook.html')

def donate_view(request):
    if request.method == 'POST':
        try:
            book_name = request.POST['book']
            author_name = request.POST['author']
            book_language = request.POST['language']
            book_desc = request.POST['desc']
            user_name = request.POST['email']
            user_password = request.POST['password']
            user_check = signUp_data.objects.get(pk=user_name)
            print('\n',user_check.email,user_check.password,'\n')
            obj = donate_book(book=book_name,author=author_name,language=book_language,disc=book_desc,email=user_name,password=user_password)
            obj.save()
            print('Data save...')
            return render(request,'processdone.html',{'name':'donating','message':'book donating process is done. thanks for donating the book to our library.'})
        except:
            return render(request,'reject.html',{'var':'Please check user information.'})

    else:    
        return render(request,'donatebook.html')
