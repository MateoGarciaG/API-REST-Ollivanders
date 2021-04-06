Classes that we use for create Object of Items
from domain.Inventory import Inventory
from domain.normal_item import NormalItem
from domain.aged_brie import AgedBrie
from domain.backstagePasses import BackstagePasses
from domain.Sulfuras import Sulfuras
from domain.Conjured import Conjured

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
    
    @staticmethod
    def createObjectItem(item):
        """Create an Item Object which depends of the name of the Item to asign this item to a Class to create an Object from the Class selected. This method was created by @dfleta from github

        Args:
            item (list): A list that contains the info of a item, which have three element. Example:
            item = ['Elixir of the Mongoose', ' 5', ' 7']

        Returns:
            [Object]: Returns an Object which the type of this object depends of the Class which was selected from the name of the item
        """
        
        dictClassesItems = {"Sulfuras, Hand of Ragnaros": "Sulfuras",
                                "Aged Brie": "AgedBrie",
                                "Backstage passes to a TAFKAL80ETC concert": "BackstagePasses",
                                "Conjured Mana Cake": "Conjured",
                                "+5 Dexterity Vest": "Conjured",
                                "Normal Item": "NormalItem"}

        try:
            itemName = item[0]
            classItem = dictClassesItems[itemName]
        except KeyError:
            classItem = dictClassesItems["Normal Item"]
        finally:
            return eval(classItem + str(tuple(item)))
    
class SingletonOllivanders():
    
    instanceOllivanders = None
    
    @staticmethod
    def createStore():
        
        if not SingletonOllivanders.instanceOllivanders:
            
            SingletonOllivanders.instanceOllivanders = Factory.initRepo()
            
            return SingletonOllivanders.instanceOllivanders
        

# if __name__ == "__main__":
    
#     print(Factory.loadInventory())