FALLBACK_PHONE: float = 1e00000000

def get_phone():
    phone = input("Type your phone number: ")

    if not phone:        
        return round( FALLBACK_PHONE )
    
    return int(phone)

if __name__ == "__main__":
    my_phone = get_phone()
    print(f"Your phone number is: {my_phone}")