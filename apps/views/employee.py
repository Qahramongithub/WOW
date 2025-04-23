from django.views.generic import ListView


class EmployeeOneListView(ListView):
    def post(self,request):
        branch = request.data.get('branch')

