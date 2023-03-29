InternshipAssignment :-


Postgres CLI -

connect to Postgres , create and populate tables -    psql -U postgres_username -d myDataBase_Name -a -f ./indian_banks.sql

Note: If file encoding error occurs, add this command at top of .sql file - SET CLIENT_ENCODING TO 'utf8';


Creating Django project -

                        - pipenv install django

			- django-admin startproject Myinternshipassignment .

			- django-admin startapp  Query
			
 Note: To auto create legacy data from postgres,use command: python manage.py inspectdb > models.py
 
Endpoints -                    

1) banklist/ - (GET) Endpoint to get all banks list.

2) branchdetails/ - (POST) Endpoint to get particular Branches details when bank and branch name are given.

3) specific_branchdetails/ - (POST) Endpoint to get all bank branches for a particular area.  

Methods used -

 `loads` method from json module to fetch data from request body

 `serialize` method from serializers module to serialize querysets to required formates 





















--'banklist/' is handled by views.Banklist 

Banks_Queryset = Banks.objects.all()
--list of all banks present in the database is featched using 'Banks' model.

bank_dict = serializers.serialize("python", [bank])[0]['fields']
--useing serialize method from serializers module to serializes 'bank' object to python object and assigining to bank_dict

2) Endpoint to get particular Branchs detailes when bank and branch name are given (POST) - branchdetails/

3) Endpoint to get particular Branch detailes when branch name is given (POST) - spicific_branchdetails/




used `loads` method from json module to fetch data from request body
used `serialize` method from serializers module to serialize querysets
