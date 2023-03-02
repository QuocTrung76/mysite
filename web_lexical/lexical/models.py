from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.word

class Entries(models.Model):
    lexicalCategory = models.CharField(max_length=30, verbose_name="Category")
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

    def __str__(self):
        return self.lexicalCategory

class Definitions(models.Model):
    definition = models.CharField(max_length=255, blank=True, null=True)
    entry = models.ForeignKey(Entries, on_delete=models.CASCADE, verbose_name="Category")
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

    def __str__(self):
        firstWord = self.definition.split()
        return firstWord[0]

class Examples(models.Model):
    example = models.CharField(max_length=255, blank=True, null=True)
    entry = models.ForeignKey(Entries, on_delete=models.CASCADE, null=True, verbose_name="Category")
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

    def __str__(self):
        firstWord = self.example.split()
        return firstWord[0]

class Synonyms(models.Model):
    synonym = models.CharField(max_length=255, blank=True, null=True)
    entry = models.ForeignKey(Entries, on_delete=models.CASCADE, null=True, verbose_name="Category")
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

    def __str__(self):
        return self.synonym

class Tables(models.Model):
    tableName = models.CharField(max_length=255, verbose_name="Own Dictionary")
    word = models.ManyToManyField(Vocabulary)

    def __str__(self):
        return self.tableName