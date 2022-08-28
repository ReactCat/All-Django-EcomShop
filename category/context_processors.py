from .models import Category

def menulinks(request):
    catlinks = Category.objects.all()
    return dict(catlinks = catlinks)
