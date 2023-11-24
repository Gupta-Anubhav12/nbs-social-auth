


from .base import BaseOAuth
import requests

class GoogleOAuth2(BaseOAuth):
    
    AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
    ACCESS_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
    ACCESS_TOKEN_METHOD = "POST"
    REVOKE_TOKEN_URL = "https://accounts.google.com/o/oauth2/revoke"
    USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
    REVOKE_TOKEN_METHOD = "GET"
    DEFAULT_SCOPE = ["openid", "email", "profile"]
    TOKEN_ALGORITHM = ["HS256"]
    
    def __init__(self,*, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,GOOGLE_REDIRECT_URI):
    
        self.GOOGLE_CLIENT_ID  = GOOGLE_CLIENT_ID
        self.GOOGLE_REDIRECT_URI =GOOGLE_REDIRECT_URI
        self.GOOGLE_CLIENT_SECRET=GOOGLE_CLIENT_SECRET
        scope = "%20".join(self.DEFAULT_SCOPE)
        self.AUTHORIZATION_URL = f"{self.AUTHORIZATION_URL}?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope={scope}&access_type=offline"
                
    
    def validate_code(self,code):
        data = {
        "code": code,
        "client_id": self.GOOGLE_CLIENT_ID,
        "client_secret": self.GOOGLE_CLIENT_SECRET,
        "redirect_uri": self.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
        
        response = requests.request(
            method=self.ACCESS_TOKEN_METHOD,
            url = self.ACCESS_TOKEN_URL,
            data=data
        )
        access_token = response.json().get("access_token")
        user_info = requests.get(self.USER_INFO_URL, headers={"Authorization": f"Bearer {access_token}"})
        user_info=user_info.json()
       
        if "error" in user_info:
            raise ValueError(user_info.get("error",{}).get("message","AUTH FAILED"))
        
        return user_info