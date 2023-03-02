from rest_framework import serializers
from .models import (
    Vocabulary, Entries,
    Definitions, Examples,
    Synonyms, Tables
)

class TableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tables
        fields = ['word', 'tableName']

class VocabularySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vocabulary
        fields = ['word']

class EntrySerializer(serializers.ModelSerializer):

    def to_representation(self, entry):
        word = VocabularySerializer(entry.word).data

        return {
            'type': entry.lexicalCategory,
            'word': word
        }

class DefinitionSerializer(serializers.ModelSerializer):

    def to_representation(self, definition):
        entry = EntrySerializer(definition.entry).data
        word = VocabularySerializer(definition.word).data

        return {
            'definition': definition,
            'entry': entry,
            'word': word
        }

class ExampleSerializer(serializers.ModelSerializer):

    def to_representation(self, example):
        entry = EntrySerializer(example.entry).data
        word = VocabularySerializer(example.word).data

        return {
            'example': example,
            'entry': entry,
            'word': word
        }

class SynonymSerializer(serializers.ModelSerializer):

    def to_representation(self, synonym):
        entry = EntrySerializer(synonym.entry).data
        word = VocabularySerializer(synonym.word).data

        return {
            'synonym': synonym,
            'entry': entry,
            'word': word
        }