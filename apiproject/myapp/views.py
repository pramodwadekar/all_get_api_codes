from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests, json

# show api data in JsonResponse
# def apidata(request):
#     url = "https://api.publicapis.org/entries"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return JsonResponse(data)
#     else:
#         return JsonResponse("false")


# show api data in html page
# def apidata(request):
#     url = "https://api.publicapis.org/entries"
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         return render(request, "xyz.html", {"data": data})
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)


# extract api data and show html
# def apidata(request):
#     url = "https://api.publicapis.org/entries"
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         key = data['entries'][1]
#         if key["API"] == "Axolotl":
#             data1 = "this is right" 
#             return render(request, "xyz.html", {"data": key,"data1":data1})
#         else:
#             data1 = "this is rong"
#         return render(request, "xyz.html", {"data": key, "data1":data1})
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)



# get data using sessiong parameters and get data
# def proviosinal_degree(request):
#     method = "get_alumni_provisional_degree_global"
#     session_id = request.session.get('id')
#     parameters = {"id": session_id}
#     response = requests.post(BASE_URL + method, data=parameters)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         # st_data = data['data'][0]['data']
#         return render(request, "json.html", {"data": data})
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)

# get api data using parameters 
# #base url
# BASE_URL = "https://www.birtikendrajituniversity.ac.in/"

# # Login alumni Function
# def auth_alumni(request):   
#     if request.method == "POST":
#         method = "get_alumni_login_global"
#         username = request.POST['username']
#         password = request.POST['password'] # Retrieve the password from the POST data
#         parameters = {"username": username, "password": password}
#         response = requests.post(BASE_URL + method, data=parameters)   
#         data = json.loads(response.text)
#         status = data['data'][0]['status']

#         login_data = data['data'][0]['data']
#         if status == "true":
#             request.session['id'] = login_data['id']
#             return redirect("alumni_home")
#         else:
#             massage ="please check username and password"
#             return render(request, "alumni_login.html", {"msg":massage})
        
# # alumni Id Card Function
# def alumni_id_card(request):
#     method = "get_my_alumni_profile_global"
#     session_id = request.session.get('id')
#     parameters = {"id": session_id}
#     response = requests.post(BASE_URL + method, data=parameters)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         st_data = data['data'][0]['data']
#         # print(st_data)
#         return render(request, "id_card.html", {"data": st_data})
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)


# def proviosinal_degree(request):
#     method = "get_alumni_provisional_degree_global"
#     session_id = request.session.get('id')
#     parameters = {"id": session_id}
#     response = requests.post(BASE_URL + method, data=parameters)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         st_data = data['data'][0]['data']
#         return render(request, "provisional_degree.html",{"provisional_degree":st_data})
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)

# # print_proviosinal_degree function
# def print_proviosinal_degree(request):
#     method = "get_alumni_provisional_degree_global"
#     session_id = request.session.get('id')
#     parameters = {"id": session_id}
#     response = requests.post(BASE_URL + method, data=parameters)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = json.loads(response.text)
#         st_data = data['data'][0]['data']
#         courses = [262, 263, 261, 228, 278]
#         context = {
#     'provisional_degree': provisional_degree,
#     'courses': courses,"provisional_degree":st_data
# }
#         return render(request, "print_provisional_degree.html",context=context)
#     else:
#         return HttpResponse(f"API request failed with status code {response.status_code}", status=500)

