import pymongo

#membuat koneksi url mongo
koneksi_url ="mongodb://localhost:27017"

def cekKoneksi() :
    client = pymongo.MongoClient(koneksi_url)
    try:
        cek = client.list_database_names()
        print(cek)
    except:
        print('database error')

cekKoneksi()

#membuat database baru
def createDatabase():
    myclient = pymongo.MongoClient(koneksi_url)
    mydatabase = myclient['db_wisatawan']
    mycollection = mydatabase['wisatawan']
    mydocument = mycollection.insert_one({'nama' : 'Jono'})

    return mydocument


#melakukan inisialisasi pada class MongoCrud
class MongoCRUD:
    def __init__(self, data, koneksi):
        self.client = pymongo.MongoClient(koneksi)
        database = data['database']
        collection = data['collection']
        cursor =self.client[database]
        self.collection=cursor[collection]
        self.data = data

    #function read data
    def read(self):
        documents = self.collection.find()
        value = [{
            item:data[item] for item in data if item != '_id'} for data in documents]
        return value
    
    
if __name__ =='__main__':
    data = {
        #nama database yang akan disambungkan
        "database" : "db_wisatawan",
        #nama collection yang akan disambungkan
        "collection" : "wisatawan",
    }

    mongo_objek = MongoCRUD(data, koneksi_url)
    read_data =mongo_objek.read()
    print(read_data)