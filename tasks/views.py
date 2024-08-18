from django.views.generic import CreateView,ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Category, Task

# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = "home.html"
    context_object_name = 'categories'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] =  Task.objects.all()
        return context
    
class TaskListView(ListView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'categories_with_tasks'

    def get_queryset(self):
        categories = Category.objects.all()
        categories_with_tasks = {}
        for category in categories:
            tasks = Task.objects.filter(category=category)
            if tasks.exists():
                categories_with_tasks[category] = tasks
        return categories_with_tasks

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['completed']
    template_name = "task_list.html"

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.complited = not task.complited
        task.save()
        return JsonResponse({'success': True})
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = "category_create.html"
    fields = ['name', 'description']
    success_url = reverse_lazy('home') 

class TaskCreateView(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = ['title', 'category', 'author']

    


