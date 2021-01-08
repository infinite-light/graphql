import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):

    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    all_categories = graphene.List(CategoryType, id=graphene.Int())
    all_quizzes = graphene.List(QuizzesType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)
    def resolve_all_categories(root, info, id):
        return Category.objects.filter(id=id)
    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.filter(id=id)

schema = graphene.Schema(query=Query)


