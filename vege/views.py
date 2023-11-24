from django.shortcuts import render,redirect
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User 

# Create your views here.
def recipes(request):
    if request.method=="POST":
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
    recipe=Recipe.objects.get(id=id)
    recipe.delete()
    messages.success(request,"Recipe deleted successfully")
    return redirect('recipes')


def login_user(request):
    return render(request,'vege/login.html')

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
            messages.error(request,"Email already registered")
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
            messages.success(request,"User Registered Successfully")
            return redirect("/recipes")


    
    return render(request,'vege/register.html')