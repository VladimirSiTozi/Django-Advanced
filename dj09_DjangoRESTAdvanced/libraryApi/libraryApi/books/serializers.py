from rest_framework import serializers

from libraryApi.books.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers. ModelSerializer):
    author = AuthorSerializer(many=True)  # many=True - for m2m, else empty

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('author')
        authors_names = [a['name'] for a in authors]  # [{"name": "Vlado"}, {"name": "Nora"}] -> ["Vlado", "Dido"]

        book = Book.objects.create(**validated_data)
        """
        {
          "author": [
            {
              "name": "Nora"
            }
          ],
          "title": "New Book Title 1",
          "pages": 445,
          "description": "Cool Book!"
        }
        
        -> # { "title": "New Book Title 1", "pages": 445, "description": "Cool Book!"}
        """

        existing_authors = Author.objects.filter(name__in=authors_names)
        existing_authors_name = set(existing_authors.values_list('name', flat=True))

        new_authors_names = set(authors_names) - existing_authors_name

        new_authors = [Author(name=a_name) for a_name in authors_names]
        created_authors = Author.objects.bulk_create(new_authors)

        all_authors = list(existing_authors) + list(created_authors)
        # [<AuthorObj: Vlado>, <AuthorObj: Nora>]

        book.author.set(all_authors)

        return book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

