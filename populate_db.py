import codecs, csv, re
from db import db


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
                   'answer': None
                  }
              db.Questions.insert_one(q)
          
    return ('db populated successfully') 
'''     


def map_students_to_qstns():
    df = pd.read_csv("students.csv", sep=',', delimiter=None, header='infer')
    emails = df['Username'].tolist()
    frm = 1
    to = 1000
    for email in emails: 
        db.Questions.update_one({"$and": [{'number': { "$gte": frm }},{'number': { "$lte": to}}]},{"$set": { "email": email}})
        frm += 1000
        to += 1000
        return ('students mapped successfully') 


#print (populate_db())
print (map_students_to_qstns())
