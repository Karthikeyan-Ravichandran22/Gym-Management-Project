
class Gym_memberships:
   regimen={}
   coustmer_data=dict()
   def __init__(self,coustmer_id,coustmer_name):
       self.coustmer_id=coustmer_id
       self.coustmer_name=coustmer_name

   @classmethod
   def add_coustmer(cls,coustmer):
        Gym_memberships.coustmer_data[coustmer.getphone_no()] = coustmer

ob=Gym_memberships('147MT','Karthikeyan')
