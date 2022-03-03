#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# login_info = {}
stud_info = {}
last_rollno = 0

def title ():
    print ('-'*50)
    print ('Lexicon International School'.center(50))
    print ('-'*50)


def login_page():
    print ('Login Page :')
    print ('1 : Teachers Login')
    print ('2 : Students Login')
    print ('3 : Create login for New User')
    

def add_login(seq,new_uname,new_pwd):
    global login_info
    if seq not in login_info:
        login_info[seq]= {'username' : new_uname , 'password': new_pwd}
        return True
    else:
        return False        
        
def get_rollno():
    global last_rollno
    last_rollno += 1
    return last_rollno    

def add_info(last_rollno,fname,eng,math,sci,percentage):
    global stud_info
    if last_rollno not in stud_info :
        stud_info[last_rollno] = {'fullname' : fname ,'eng': eng,'math' : math,
                               'sci':sci,'percentage':percentage}
        
        
def select_action():    
    print ('-'*50)
    print ('1 : Enter Students Info ')
    print ('2 : Search Roll Number')
    print ('3 : Get Result')
    
    
def enter_stud_details():
    title()
    global stud_info
    get_rollno()
    
    if last_rollno not in stud_info.keys():
        sfname     = input ('Enter Students Full Name     :')
        seng       = input ('Enter Students English Marks :')
        seng       = int(seng)
        smath      = input ('Enter Students Math Marks    :')
        smath      = int(smath)
        ssci       = input ('Enter Students Science Marks :')
        ssci       = int(ssci)
        prnctge    = (seng+smath+ssci)/3
        prnctge    = int(prnctge)
        add_info(last_rollno,sfname,seng,smath,ssci,prnctge)
                      
    else:
        print('Duplicate Roll Number')

        
def search_rollno():
    title()
    global stud_info
    
    for k in stud_info.keys():
        nroll={'rlno':[k],'name':[stud_info[k]['fullname']]}
        
        sname= input ('Enter Students Name to search : ')
        if sname in nroll['name']:
            print ('Name                                    Roll Number')
            print ('-'*50)
            print (f'{sname}                                    {k}')
        k+=1     

        
def get_rank():
    for a in stud_info.keys():
            percentagelist = [stud_info[a]['percentage']]
            percentagelist.sort()
            
            
def print_result():
    for i in stud_info.keys():
            global last_rollno
            eng = stud_info[i] ['eng']
            mat = stud_info[i] ['math']
            scie = stud_info[i] ['sci']
            ptage = stud_info[i] ['percentage']
            f_name= stud_info[i]['fullname']
            rolno= last_rollno
            print (f'Name         :{f_name}')
            print (f'Roll Number  :{rolno}')
            print ('-'*50)
            print (f'English    : {eng}')
            print (f'Maths      : {mat}')
            print (f'Science    : {scie}')
            print ('-'*50)
            print (f'Percentage : {ptage} %')
            print (f'Rank       : ')
            if ptage <35:
                print ('Result  : Fail')
            else :     
                print ('Result     : Pass') 
    

def get_result():
    title()
    global stud_info
    rollno =input ('Enter Students Roll no :') 
    rollno = last_rollno
    
    if rollno in stud_info.keys():
        print_result()
    else :
        print('Roll Number not found') 
        
def detail_choices():
    for details_choice in [1,2,3]:
                select_action()  
                details_choice=input('Enter Your choice : ')
                details_choice = int(details_choice)
                if details_choice==1:
                    enter_stud_details()
                elif details_choice==2:
                    search_rollno()
                elif details_choice==3:
                    get_result()
                else :
                    print('ERROR : Enter correct choice')  
        
def details():
    global login_info
    get_uname= input('Enter Username : ')
    get_pwd= input('Enter Password : ')
    seqs=login_info.keys()
    for i in  seqs:
        j=login_info[i]
        if get_uname in j.values()  and get_pwd in j.values() :
            detail_choices()            
        else :
            print ("User not found. Please enter correct login details.")

def login():
    title() 
    login_page()
    login_choice=input('Enter Your login choice : ')
    if login_choice.isdigit():
        login_choice = int(login_choice)
         
        if login_choice == 1 :
            print ('-'*50)
            print ('Teachers Login'.center(50))
            print ('-'*50)
            details()
        elif login_choice == 2 :
            print ('Student Login not available yet')
        elif login_choice == 3 :
            new_uname = input('Enter New Username : ')
            new_pwd   = input('Enter New Password : ')
            for a in range(1,3):
                global login_info
                add_login(a,new_uname,new_pwd)
                a+=1
                break
           
        else :
            print ('Wrong Input!!! Please try again')
    else:
        print('ERROR : Enter correct choice') 

   
     
for i in range(100):
    login()
    i+=1

