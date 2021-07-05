from django.http import HttpResponse


def home(request):

    from backend.NGSI_Interpreter.POST_Entitty import Create_entity
    
    create_entity = Create_entity(payload)
    print("created services : ")
    return HttpResponse("biw")
class home_notify:
    template_page='CBResponse.html'
    def post(self, request):
        text = request.POST
        args = {'text':text }
        #return render(request,self.template_page,args)
        return HttpResponse(self.template_page,args)

    def get(self, request):
        return HttpResponse('Welcome')

def notifications(requests):




    return HttpResponse("notifications:", requests)