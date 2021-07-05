import json
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from backend.Save_Entity_To_DB import Update_Entity_On_Db, Save_Entity_To_Db, Delete_Entity_from_Db
from backend.Save_sabscription_To_DB import Delete_subscription_from_Db, Save_subscription_To_Db
from connector.request_broker import Get_entity_by_id, Get_entity_by_type, Update_entity, Create_entity, Delete_entity, \
    Get_subscription_by_id, Create_subscription, Get_subscriptions, Delete_subscription
from rest_framework.views import APIView



class Request_entity(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        json_body = json.loads(request.body)
        if json_body['id'] == "urn:ngsi-ld:AgriDevice:AgriDSoil:IPex12:00043" or json_body['id'] == "urn:ngsi-ld:AgriDevice:AgriDSoil:IPex12:00044":
            return HttpResponse('you are not allowed to do this operation  !!!', status=400)
        else:
            print(json.dumps(json_body, indent=4))
            print('saving entity.........')

            # chek if the entity exists in context broker
            print('cheking the if the device exists in the context broker............')
            try:
                entity = Get_entity_by_id(json_body['id'])
            except:
                print('connextion to cb faild')
                pass
            if entity.status_code == 200:
                print("updating Device DATA..................")
                try:
                    updat = Update_entity(json_body)
                    updat_db = Update_Entity_On_Db(json_body)
                except:
                    print('device {} could not be updated '.format(json_body['id']))
                    pass
                if updat.status_code == 204:
                    print("+ updated succesfely ^^")
                else:
                    print('+ updated on local DB')
                    print('- could not be updated on CB')
                return HttpResponse('- already exist on context broker \n \n + saved on local DB', status= 204)
            else:
                print("- entity dosnn't exist........")
                print('creating entity .......')
                try:
                    print('saving entity to local DB..........')
                    updat = Create_entity(json_body)
                    # save the device in the local database (MONGO_DB)
                    Save_Entity_To_Db(json_body)
                except:
                    print('- device {} could not be created '.format(json_body['id']))
                    return HttpResponse("server error", status= 500)
                    pass
                if updat.status_code == 201:
                    print("created succesfely ^^")
                    return HttpResponse("created succesfely ^^", status= 201)

    def get(self, request):
        json_body = json.loads(request.body)
        json_keys = list(dict.keys(json_body))
        print(json_keys[0])
        if json_keys[0] == 'id':
            try:
                entity = Get_entity_by_id(json_body['id'])
            except:
                print('connextion to cb faild')
                return HttpResponse(status= 500)
                pass
        elif json_keys[0] == 'type':
            try:
                entity = Get_entity_by_type(json_body['type'])
            except:
                print('connextion to cb faild')
                return HttpResponse(status= 500)
                pass
        else:
            return HttpResponse('try with id or type',status=400)
        json_entity = json.loads(entity.text)
        if entity.status_code == 200:
            # save the device in the local database (MONGO_DB)
            Save_Entity_To_Db(json_entity)
        print(entity)
        j_entity = json.dumps(json_entity, indent=4, sort_keys= False)
        print(j_entity)
        return HttpResponse(j_entity, status= entity.status_code, content_type='application/ld+json')

    def delete(self, request):
        json_body = json.loads(request.body)

        json_keys = list(dict.keys(json_body))
        print(json_keys[0])
        if json_keys[0] == 'id':
            if json_body['id'] == "urn:ngsi-ld:AgriDevice:AgriDSoil:IPex12:00043" or json_body[
                'id'] == "urn:ngsi-ld:AgriDevice:AgriDSoil:IPex12:00044":
                return HttpResponse('you are not allowed to do this operation  !!!', status=400)
            else:
                try:
                    entity = Delete_entity(json_body['id'])
                    Delete_Entity_from_Db(json_body['id'], json_keys[0])

                except:
                    print('connextion to cb faild')
                    pass
                print(entity)
                if entity.status_code == 204:
                    return HttpResponse('entity has been deleted successfully', status=204)
                elif entity.status_code == 404:
                    return HttpResponse("entity dosn't exist", status=404)
                elif entity.status_code == 400:
                    return HttpResponse("bad request", status=400)
                else:
                    return HttpResponse("server error", status=500)

        elif json_keys[0] == 'type':
            try:
                entity= Delete_Entity_from_Db(json_body['type'], json_keys[0])

            except:
                print('connextion to cb faild')
                pass
            print(entity.deleted_count)
            return HttpResponse(f"deleted entities: {entity.deleted_count} ", status=204)

class Request_subscription(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        json_body = json.loads(request.body)

        print(json.dumps(json_body, indent=4))
        print('saving subscription.........')

        # chek if the subscription exists in context broker
        print('creating subscription .......')
        try:
            print('saving entity to local DB..........')
            subscription = Create_subscription(json_body)
            # save the subscription on the local database (MONGO_DB)
            Save_subscription_To_Db(json_body)
        except:
            print('- subscription {} could not be created '.format(json_body['id']))
            return HttpResponse("server error", status= 500)
            pass
        if subscription.status_code == 201:
            print("created succesfely ^^")
            return HttpResponse("created succesfely ^^", status= 201)

    def get(self, request):
        try:
            json_body = json.loads(request.body)
            json_keys = list(dict.keys(json_body))
            print(json_keys[0])
            if json_keys[0] == 'id':
                try:
                    subscription = Get_subscription_by_id(json_body['id'])
                except:
                    print('connextion to cb faild')
                    return HttpResponse(status= 500)
                    pass
        except:
            try:
                subscription = Get_subscriptions()
            except:
                print('connextion to cb faild')
                return HttpResponse(status= 500)
                pass
            pass
        else:
            return HttpResponse("try with 'id' or leave body void", status=400)
        json_subscription = json.loads(subscription.text)
        if subscription.status_code == 200:
            # save the subscription in the local database (MONGO_DB)
            Save_subscription_To_Db(json_subscription)
        print(subscription)
        j_subscription = json.dumps(json_subscription, indent=4, sort_keys= False)
        print(j_subscription)
        return HttpResponse(j_subscription, status= subscription.status_code, content_type='application/ld+json')

    def delete(self, request):
        json_body = json.loads(request.body)

        json_keys = list(dict.keys(json_body))
        print(json_keys[0])
        if json_keys[0] == 'id':
            try:
                subscription = Delete_subscription(json_body['id'])
                Delete_subscription_from_Db(json_body['id'], json_keys[0])

            except:
                print('connextion to cb faild')
                pass
            print(subscription)
            if subscription.status_code == 204:
                return HttpResponse('subscription has been deleted successfully', status=204)
            elif subscription.status_code == 404:
                return HttpResponse("subscription dosn't exist", status=404)
            elif subscription.status_code == 400:
                return HttpResponse("bad request", status=400)
            else:
                return HttpResponse("server error", status=500)

        elif json_keys[0] == 'type':
            try:
                subscription= Delete_subscription_from_Db(json_body['type'], json_keys[0])

            except:
                print('connextion to cb faild')
                pass
            print(subscription.deleted_count)
            return HttpResponse(f"deleted subscriptions: {subscription.deleted_count} ", status=204)