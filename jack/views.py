from django.shortcuts import render
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from diets.models import *
from .jack import *
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import APIView



# Create your views here.
class JackQuestionViewSet(ModelViewSet):
    queryset = JackQuestion.objects.all()
    serializer_class = JackQuestionSerializer
    
    def create(self, request, *args, **kwargs):
        conversation_value = request.data.get('conversation')
        print(conversation_value)
        conversations = JackQuestion.objects.filter(conversation=conversation_value).all()
        created_by = JackConversation.objects.filter(id=conversation_value)
        created_by = created_by[0].made_by.user.id
        print(created_by)
        previous_messages = []
        if len(conversations) > 50: 
            conversations = conversations.reverse()[:30]
        if conversations:
            for conversation in conversations:
                previous_message =({
                'question': conversation.question,
                'response': conversation.response
                })
                previous_messages.append(previous_message)
        
        mutable_data = request.data.copy()
        ingredients = Ingredients.objects.filter(created_by=created_by)
        mutable_data['response'] = llamarFuncion(question=request.data.get('question'), previous_messages=previous_messages, previous_foods=ingredients)
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=200)
    
    def update(self, request, *args, **kwargs):
        print('Hola (update)')
        print(request.data)
        return super().update(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        print('chupame los huevos(list)')
        print(request.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('ola(retrieve)')
        return super().retrieve(request, *args, **kwargs)
    
class JackConversationViewSet(ModelViewSet):
    queryset = JackConversation.objects.all()
    serializer_class = JackConversationSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print('Hola (update)')
        print(request.data)
        return super().update(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        print('chupame los huevos(list)')
        print(request.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('ola(retrieve)')
        return super().retrieve(request, *args, **kwargs)
    
class ConversationMessages(APIView):
    def get(self, request, conversation_id):
        try:
            messages = JackQuestion.objects.filter(conversation_id = conversation_id)
            serializer = JackQuestionSerializer(messages, many=True)
            print({"message": "Conversaciones conseguidas de manera correcta", "data": serializer.data})
            return JsonResponse({"message": "Conversaciones conseguidas de manera correcta", "data": serializer.data})
        except Exception as e:
             print(e)
             return JsonResponse({"message": "Error", "data": e})