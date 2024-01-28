from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_homepage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# def allowed_users(allowed_roles = []):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
            
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else: 
#                 return HttpResponse('You are not authorised to view this page')
        
            
        
 #       return wrapper_func
  #  return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'clients':
            return redirect('client_homepage')
        if group == 'agents':
            return redirect('agent_homepage')
        if group =='admins':
            return view_func(request, *args, **kwargs)
        else:
            # Handle the case when the user's group is not recognized
             unauthorized_response = """
                <html>
                <head>
                    <title>Unauthorized Access</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f8f8f8;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: #ff0000;
                        }
                    </style>
                </head>
                <body>
                    <h1>Unauthorized Access</h1>
                    <p>You do not have permission to access this page.</p>
                </body>
                </html>
            """
        return HttpResponse(unauthorized_response, status=403)  # You can customize the response accordingly
    return wrapper_func

def agent_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'clients':
            return redirect('agent_homepage')
        if group == 'agents':
            return view_func(request, *args, **kwargs)
        if group =='admins':
            return redirect('admin_homepage')
        else:
            # Handle the case when the user's group is not recognized
             unauthorized_response = """
                <html>
                <head>
                    <title>Unauthorized Access</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f8f8f8;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: #ff0000;
                        }
                    </style>
                </head>
                <body>
                    <h1>Unauthorized Access</h1>
                    <p>You do not have permission to access this page.</p>
                </body>
                </html>
            """
        return HttpResponse(unauthorized_response, status=403)  # You can customize the response accordingly
            
    return wrapper_func

def client_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'clients':
            return view_func(request, *args, **kwargs)
        if group == 'agents':
            return redirect('agent_homepage')
        if group =='admins':
            return redirect('admin_homepage')
        else:
             # Handle the case when the user's group is not recognized
             unauthorized_response = """
                <html>
                <head>
                    <title>Unauthorized Access</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f8f8f8;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: #ff0000;
                        }
                    </style>
                </head>
                <body>
                    <h1>Unauthorized Access</h1>
                    <p>You do not have permission to access this page.</p>
                </body>
                </html>
            """
        return HttpResponse(unauthorized_response, status=403)  # You can customize the response accordingly
            # Handle the case when the user's group is not recognized
            
    return wrapper_func