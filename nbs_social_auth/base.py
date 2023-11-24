

class BaseOAuth:
    AUTHORIZATION_URL:str 
    ACCESS_TOKEN_URL:str
    ACCESS_TOKEN_METHOD:str
    REVOKE_TOKEN_URL:str
    REVOKE_TOKEN_METHOD:str
    
    
    
    def get_auth_url(self):
        return self.AUTHORIZATION_URL
    
    def validate_code(self,code:str):
        pass
    
    