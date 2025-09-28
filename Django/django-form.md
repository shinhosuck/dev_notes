from django import forms
from articels.models import Article
from articles.forms import ArticelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

=============================
FORMS.FORM VS FORMS.MODELFORM
=============================

When using ModelForm:
    class ArticleForm (forms.ModelForm):
        class Meta:
            model = Article
            fields = ["title", "conent"]

    -have to declare model and fields.


When using Form:
    class ArticleForm (forms.Form):
        title = forms.CharField(max_length=100)
        conent = forms.TextField()

    -does not have to declare model and fields.

=========================================
FORM AUTHENTICATION "FORM" VS "MODELFORM"
=========================================
In views.py

Form create using forms.Form:
    -On "Form" it does not show "validation error", you have validate it using conditions.
    -Need to "cleaned_data" to retrieve data.

    def create_article_view(request):
        form = CreateArticleForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                author = request.user
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                new_article = Article.objects.create(author=author, title=title, content=content)
                return redirect("articles:detail", new_article.id)
        context = {"form": form}
        return render(request, "articles/create.html", form)


Form create using forms.ModelForm:
    -ModelForm automatically validates form-shows validatation error automatically.
    -Does not need "cleaned_data" on ModelForm.

    def create_article_view(request):
        form = CreateArticleForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                new_article = form.save(commit=False)
                new_article.author = request.user
                new_article.save()
                return redirect("articles:detail", new_article.id)
        context = {"form": form}
        return render(request, "articles/create.html", form)


=========================
USER AUTHENTICATION FORMS
=========================
-User login:
    -create form on html - it will be a POST from.
    -this is a logn way.
    def login(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("articles:home")
                else:
                    messages.error(request, "username or password did not match!")
                    return redirect("articles:home")
            else:
                messages.error(request, "username and password field can not be empty!")
                return redirect("articles:home")

    -more efficient way using built in form
    def login(request):
        form = AuthenticationForm(request, data=request.POST)
        if request.method == "POST":
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("articles:home")
        context = {"from": form}
        return render(request, "articles/login.html", context)


-User Registration Form:
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    else:
        context = {"form": form}
        return render(request, "users/register.html", context)
