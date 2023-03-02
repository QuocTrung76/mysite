from django.shortcuts import render, redirect
from .models import (
    Vocabulary, Entries,
    Definitions, Examples,
    Synonyms, Tables
)
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import requests
import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    VocabularySerializer, EntrySerializer,
    DefinitionSerializer, ExampleSerializer,
    SynonymSerializer, TableSerializer
)
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

app_id = "7015a689"
app_key = "92aecbd0408cd416c129dca623726592"

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        print("heelo", username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return JsonResponse({"valid":True}, status = 200)
        else:
            return JsonResponse({"valid":False}, status = 200)
    return render(request, 'lexical/index.html')


class GetVocalMeaning(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    template_name = 'lexical/search.html'
    

    def list(self, request):
        word = request.GET.get('word', None)
        word_from_list = request.GET.get('wordFromList', None)
        command = request.GET.get('command', None)
        tableName = request.GET.get('tableName', None)
        tables = Tables.objects.all()
        print(word, word_from_list)
        if not word:
            word = word_from_list
        if word:
            word = word.lower()
            checkWord = Vocabulary.objects.filter(word=word).exists()
            if checkWord:
                if command == 'Add':
                    my_table = Tables.objects.filter(tableName=tableName)
                    wordList = []
                    for tableWord in my_table[0].word.all():
                        wordList.append(tableWord.word)
                    wordList.append(word)
                    words = Vocabulary.objects.filter(word__in=wordList)
                    my_table[0].word.set(words)
                    my_table[0].save()
                wordDict = {}
                my_word = Vocabulary.objects.filter(word=word)[0]
                my_lexical = Entries.objects.filter(word=my_word.id)
                lexicalCategory = []
                for lexical in my_lexical:
                    lexicalCategory.append(lexical.lexicalCategory)
                    wordDict[lexical.lexicalCategory] = {}
                
                for lexicalId in my_lexical:
                    definitions = []
                    my_definitions = Definitions.objects.filter(entry=lexicalId.id, word=my_word.id)
                    for definition in my_definitions:
                        definitions.append(definition.definition)
                    if definitions:
                        wordDict[lexicalId.lexicalCategory]['definitions'] = definitions
                    
                    examples = []
                    my_examples = Examples.objects.filter(entry=lexicalId.id, word=my_word.id)
                    for example in my_examples:
                        examples.append(example.example)
                    if examples:
                        wordDict[lexicalId.lexicalCategory]['examples'] = examples
                    
                    synonyms = []
                    my_synonyms = Synonyms.objects.filter(entry=lexicalId.id, word=my_word.id)
                    for synonym in my_synonyms:
                        synonyms.append(synonym.synonym)
                    if synonyms:
                        wordDict[lexicalId.lexicalCategory]['synonyms'] = synonyms
                newWordList = Tables.objects.filter(tableName=tableName)[0].word.all()
                returnNewWordList = []
                for newWord in newWordList:
                    returnNewWordList.append(newWord.word)
                returnNewWordList.sort()
                return JsonResponse(
                    {
                        'valid': True,
                        'wordDict': wordDict,
                        'lexicalCategory': lexicalCategory,
                        'word': my_word.word,
                        'tableName': tableName,
                        'wordList': returnNewWordList
                    },
                    status = 200
                )
            else:
                url = "https://od-api.oxforddictionaries.com/api/v2/entries/en-us" + "/" + str(word).lower()
                r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
                
            
                if 'results' in r.json():
                    new_word = Vocabulary.objects.create(word=word)
                    new_word.save()
                    newWord = Vocabulary.objects.filter(word=word)
                    if command == 'Add':
                        my_table = Tables.objects.filter(tableName=tableName)
                        wordList = []
                        for tableWord in my_table[0].word.all():
                            wordList.append(tableWord.word)
                        wordList.append(word)
                        words = Vocabulary.objects.filter(word__in=wordList)
                        my_table[0].word.set(words)
                        my_table[0].save()
                        print(words)
                    wordDict = {}
                    lexicalCategory = []
                    for category in r.json()['results'][0]['lexicalEntries']:
                        if 'senses' in category['entries'][0]:
                            typeOfWord = category['lexicalCategory']['text']
                            lexicalCategory.append(typeOfWord)
                            new_type = Entries.objects.create(lexicalCategory=typeOfWord, word=newWord[0])
                            new_type.save()
                            newType = Entries.objects.filter(lexicalCategory=typeOfWord, word=newWord[0])
                            wordDict[typeOfWord] = {}
                            for sense in category['entries'][0]['senses']:
                                if 'definitions' in sense:
                                    if 'definitions' not in wordDict[typeOfWord]:
                                        wordDict[typeOfWord]['definitions'] = []
                                    for definition in sense['definitions']:
                                        wordDict[typeOfWord]['definitions'].append(definition)
                                        newDefine = Definitions.objects.create(definition=definition, entry=newType[0], word=newWord[0])
                                        newDefine.save()
                                if 'examples' in sense:
                                    if 'examples' not in wordDict[typeOfWord]:
                                        wordDict[typeOfWord]['examples'] = []
                                    for example in sense['examples']:
                                        wordDict[typeOfWord]['examples'].append(example['text'])
                                        newExample = Examples.objects.create(example=example['text'], entry=newType[0], word=newWord[0])
                                        newExample.save()
                                if 'synonyms' in sense:
                                    if 'synonyms' not in wordDict[typeOfWord]:
                                        wordDict[typeOfWord]['synonyms'] = []
                                    for synonym in sense['synonyms']:
                                        wordDict[typeOfWord]['synonyms'].append(synonym['text'])
                                        newSynonym = Synonyms.objects.create(synonym=synonym['text'], entry=newType[0], word=newWord[0])
                                        newSynonym.save()
                    newWordList = Tables.objects.filter(tableName=tableName)[0].word.all()
                    returnNewWordList = []
                    for newWord in newWordList:
                        returnNewWordList.append(newWord.word)
                    returnNewWordList.sort()
                    return JsonResponse(
                        {
                            'valid': True,
                            'wordDict': wordDict,
                            'lexicalCategory': lexicalCategory,
                            'word': r.json()['id'],
                            'tableName': tableName,
                            'wordList': returnNewWordList
                        }, status = 200
                    )
                return JsonResponse({'valid': False, 'error': 'check spelling'}, status = 200)
        return render(request, self.template_name, {'tables': tables, 'user': str(request.user)})

class GetVocalTable(generics.ListCreateAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    template_name = 'lexical/lexical.html'

    def list(self, request):
        # queryset = self.get_queryset()
        # serializer = VocabularySerializer(queryset, many=True)

        # list_choice = Vocabulary.typeOfWord.field.choices
        # list_choice_agg = []
        # for choice in list_choice:
        #     list_choice_agg.append(choice[0])

        # content = {
        #     'datas': serializer.data,
        #     'wordType': list_choice_agg
        # }
        return render(request, self.template_name)