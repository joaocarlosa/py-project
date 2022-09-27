class HotelModel():
    
    
    def __init__(self, id, name, email, business, role, manager):
        self.id = id,
        self.name = name
        self.email = email,
        self.business = business
        self.role = role
        self.manager = manager
        
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'business': self.business,
            'role': self.role,
            'manager': self.manager,
        }
        


enterprises = [{
    "id": "0",
    "name": "Haldane",
    "email": "haldane@credihabitar.com",
    "business": "CrediHabitar",    
    "role": "CEO",
    "manager": "Haldane"
},
{
    "id": "1",
    "name": "Tiago",
    "email": "tiago@credihabitar.com",
    "business": "CrediHabitar",    
    "role": "CDO",
    "manager": "Tiago"
},
{
    "id": "2",
    "name": "Rodrigo",
    "email": "rodrigo@credihabitar.com",
    "business": "CrediHabitar",    
    "role": "CDO",
    "manager": "Tiago"
}]