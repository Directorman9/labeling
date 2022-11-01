import codecs, csv, random, string, re, pandas as pd
from db import db



def update_questions():    
    with codecs.open("data.tsv", encoding='utf-8', mode='r') as inptFile:
          reader = csv.reader(inptFile, delimiter='\t')
          number = 0
                  
          for line in reader:
              root = line[0].split('#')
              title = root[4]
              description = root[5]
              number = number+ 1
              q = {'number': number,
                   'title': title,
                   'description': description,
                  }
              db.Questions.update_one({'number': number },{"$set": {"title": title, "description": description}})
          
    return ('db populated successfully') 
    
'''
def populate_db():    
    with codecs.open("data.tsv", encoding='utf-8', mode='r') as inptFile:
          reader = csv.reader(inptFile, delimiter='\t')
          number = 0
                  
          for line in reader:
              root = line[0].split('#')
              title = root[4]
              description = root[5]
              number = number+ 1
              q = {'number': number,
                   'title': title,
                   'description': description,
                  }
              db.Questions.insert_one(q)
          
    return ('db populated successfully') 
   


def map_students_to_qstns():
    df = pd.read_csv("instructors.csv", sep=',', delimiter=None, header='infer')
    emails = df['Username'].tolist()
    frm = 18000#16000 #1
    to = 19000#17000  #1000
    for email in emails: 
        db.Questions.update_many({"$and": [{'number': { "$gte": frm }},{'number': { "$lte": to}}]},{"$set": { "email1": email}})
        frm += 1000
        to += 1000
        
    return ('students mapped successfully') 


def insert_users():
    df = pd.read_csv("students.csv", sep=',', delimiter=None, header='infer')
    emails = df['Username'].tolist()
    for email in emails:
        student = {'email':email,
                   'password': ''.join(random.choices(string.ascii_lowercase, k=7))    
                  }
        db.Users.insert_one(student)
        
    return ('Users added successfully')


def add_attributes():
    db.Questions.update_many({},{"$set":{'answer1': None, 'answer2': None}})
    return ('attributes added successfully')   
 

def remove_attribute():
    db.Questions.update_many({},{"$unset":{'answer': None}})
    return ('attributes added successfully')   
'''   
#print (populate_db())
print (update_questions())
#print (map_students_to_qstns())
#print (insert_users())
#print (add_attributes())
#print (remove_attribute())
