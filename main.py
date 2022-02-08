import json
from datetime import date
from datetime import datetime
import random
import os
from os import path

def userlogin():
    with open("UserDetails/"+str(username)+"logindetails.json") as read_file:
            data_of= json.load(read_file)
            print(data_of)
            dic  = {'user':[]}
            userData = {'username':"", 'password':""}
            json_data=open("UserDetails/"+str(username)+"logindetails.json", "r")
            data=json.load(json_data)
            json_data.close()
            for i in data["user"]:
                if i["username"] == username:
                    if i["password"] == password:
                        print("Login Succesfull")
                    else:
                        print("Invalid Password")
                else:
                    print("Invalid Username")
                

def usersignup():
    dic  = {'user':[]}
    userData = {'username':"", 'password':""}
    userData['username'] = username
    userData['password'] = password
    print(userData)
    dic['user'].append(userData)
    print(dic)
    json_file = open("UserDetails/"+str(username)+"logindetails.json", "w")
    json.dump(dic, json_file, indent = 2)
    json_file.close()
    print("congrarts", username, "you are Signed Up Successfully")

print()
print("                  Welcome To Nehru Parking System                 ")
print()
print("     ----------------------------------------------------------")
print()


customer = input('For signup Enter : 1 \n \nFor login Enter  : 2\n \n')

if customer == '1':
    username = input('Please Enter Name  ')
    password = input('Please Enter Password  ')
    if path.exists("UserDetails/"+str(username)+"logindetails.json")==True:
        userlogin()
    else:
        usersignup()


elif customer == '2':
    username = input('Please Enter Name  ')
    password = input('Please Enter Password  ')
    usersignup()

def userslip():
    print()
    print('        Parking Slip            ')
    print()
    print("  ----------------------------- ")
    print()
    print(" | User Name    : ",username)
    print(" | Vehicle Type : ", "Two_wheelers")
    print(" | Vehicle No   : ",slip["vehicle No"])
    print(' | Mobile_no    : ', slip["Mobile_no"])
    print(" | Date         : ", slip["Date"])
    print(" | Time         : ", slip["Time"])
    print(" | Token No     : ", slip["Token No"])
    print(" | Total Amount : ",slip["charges"],"/-")
    print("       THANK YOU FOR VISITING      ")


total_parking_space = {"Two_wheelers":[1,2,3,4,5,6,7,8,9,10],"Three_Four_wheelers":[11,12,13,14,15,16,17,18,19,20],"Above_Four_Wheelrs":[21,22,23,24,25,26,27,28,29,30]}

now = datetime.now()

day = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

mode =input("1. Entry \n2. Exit")

vehicle_type = input('Enter veicle type \n1. Two wheelers - 100 \n2. Three/Four wheelers - 200  \n3. Above Four Wheelrs - 300 ')

mobile_no = int(input('Enter your mobile number (len should be 10) '))

if len(str(mobile_no )) == 10:
    mobile_no=mobile_no
else:
    mobile_no = int(input('Number should must be 10 Digits '))

vehicle_no = input('Enter vehicle number  ')

if mode == "1":

    if vehicle_type == '1':
        print("Reamaining Slots : ",total_parking_space["Two_wheelers"])
        if len(total_parking_space["Two_wheelers"]) == 0:
            print('Sorry, There is not space available for Now. You can try after somtime')
        else:
            token = random.choice(total_parking_space["Two_wheelers"])
            total_parking_space['Two_wheelers'].remove(token)
            slip = {"Vehicle Type":"Two_wheelers","vehicle No":vehicle_no,'Mobile_no': mobile_no,"Date":day,"Time":time,"Token No":token , "charges":100}
            
            json_file = open("ParkingData/"+str(username)+"slip.json", "w")
            json.dump(slip, json_file, indent = 2) 
            userslip()

    elif vehicle_type == '2':
        print("Reamaining Slots : ",total_parking_space["Three_Four_wheelers"])
        if len(total_parking_space["Three_Four_wheelers"]) == 0:
            print('Sorry, There is not space available for Now. You can try after somtime')
        else:
            token = random.choice(total_parking_space["Three_Four_wheelers"])
            total_parking_space['Three_Four_wheelers'].remove(token)
            slip = {"Vehicle Type":"Three_Four_wheelers","vehicle No":vehicle_no,'Mobile_no': mobile_no,"Date":day,"Time":time,"Token No":token, "charges":200}
            
            json_file = open("ParkingData/"+str(username)+"slip.json", "w")
            json.dump(slip, json_file, indent = 2) 
            userslip()

    elif vehicle_type == '3':
            print("Reamaining Slots : ",total_parking_space["Above_Four_Wheelrs"])
            if len(total_parking_space["Above_Four_Wheelrs"]) == 0:
                print('Sorry, There is not space available for Now. You can try after somtime')
            else:
                token = random.choice(total_parking_space["Above_Four_Wheelrs"])
                total_parking_space['Above_Four_Wheelrs'].remove(token)
                slip = {"Vehicle Type":"Above_Four_Wheelrs","vehicle No":vehicle_no,'Mobile_no': mobile_no,"Date":day,"Time":time,"Token No":token,"charges":300}
                
                json_file = open("ParkingData/"+str(username)+"slip.json", "w")
                json.dump(slip, json_file, indent = 2) 
                userslip()
    
else:

    tokenNum = int(input("Enter Token  "))

    if path.exists("ParkingData/"+str(username)+"slip.json")==True:
        json_data=open("ParkingData/"+str(username)+"slip.json", "r")
        slip=json.load(json_data)
        if slip["vehicle No"] == vehicle_no:  
            if tokenNum == slip["Token No"]:
                userslip()
            else:
                print("Please once check your Token Num")
        else:
            print("This Vehicle Doesn't park here")
    else:
        print("No vahicle with this user exist")







