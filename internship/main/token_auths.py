import jwt


def create_token(user):
    payload = {
        
            "user_id": user.id,
            "email": user.email,
            "password": user.password,
            "superuser": user.is_superuser,  
    }

    key = "drf"
    token = jwt.encode(payload=payload,key=key)
    return token

def decode_token(token):
    key = "drf"
    payload = jwt.decode(token,key=key,algorithms="HS256")
    return payload
    

