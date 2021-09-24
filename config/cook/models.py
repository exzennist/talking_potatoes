from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Recipe(models.Model) : 
    title = models.CharField(max_length=200, verbose_name='제목')
    photo = models.ImageField(upload_to = 'recipe', verbose_name = '사진 photo')
    ingredients_list = models.CharField(max_length=200, verbose_name = '재료 리스트 저장 ingredients_list')

    def __str__(self) : 
        return self.title

#    def summary(self):
#        return self.inredients_list[:100] # 재료 리스트를 100자만 보여지게 한다. 

# ingredients_list 안에 Content 가 들어가야하는데? 시발.. 잦댔당 ㅎㅎ

class Content(models.Model) : 
    title = models.ForeignKey(Recipe, on_delete=CASCADE, null = True, verbose_name='요리 제목 foreignkey title') # id 같은 역할
    ingredients = models.CharField(max_length=200, blank=True, null=True, verbose_name='재료 이름 ingredients')
    ingredients_count = models.CharField(max_length=200, blank = True, null = True, verbose_name= '재료개수 ingredients_count')
    method = models.TextField(verbose_name='조리 방법 method')

