# finRecord
Financial Transaction Recording System

- Develop a Financial Transaction Recording System. The system must be capable of CRUD operations
Application has 3 different web pages 
 1. First one displays all recorded transactions (Transaction Records) Also gives option to Edit and Delete available entries and also adding an entry
 2. Second page: Add Transaction. User adds Date and Amount values for the new entry
 3. Edit Page: user navigated to upon clicking the edit entry option

https://www.loom.com/share/fdb7ffe092e44db583aab23e0c0ff891?sid=120ccc6b-3275-4261-9927-4a5fa7cc5347


Commands:
- source venv/bin/activate
- pip install -r requirements.txt
- Run flask locally:
  - flask run
- Pass environment variable:
  - FLASK_ENV=development flask run
- changes commit to heroku
  - git push heroku master 
- Workflow
  - $ heroku create finrecord-staging --remote staging
  - $ git push staging master
- Promote new version to production
  - $ heroku pipelines:promote --remote staging