# HNG-CRUD
A simple REST API capable of CRUD
classDiagram
    class Person {
        - id: int
        - name: string
    }

    class PersonSerializer {
        <<Serializer>>
        - class: Person
    }

    class PersonListCreateView {
        <<APIView>>
        - queryset: Person
        - serializer_class: PersonSerializer
        + post(request): Response
        + get(request): Response
    }

    class PersonRetrieveUpdateDeleteView {
        <<APIView>>
        - queryset: Person
        - serializer_class: PersonSerializer
        + get(request): Response
        + put(request): Response
        + patch(request): Response
        + delete(request): Response
    }
    
    PersonListCreateView --|> Person
    PersonRetrieveUpdateDeleteView --|> Person
    PersonSerializer --|> Person
    PersonSerializer --|> PersonListCreateView
    PersonSerializer --|> PersonRetrieveUpdateDeleteView
