# The following are the details of trains:
"""

Train No                   Train Name              From         To         Running days                      Sleeper Fare          AC Fare

16453                   Prasanti Express           SBC          BBS      'Mo', 'We', 'Th'                       600                 987

25627                  Karnataka Express           SBC          DEC        'Su', 'Tu'                           1600                2500

22642                Trivandrum SF Express         VSKP         TVM   'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'         800                1256

22905                 Okha Howrah Express          ST           KOAA        'We', 'Sa'                           987                 2879

Represent each train's detail as a dictionary in the following format:
train_dict={“train_no”:train number, “name”:train name, “from”:source, “to”:destination, “days_of_run”:list of running days, “sleeper_fare”:sleeper fare, “ac_fare”:AC fare }

Create a list of trains, name it as train_list. Consider it to be a global variable.
Refer the table below for the error messages to be returned for various conditions.

 get_train_name(train_no)

        This function accepts the train number and returns the dict which contains the details of the train.

get_trains_for_day(day_of_run)

       This function accepts a day and returns the list of numbers of the trains running on that day.

get_total_fare(train_no,passenger_dict)

       This function accepts train_no and a dictionary of passenger details. The passenger_dict is of the following format:
       passenger_dict={ “sleeper”:5, “ac”,1 }
       This function returns the total fare based on the passenger details and train number.
"""
# Code:  

train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    #start writing your code here
    for i in train_list:
        if train_no == i["train_no"]:
            return i
    return "Invalid Train_no"
           
def get_trains_for_day(day_of_run):
    #start writing your code here
    a = [i["train_no"] for i in train_list if day_of_run in i["days_of_run"]]
    if len(a) > 0:
        return a
    else:
        return "Invalid day"

def get_total_fare(train_no,passenger_dict):
    #start writing your code here
    for i in train_list:
        if i["train_no"] == train_no:
            return i["sleeper_fare"]*passenger_dict["sleeper"] + i["ac_fare"]*passenger_dict["ac"]
        else:
            pass
    return "Invalid Train_no"

print(get_train_name(25627))
print(get_trains_for_day("Mo"))
print(get_total_fare(22642,{"sleeper":5, "ac":1}))

