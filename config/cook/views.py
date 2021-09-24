from django.shortcuts import get_object_or_404, render, redirect
from .models import * 
# # Create your views here.

# 랜딩페이지 
def index(request) : 
    return render(request, 'index.html')

# # Read 마이 페이지에서 레시피들 보여지는 화면 
def home(request) :
    recipe = Recipe.objects.all()
    context = {
        'recipe' : recipe, 
    }
    return render(request, 'home.html', context)

# Detail 각 레시피 화면 
def detail(request, id) : 
    recipe = get_object_or_404(Recipe, pk = id)
    content = Content.objects.filter(title = recipe)
    context ={
        'recipe' : recipe, 
        'content' : content,
    }
    return render(request, 'detail.html', context)

# Create 레시피 만들기 화면 
def new(request) : 
    return render(request, 'create.html')

def create(request) : 
    recipe = Recipe() 
    content = Content()
    recipe.title = request.POST.get('title')
    recipe.photo = request.FILES.get('photo') 
    recipe.save()
    
    content.title = recipe
    content.ingredients = request.POST.get('ingredients')
    content.ingredients_count = request.POST.get('ingredients_count')
    content.method = request.POST.get('method') 
    content.save() 
    
    return redirect('/detail/'+str(recipe.id))


# 로그인버전
# def create(request) : 
#     user_pk = request.session.get('user') 
#     if not user_pk : 
#         return redirect('/') # 로그인안하면 랜딩페이지 index.html로 가게 한다. 
#     elif user_pk : 
#         if request.method == 'POST' : 
#             recipe = Recipe() 
#             content = Content()
#             recipe.title = request.POST.get('title')
#             recipe.photo = request.FILES.get('photo') 
#             recipe.save()

#             content.title = recipe
#             content.ingredients = request.POST.get('ingredients')
#             content.ingredients_count = request.POST.get('ingredients_count')
#             content.method = request.POST.get('method') 
#             content.save() 
#             return redirect('/detail/'+str(recipe.id))
            
#     context ={
#         'user_pk' : user_pk, 
#     }
#     return render(request, 'create.html', context)


# def new(request) : 
#     return render(request, 'create.html')

# def create(request) : 
    
#     recipe = Recipe() 
#     if request.method =='POST' : 
#         content = Content()

    
# 재료 취합하는 함수도 필요할 듯 


# # Delete 없애기 (걍 함수만 쓰면 돼서 금방할듯)