import json
import requests
import datetime
import time
import pyodbc
import sys
from pyodbc import IntegrityError
from termcolor import colored

def time_format():
    return 

data = {}
result = []
tim_e = str(datetime.datetime.now())

def connectToBD():
    return pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-IHSSCUQ;"
                      "Database=BD1;"
                      "Trusted_Connection=yes;")

def getAllItems():
    resp = requests.get('https://api.warframe.market/v1/items')
    data = resp.json()['payload']['items']
    return data

def getInfo(offer, item):
    return [item['url_name'], str(offer['platinum']),  offer['user']['last_seen'], offer['user']['status'], offer['user']['ingame_name'], offer['platform'], offer['last_update']]

def sendToDBSells(sellOrders, offer, item):
    cnxn = connectToBD()
    cursor = cnxn.cursor()   
    add = f"""INSERT INTO dbo.Table_6 
                VALUES ('{item['url_name']}', {int(offer['platinum'])},  
                        '{offer['user']['ingame_name']}', '{offer['user']['status']}', 
                        '{offer['user']['last_seen']}', '{offer['platform']}', '{offer['last_update']}');"""
    #print(add)
    cursor.execute(add) 
    cnxn.commit()        
    cnxn.close()       


def getSellOrders():
    data = getAllItems()
    time_start = datetime.datetime.now()
    print (f"Starting parsing - {time_start}")
    for item in data:
        if ('prime') in item['url_name']:
            respOrders = requests.get('https://api.warframe.market/v1/items/' + item['url_name'] + '/orders')
            itemOrders = respOrders.json()['payload']['orders']                                       
            for offer in itemOrders:
                sellOrders = []                
                if ('sell') in offer['order_type']:
                    try:
                        sellOrders = getInfo(offer, item)
                        sendToDBSells(sellOrders, offer, item)
                        print (f"{item['item_name']} order has been added...")
                    except IntegrityError:
                        print (colored('IntegrityError: this order is already in the dbo.Table_6', 'grey'))
                        continue                        
            time.sleep(5)
    time_end = datetime.datetime.now()
    print(f"End of parsing - {time_end}. Time of parsing - {time_end - time_start}.")
            
#getSellOrders()  

                # def formAProfitTable():
                #     data = getAllItems()
                #     cnxn = connectToBD()
                #     cursor = cnxn.cursor()
                #     cursor1 = cnxn.cursor()
                #     for it_em in data:
                #         if (('_set') in it_em['url_name'] and ('prime') in it_em['url_name']):
                #             sibling_items = []
                #             sibling_items = requests.get('https://api.warframe.market/v1/items/' + it_em['url_name']).json()['payload']['item']['items_in_set']
                #             for sibling in sibling_items:
                #                 if ('_set') not in sibling['url_name']:
                #                     for row in cursor1.execute(f"SELECT * FROM dbo.Table_7;").fetchone():
                #                         if row.min_price == None:                            
                #                             try:
                #                                 # siblings = [sibling['url_name']]
вот эта часть   #                                 cursor.execute(f"INSERT INTO dbo.Table_7 (item, set_parts) VALUES ('{it_em['url_name']}', '{sibling['url_name']}');")
  не работает   #                                 cnxn.commit()
                #                                 print(f"('{it_em['url_name']}', '{sibling['url_name']}') has been inserted into dbo.Table_7")
                #                             except IntegrityError:
                #                                 print (colored(f"IntegrityError (is not an Error): row with '{it_em['url_name']}', '{sibling['url_name']}' will be updated.", 'yellow'))
                #                                 update_info = cursor.execute(f"SELECT TOP 1 * FROM dbo.Table_6 WHERE (url_name = '{sibling['url_name']}' AND (user_status = 'ingame' OR user_status = 'online')) ORDER BY user_status ASC, platinum ASC;").fetchone()
                #                                 cursor.commit()
                #                                 cursor.execute(f"UPDATE dbo.Table_7 SET min_price = {update_info.platinum}, ingame_name = '{update_info.ingame_name}', last_update = '{update_info.last_update}' FROM dbo.Table_6 WHERE dbo.Table_6.url_name = dbo.Table_7.set_parts;")
                #                                 cnxn.commit()
                #                         else:
                #                             print (colored(f"IntegrityError (is not an Error): row with '{it_em['url_name']}', '{sibling['url_name']}' will be updated.", 'yellow'))
                #                             update_info = cursor.execute(f"SELECT TOP 1 * FROM dbo.Table_6 WHERE (url_name = '{sibling['url_name']}' AND (user_status = 'ingame' OR user_status = 'online')) ORDER BY user_status ASC, platinum ASC;").fetchone()
                #                             cursor.commit()
                #                             cursor.execute(f"UPDATE dbo.Table_7 SET min_price = {update_info.platinum}, ingame_name = '{update_info.ingame_name}', last_update = '{update_info.last_update}' FROM dbo.Table_6 WHERE dbo.Table_6.url_name = dbo.Table_7.set_parts;")
                #                             cnxn.commit()                            
                #                 else:
                #                     continue                
                                                
                    
                # formAProfitTable()    

def readFromDB():
    cnxn = connectToBD()
    cursor = cnxn.cursor()
    

                                                                                                                                                                    

def evaluateProfit():
    return
    






# def sortNames():
#     data = getAllItems()
#     for item in data:
#         if item['item_name'].find('Prime') != -1:
#             result.append([item['item_name'], item['url_name'], item['id'], tim_e])
#     return result
      

# def writeToFile():
#     result = sortNames()
#     path = 'J:\\Visual Studio Projects\\Warframe OBD\\Warframe Fetch\\'
#     filePathNameExt =  path + 'items.json'
#     with open(filePathNameExt, 'w') as json_file:        
#         json.dump(result, json_file, indent=(4))

# def sendToDB():     
#     cnxn = connectToBD()
#     cursor = cnxn.cursor()
#     with open ('items.json', 'r') as data_file:
#         data = json.load(data_file)
#     add = "INSERT INTO dbo.Table_3 VALUES "
#     for obj in data:
#         addrow = add + f"('{obj[0]}', '{obj[1]}', '{obj[2]}', '{obj[3]}');"
#         cursor.execute(addrow) 
#         cnxn.commit()        
#     cnxn.close()            

# def test():
#     cnxn = connectToBD()


#     cursor = cnxn.cursor()
#     cursor.execute('SELECT * FROM dbo.Table_3')
    
#     for row in cursor:
#         print('row = %r' % (row,))

    
    