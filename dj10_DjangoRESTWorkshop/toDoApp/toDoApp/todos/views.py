from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from toDoApp.todos.models import Todo, Category
from toDoApp.todos.serializers import TodoSerializer, CategorySerializer, TodoReadSerializer


class TodoListCreateApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()

        category = self.request.query_params.get('category')
        is_done = self.request.query_params.get('category')

        if category:
            queryset = queryset.filter(category__name=category)
        if is_done:
            queryset = queryset.filter(state=is_done.lower() == 'true')

        return queryset


class TodoDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoReadSerializer


class CategoriesListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
