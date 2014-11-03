class question(object):
  def __init__(self,id,kw):
    self.id=id
    self.kw=kw
    self.num_match=[]
  def __repr__(self):
    return str(self.id)

            
if __name__=="__main__":
  question(1,[])

