from bson.objectid import ObjectId
from db.database import Database

class BibliotecaDAO:
    def __init__(self):
        self.db = Database(database='biblioteca', collection='livros')
        self.collection = self.db.collection

    def create_livro(self, titulo: str, autor: str, ano: int, preco: int):
        res = self.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
        return res.inserted_id

    def read_livro_by_id(self, id: str):
        res = self.collection.find_one({"_id": ObjectId(id)})
        return res

    def read_livro(self, ano: int ):
        res = self.collection.create_index({"ano": ano}, {"unique": True})
        res1 = self.collection.find({"ano": ano})
        return res1
    def update_livro(self,id: str, titulo: str, autor: str, ano: int, preco: int):
        res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
        return res.modified_count

    def update_preco_livro(self,id: str, preco : int):
        res = self.collection.update_one({"_id": ObjectId(id)},{"$set":{"preco":preco}})
        return res.modified_count
    def delete_livro_by_id(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count
    def delete_livro(self, titulo: str):
        res = self.collection.delete_one({"titulo": titulo})
        return res.deleted_count