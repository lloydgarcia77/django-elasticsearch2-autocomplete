from searchengine.models import Comments, Todo
from haystack import indexes

class CommentsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    email = indexes.EdgeNgramField(model_attr='email')
    name = indexes.CharField(model_attr='name')
    postId = indexes.CharField(model_attr='postId')
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        return Comments
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class TodoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    user_id = indexes.CharField(model_attr='user_id')
    tid = indexes.CharField(model_attr='tid')
    title = indexes.CharField(model_attr='title')
    completed = indexes.BooleanField(model_attr='completed') 

    def get_model(self):
        return Todo
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
