
class ATCException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        ret = "[ATC_EXCEPTION] %s" % str(self.message)
        print(ret)
        return ret
        
    
    
