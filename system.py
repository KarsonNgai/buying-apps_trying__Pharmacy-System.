class inventory():
  single_store={}
  bulk_store={}
  payment={}
  def ind_storage(self, name, price):
    self.single_store.setdefault(name,price)
    print(self.single_store)
    
  def bulk_storage(self, size,name, price):
    if name not in self.bulk_store:
      self.bulk_store.setdefault(name,{})
    self.bulk_store[name].setdefault(size,price)
    
    print(self.bulk_store)
  def how_much(self, name, price):
    self.payment[name]=price

class Pharmacy_system():
  buying_lst_show={}
  def __init__(self):
    #index
    sel=input('Welcome to Super Pharmacy System.\n1: Create Pharmacy Item\n2: Add Item to Order\n3: Show Order Detail\n4: Order Payment\n5: Exit\nPlease input your choice. (1 - 5):\n').strip(' ')
    if sel=='1':
      self.item_creation()
    elif sel=='2':
      self.item_menu()
    else:
      print('quit')
      pass
  
  def item_creation(self):
    
    sel=input('Please Indicate the Menu Item You Want to Create:\n1 - Individual\n2 - Bulk\n').strip(' ')
    if len(sel)==0:
      print('it cannot be empty.\n===================\n')
      self.__init__()
    #single
    elif sel.strip() =='1':
      name=input('Enter the Item Name for the New Menu Item:').strip(' ').upper()
      if len(name)==0:
        print('The Name for the New Item cannot be Empty.\n===================\n')
        self.__init__()
      if name in inventory.single_store:
        print('The Name for the New Item Already Exist.\n\n======')
        self.__init__()
      while True:
        price=input(f'Enter the price for a {name}').strip(' ')
        try:
          if int(price)>0:
            break
        except:
          print('The price for the New Item is Invalid.')
      inventory().ind_storage(name,price)
      print(f'A Single item {name} is Created at the price of ${price} each.')
    #bulk  
    elif sel.strip() =='2':
      size=input('Please Input the size for your item (S: small M: medium L: large)').upper()
      if size not in ['S','M','L']:
        print(f'The inputted size, {size}, is invalid.')
        self.__init__()
  
      name=input('Enter the Item Name for the New Menu Item:').upper()
      if len(name)==0:
        print('The Name for the New Item cannot be Empty.\n===================\n')
        self.__init__()
      if name in inventory.bulk_store:
        
        if size in inventory.bulk_store[name]:
          print('The Name for the New Item Already Exist.\n===============\n')
          self.__init__()
      while True:
        price=input(f'Enter the price for a pack of Economic masks with the size ({size})')
        try:
          if int(price)>0:
            break
        except:
          print('The price for the New Item is Invalid.')
      inventory().bulk_storage(size,name,price)
      print(f'A Bulk Item of {name} ( {size} ) is Created.')
    self.__init__()
  def item_menu(self):
    #index_name {index:name} mainly use to link the inventory dic
    index_name={}
    #the following 3 print use for testing
    if len(inventory.single_store)==0 and len(inventory.bulk_store)==0:
      print('There is No Item Available in this System.\nPresse Create New Item First.\n\n')
      self.__init__()

    #print the buying list #<>require formating
    counting=0
    strs=''
    for i,p in inventory.single_store.items():
      counting+=1
      index_name.setdefault(str(counting),i)
      strs+=str(counting)+'|Individual  '+ i+'|'+str(p)+'\n'
    for i in inventory.bulk_store:
      for k,v in inventory.bulk_store[i].items():
        counting+=1
        index_name.setdefault(str(counting),i+'('+k+')')  
        strs+= str(counting)+'|Bulk  '+i+'|'+k+'|'+str(v)+'\n' #formate
    print(strs) #formate

    #input the item index and quantity
    sel2=(input('Please Input the Item for the Current Order (1 - {}, 0 to return the previous menu): \n'.format(counting))).strip(' ')
    if sel2=='0':
      self.__init__()
    if sel2 not in [str(i) for i in range(1,counting+1)]:
      print('Invalid Choice.')
      self.__init__()
    #elif sel2 not 
    sel3=input('Please Input the Quantity of \'{}\' You Want to Buy: '.format(index_name[sel2]))
    try: 
      if int(sel3) >0:
        pass
    except:
      print('The Value of Quantity Must Be Greater Than 0.')
      self.__init__()
  
    #single item and bulk item_geting name from index_name
    if '(S)' in index_name[sel2] or '(M)' in index_name[sel2] or '(L)' in index_name[sel2]:
      get_name=index_name[sel2].split('(')[0]
      get_size=index_name[sel2].split('(')[1].split(')')[0]  #split and get the size form index_name
      get_price=inventory.bulk_store[get_name][get_size]
    else: 
      get_name=index_name[sel2]
      get_price=inventory.single_store[get_name]
    total_price=float(get_price)*float(sel3)

    #inventory.payment store the qty and total price
    inventory().how_much(index_name[sel2], total_price)
    self.buying_lst_show[index_name[sel2]]='{}   @ {} {} subtotal: {}\n'.format(index_name[sel2],float(get_price), sel3, total_price)
    strs=''
    for i in self.buying_lst_show:
      strs+=self.buying_lst_show[i]
    print('>>>',strs)
    print('=========You have ordered 1 item(s)===============')
    self.item_menu()
