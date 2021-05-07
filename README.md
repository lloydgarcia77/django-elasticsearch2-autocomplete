# django-elasticsearch2-autocomplete
Advance search engine

Documentaion:
    https://pypi.org/project/elasticsearch/

Tutorials/Guides:
    https://code.tutsplus.com/articles/how-to-index-and-query-data-with-haystack-and-elasticsearch-in-python--cms-29492

Elastisearch2:
    https://www.elastic.co/downloads/past-releases/elasticsearch-2-4-2

Haystack Commands:
    https://django-haystack.readthedocs.io/en/latest/management_commands.html#update-index
    1: python manage.py build_solr_schema –> create schema for solr schema.xml
    2: python manage.py update_index — > update new indexes to solr server
    3: python manage.py rebuild_index — > remove old indexes update all as new

Dependencies (Watch out for the versions compatibilities):
    pip install pyelasticsearch
    pip install "elasticsearch>=2.0.0,<3.0.0"
    pip install django-haystack
    Package                       Version
    ----------------------------- -------------------
    elasticsearch                 2.4.1 -> Critical
    elasticsearch-dsl             7.3.0
    django-elasticsearch-dsl      0.5.1
    django-elasticsearch-dsl-drf  0.17.6
    django-haystack               3.0
    django-haystack-elasticsearch 0.1.0

    or

    pip install elasticsearch==2.4.1 
    pip install django-elasticsearch-dsl==0.5.1
    pip install django-elasticsearch-dsl-drf==0.17.6
    pip install django-haystack==3.0
    pip install django-haystack-elasticsearch==0.1.0

Troubleshooting:
    Template Does Not Exists:
        text = indexes.EdgeNgramField(document=True, use_template=True, template_name="search\indexes\customers\customers_text.txt")



Background Process Ubuntu:
    Start a job:
        ./elasticsearch &
    View job list:
        jobs    
    Terminate job:
        kill %[job id]

JAVA Installation Ubuntu:
    https://vitux.com/how-to-setup-java_home-path-in-ubuntu/
    sudo apt install openjdk-8-jdk
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    echo $JAVA_HOME
    export PATH=$PATH:$JAVA_HOME/bin
    echo $PATH
    java -version
 
Ubuntu Troubleshooting Haystack TemplateDoesNotExists:
    https://stackoverflow.com/questions/17608100/haystack-indexing-error

    use_template=True

    Proper way of path

    ``search/indexes/{app_label}/{model_name}_{field_name}.txt``

    'search/indexes/{app-name}/note_text.txt'

    ── templates
│   │   ├── index.html
│   │   └── search
│   │       ├── indexes
│   │       │   └── customers
│   │       │       └── customer_text.txt
│   │       └── search.html
