
# Queslet-questionbank

The website is used to manage the question bank, support users to enter according to Case 2 of FPT University, the teacher can import the Directory (including word files and images) and the website will detect duplicate questions that already exist. in which the question bank. Using framework Django, Database(Picone, PostgreSQL)





![Logo](images/Logo.png)


## Framework

[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue)](https://www.python.org/downloads/release/python-380/) [![Django](https://img.shields.io/badge/Django-4.1.7-green)](https://www.djangoproject.com/) [![EasyOcr](https://img.shields.io/badge/EasyOCR-%202.0-blue.svg)](https://github.com/JaidedAI/EasyOCR) [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/) [![PostSQL](https://img.shields.io/badge/PostSql-blue)](https://www.postgresql.org/) [![Pinecone](https://img.shields.io/badge/Pinecone-blue)](https://www.pinecone.io/learn/vector-indexes/)

## Deployment
Before run install all library in requirements.txt. 

### Model
- Create folder 'queslet/model/' inside application and unzip [Sbert Model](https://drive.google.com/file/d/1-nxMDQR7P3vXBHfx6dppcMm1ah64v6_g/view?usp=share_link)
### Installation 
- Create database name 'queslet'
- Change password postSql in file setting.py
- Run cmd command 
```bash
python manage.py showmigrations 
python manage.py migrate 
python manage.py createsuperuser
admin
```


- Run Sql script 
```bash
INSERT INTO questionbank_subject (subject, user_id)
VALUES ('math', 'admin'), ('english', 'admin');

COPY questionbank_mcq
FROM '[path to datbase.csv]' 
DELIMITER ',' 
CSV HEADER;
```
- Run cmd command
```bash
python manage.py runserver
```

## Screenshots
**Homepage**

![App Screenshot](images/Homepage.png)

**Import Page**

![App Screenshot](images/Importpage.png)

