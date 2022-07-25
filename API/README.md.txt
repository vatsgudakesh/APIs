#ROUTES-------For department app


'GET' : http://127.0.0.1:8000/department/    
'POST' : http://127.0.0.1:8000/department/ 
		
		Body example:{
        
        				"DepartmentName": "finance"
    				}
'PUT' : http://127.0.0.1:8000/department/id
		
		Body example:{
        				"DepartmentId": 9,
        				"DepartmentName": "finance"
    					}
'DELETE :http://127.0.0.1:8000/department/id

#ROUTES-----For employee app (replace department with employee)

