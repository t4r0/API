from tastypie.resources import  Resource

class Busqueda(Resource):
    
    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)
        
    def prepend_urls(self):
        from django.conf.urls import url
        return [    
            url(r'^busqueda/(?P<keyworkd>\w+)/$', self.wrap_view('get_search'), name='masterPieces_dispatched'),                   
            ]
enabled_resources=[]