import redis
r=redis.Redis(decode_responses=True)

def get_user(name:str,age:str,phone:str):
    dict={"name":name,"age":age,"phone":phone}
    r.hmset(f"user:{phone}",mapping=dict)

def show_user(phone):
    print(r.hgetall(f"user:{phone}"))
    


def get_trip(src:str,dest:str,time:str,dev:str,passanger:list):
    dict={"src":src,"dest":dest,"time":time,"dev":dev,"passanger":passanger}
    r.hset({"trip_id":""})
    if not hasattr(get_trip,"trip_id"):
       get_trip.trip_id =1
       r.hmset(f"trip:{get_trip.trip_id}",mapping=dict)
       print(f"trip:{get_trip.trip_id} inserted")
    get_trip.trip_id +=1
    r.hmset(f"trip:{get_trip.trip_id}",mapping=dict)
    print(f"trip:{get_trip.trip_id} inserted")

def show_trip(id):
    print(r.hgetall(f"trip:{id}"))


def get_tour(price:str,leader:str,trip:str):
    dict={"price":price,"leader":leader,"trip":trip}
    if not hasattr(get_tour,"tour_id"):
       get_tour.tour_id =1
       r.hmset(f"tour:{get_tour.tour_id}",mapping=dict)
       print(f"tour:{get_tour.tour_id} inserted")
    get_tour.tour_id += 1
    r.hmset(f"tour:{get_tour.tour_id}",mapping=dict)
    print(f"tour:{get_tour.tour_id} inserted")

def show_tour(id):
    print(r.hgetall(f"tour:{id}"))

# get_user('reza','34','09357236211')
# get_user('sara','12','09376553365')
# show_user("09357236211")
# show_user("09376553365")

# get_trip("tehran","esfahan","thusday","train",str(["ali","mina","sahar"]))   
# get_trip("mashhad","shiraz","sunday","airplane",str(["omid","mina","reza","roya"]))  
# show_trip(1)
# show_trip(2)

# get_tour("150000","Mr.moradi",str({'src': 'tehran', 'dest': 'esfahan', 'time': 'thusday', 'dev': 'train', 'passanger': "['ali', 'mina', 'sahar']"}))
# show_tour(1)

# r.flushdb()

