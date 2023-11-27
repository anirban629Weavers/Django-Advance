from django.shortcuts import render,redirect
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def recipes(request):
    if request.method=="POST":
        if not request.user.is_authenticated:
            messages.warning(request,"Please Login First")
            return redirect("login")
            
        
        data=request.POST
        
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        messages.success(request,"Recipe added successfully")
        return redirect('recipes')

    all_recipes=Recipe.objects.all()
    
    if(request.GET.get('search')):
         all_recipes=all_recipes.filter(recipe_name__icontains=request.GET.get('search'))
    
    return render(request, 'vege/recipes.html',context={'recipes':all_recipes})

def update_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    if request.method=="POST":
        if not request.user.is_authenticated:
          messages.warning(request,"Please Login First")
          return redirect("login")
            
        data=request.POST
        
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        
        if recipe_name:recipe.recipe_name=recipe_name 
        if recipe_description:recipe.recipe_description=recipe_description
        if recipe_image:recipe.recipe_image=recipe_image
    
        recipe.save()
        
        messages.success(request,"Recipe updated successfully")
        return redirect('recipes')
    
    context={'recipe':recipe}
    return render(request,'vege/update.html',context=context)

def delete_recipe(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login First")
        return redirect("login")

    recipe=Recipe.objects.get(id=id)
    recipe.delete()
    messages.success(request,"Recipe deleted successfully")
    return redirect('recipes')


def login_user(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")            
        print(email,password)
        
        if not User.objects.filter(email=email).exists():
            messages.warning(request,"User does not exist")
            return redirect('login')
        
        # user=authenticate(request,username="a@a.com",password=password)
        # ! Make the email and username same 
        user=authenticate(request,username=email,password=password)
        
        if user is None:
            messages.warning(request,"Invalid Credentials")
            return redirect('login')
        else:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('recipes')
                            
    if request.user.is_authenticated:
        return redirect("recipes")
    else:
        return render(request,'vege/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You're Logged out")
    return redirect('recipes')

def register_user(request):
    if request.method=="POST":
        data=request.POST
        
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        
        user=User.objects.filter(email=email)
        
        if user.exists():    
            messages.warning(request,"Email already registered")
            return render(request,'vege/register.html')
        else:
            user=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request,"User Registered Successfully")
            return redirect("/recipes")


    if request.user.is_authenticated:
        return redirect("recipes")
    else:
        return render(request,'vege/register.html')
