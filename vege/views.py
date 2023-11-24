from django.shortcuts import render,redirect
from .models import Recipe
from django.contrib import messages

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