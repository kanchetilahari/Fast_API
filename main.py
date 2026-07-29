from fastapi import FastAPI,Body



app=FastAPI()
students = [
    {"name":"srihari","course":"DS","student_id":1},
    {"name":"srinu","course":"DA","student_id":2},
    {"name":"rajesh","course":"DS","student_id":3},
    {"name":"Srikanth","course":"DA","student_id":4}]

@app.get('/')
def hpme_page():
   return {"message":"welcome to FastAPI 552_B"}
#http://127.0.0.1:8000/get_all_students
@app.get('/get_all_students')  # get all students is done
def view_all_students():
   return {"operation":"GET",
           "result":students}
#http://127.0.0.1:8000/get_single_students_by_id/1
@app.get('/get_single_students_by_id/{student_id}')   #path parameter {}
def single_student(student_id:int):
   for i in students:
      if i['student_id']==student_id:
         return{"request":"GET",
               "result":i}
   return{"message":"student id you are looking for is not available in the student list"}

#POST
@app.post('/add_students')
def add_single_student(addnewstudent=Body()):
   students.append(addnewstudent)
   return {"operation":"POST","students details":students}


#update(PUT)
@app.put('/update_student_details_by_id/{student_id}')   #path parameter
def single_student(name:str,course:str,student_id:int):   #query parameter
   dict_={"name":name,"course":course,"student_id":student_id}
   for i in students:
      if i['student_id']==student_id:
         p=i.update(dict_)
         return{"request":"PUT",
               "previous detail":i
               }
   return{"message":"student id you are looking for is not available in the student list"}


#DELETE
@app.delete('/delete_student_details_by_id/{student_id}')
def single_student(student_id:int):
   for i in range(len(students)):
      if students[i]['student_id']==student_id:
         
         d=students.pop(i)
         return{"request":"DELETE",
               "deleted detail":d
               }
   return{"message":"student id you are looking for is not available in the student list"}
