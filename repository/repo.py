# Classes that we use for create Object of Items
# from domain.Inventory import Inventory
# from domain.normal_item import NormalItem
# from domain.aged_brie import AgedBrie
# from domain.backstagePasses import BackstagePasses
# from domain.Sulfuras import Sulfuras
# from domain.Conjured import Conjured

# CSV
import csv
import os

class Factory():
    
        
    # @staticmethod
    # def loadInventario():
        
    @staticmethod
    def loadInventory():
        
        # tienda = Inventory()
        
        # filename = "C:/Users/Mateo/Documents/APUNTES_DUAL_FP_2020/PROJECTS/Flask_APIRestFul_Ollivanders/API-REST-Ollivanders/repository/data_items.csv"
        
        # file = open(filename, 'r')
        
        # reader = csv.reader(file)
        
        file_dir = os.path.dirname(__file__)
        
        filename = "data_items.csv"
        
        absolute_file_path = os.path.join(file_dir, filename)
        
        with open(absolute_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            inventory = []
            
            for row in csv_reader:
                
                inventory.append({'name': row[0], 'sell_in': int(row[1]), 'quality': int(row[2]) })
                
        return inventory
    
class SingletonOllivanders():
    
    instanceOllivanders = None
    
    @staticmethod
    def createStore():
        
        if not SingletonOllivanders.instanceOllivanders:
            
            SingletonOllivanders.instanceOllivanders = Factory.initRepo()
            
            return SingletonOllivanders.instanceOllivanders
        

# if __name__ == "__main__":
    
#     print(Factory.loadInventory())