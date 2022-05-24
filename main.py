import requests
from decouple import config
url="https://backend.prabhucapital.com/api/v1/public/demat-allotment"

def get_demat_allotment(boid,company):
    query_parameter={"boid":boid,"company":company}
    data=requests.get(url,params=query_parameter)
    result=data.json()
    allotment=result.get("data").get("allotmentList")
    if len(allotment)==0:
        print("No Alloted:",boid)
    else:
        print("Alloted:",boid)

        
List_of_boids=[config('suman'),config('chhandra'),config('min'),config('dor'),config('lata'),config('chadra')]
for _ in List_of_boids:
    get_demat_allotment(_,'River Falls Power Limited')
