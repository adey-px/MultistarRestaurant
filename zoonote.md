### Using Custom User model
- If ran migrations earlier, after creating custom user model in 'account' app, 
  delete the table in db and the db itself. Re-create the db in postgres. 
  Otherwise there might be a conflict bcos django already has built-in User model
- Deactivate .venv, reactivate it again and make fresh migrations
- Also create new Superuser since the old ones would have been deleted also

### Form
When creating form in django, its actully form fields being created.
You still need to insert those fields insde html form tags. And always
add {% csrf_token %} whenever the form method is 'post'

### Create .gitignore
npx gitignore nodejs for nodejs app
npx gitignore python for python app

### Activate virtual env
Bash terminal - source .venv/Scripts/activate 
Windows prompt - .venv\scripts\activate