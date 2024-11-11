import json

centrs=[]
def load_data():
    #file=open('centrs.json', 'r')
    #data=json.load(file)
    #file.close()
    global centrs
    #centrs=data['centrs']
    print('DATI PIEVIENOTI')


def add_centrs():
    centrs_name=input('people name: ')
    centrs_adress=input('people  adress: ')
    centrs_id=input('people  id: ')
   
    centr={
            'name':centrs_name,
            'adress':centrs_adress,
            'id': centrs_id,
             'contacts': []
    }
    while (True):
            response=input('Vai vēlies pietekties apmeklejumam (jā/nē)')
            if response=='jā':
                print("Bernu centrā informācija:")
                contact_name=input('Ievadiet cik ilgs apmeklējums:')
                contact_position=input('Ievadiet bernu daudzumu:')
                contact_id=input('people id:')
                contact={
                    'name':contact_name,
                    'adress': contact_position,
                    'id': contact_id
                }
                centr['contacts'].append(contact)
            elif response=='nē':
                break
    centrs.append(centr)

def print_centrs():
     for centrs in centrs:
            print('---CENTRS---')
            print(f"{centrs['name']}({centrs['id']})")
            print(f"Adrese:{centrs['adress']}")
            print(f"Kontaktu skaits:{len(centrs['contacts'])}")
 
def save_data():
    data={
            'centrs': centrs
        }
    print('SAGLĀBA DATUS.....')
    file=open('centrs.json', 'w')
    json.dump(data, file, indent=4)
    print('Data saved')

def find_centrs_by_id():
     centrs_id=input('Ievadiet organizācija ID:')
     for centrs in centrs:
          if centrs['id']==centrs_id:
            print('---CENTRS---')
            print(f"{centrs['name']}({centrs['id']})")
            break

def main(): 
    #load_data()
    while (True):
        response=input('(1) Add organization (2) Print organization (3) Find contact (4) Exit ')
        if response=='1':
            add_centrs()
                
        elif response=='2':
            print_centrs()
        elif response=='3':
            add_centrs()    
        elif response=='4':
            save_data()
            print(centrs)
            exit()
        else:
            print("Izvele skaitļu 1,2,3 vai 4")
            continue
main()