def gen_but(received_message):
    greet_inputs =  ["hi", "hello", "wassup", "hey"]
    day_inputs = ["morning", "afternoon", "after noon", "evening", "night"]

    buttons = []
    message_lower = received_message.lower()
    
    if message_lower in greet_inputs:
        buttons = [
            {"title": "About Us", "payload": "/about company"},
            {"title": "Contact", "payload": "/contact"},
            {"title": "Services", "payload": "/service"}
        ]

    if "service" in message_lower or "services" in message_lower:
        buttons = [
            {"title": "AI Products", "payload": "/products"},
            {"title": "Staffing", "payload": "/staffing"},
            {"title": "Consulting", "payload": "/consult"}
        ]

    elif message_lower in day_inputs:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]

    elif "/products" in message_lower or "ai products" in message_lower or "products" in message_lower:
        buttons = [
            {"title": "Staffing", "payload": "/staffing"},
            {"title": "Consulting", "payload": "/consult"}
        ]

    elif "/staffing" in message_lower or "staffing" in message_lower or "staff" in message_lower:
        buttons = [
            {"title": "AI Products", "payload": "/products"},
            {"title": "Consulting", "payload": "/consult"}
        ]

    elif "/consult" in message_lower or "consultancy" in message_lower or "consulting" in message_lower:
        buttons = [
            {"title": "AI Products", "payload": "/products"},
            {"title": "Staffing", "payload": "/staffing"}
        ]

    elif "expertise" in message_lower or "expertises" in message_lower:
        buttons = [
            {"title": "AI", "payload": "/technology"},
            {"title": "RPA", "payload": "/rpa"},
            {"title": "Cloud Computing", "payload": "/cloud"},
            {"title": "Cyber Security", "payload": "/cyber"},
            {"title": "Big Data", "payload": "/bda"}
        ]
        
    elif "/technology" in message_lower:
        buttons = [
            {"title": "RPA", "payload": "/rpa"},
            {"title": "Cloud Computing", "payload": "/cloud"},
            {"title": "Cyber Security", "payload": "/cyber"},
            {"title": "Big Data", "payload": "/bda"}
        ]
        
    elif "/rpa" in message_lower or "rpa" in message_lower or "robotic" in message_lower:
        buttons = [
            {"title": "AI", "payload": "/technology"},
            {"title": "Cloud Computing", "payload": "/cloud"},
            {"title": "Cyber Security", "payload": "/cyber"},
            {"title":"Big Data", "payload": "/bda"}
        ]
        
    elif "/cloud" in message_lower or "cloud" in message_lower:
        buttons = [
            {"title": "AI", "payload": "/technology"},
            {"title": "RPA", "payload": "/rpa"},
            {"title": "Cyber Security", "payload": "/cyber"},
            {"title": "Big Data", "payload": "/bda"}
        ]
        
    elif "/cyber" in message_lower or "cyber" in message_lower or "security" in message_lower or "cybersecurity" in message_lower:
        buttons = [
            {"title": "AI", "payload": "/technology"},
            {"title": "RPA", "payload": "/rpa"},
            {"title": "Cloud Computing", "payload": "/cloud"},
            {"title": "Big Data", "payload": "/bda"}
        ]
        
    elif "/bda" in message_lower or "bda" in message_lower or "data" in message_lower:
        buttons = [
            {"title": "AI", "payload": "/technology"},
            {"title": "RPA", "payload": "/rpa"},
            {"title": "Cyber Security", "payload": "/cyber"},
            {"title": "Cloud Computing", "payload": "/cloud"}
        ]

    elif "contact" in message_lower or "contacts" in message_lower:
        buttons = [
            {"title": "Mail ID", "payload": "/mail"},
            {"title": "Location", "payload": "/location"},
            {"title": "WhatsApp", "paylaod": "/whatsapp"}
        ]

    elif "media" in message_lower or "accounts" in message_lower:
        buttons = [
            {"title": "Facebook", "payload": "/facebook"},
            {"title": "LinkedIn", "payload": "/linkedin"},
            {"title": "Instagram", "payload": "/instagram"}
        ]
        
    elif message_lower == "about" or "about company" in message_lower or "your company" in message_lower:
        buttons = [
            {"title": "Facebook", "payload": "/facebook"},
            {"title": "LinkedIn", "payload": "/linkedin"},
            {"title": "Instagram", "payload": "/instagram"}
        ]

    elif "address" in message_lower:
        buttons = [
            {"title": "Mail ID", "payload": "/mail"},
            {"title": "Location", "payload": "/location"}
        ]

    elif any(keyword in message_lower for keyword in ["whatsapp", "whats app", "what's app", "costing", "cost", "pricing", "price", "demo", "demonstration", "career", "internship", "intern"]):
        buttons = [
            {"title": "WhatsApp", "payload": "/whatsapp"},
            {"title": "Mail ID", "payload": "/mail"}
        ]
        
    elif "/mail" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "/location" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "/facebook" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "/linkedin" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "/instagram" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "/about company" in message_lower:
        buttons = [
            {"title": "Satisfied", "payload": "/satisfy"},
            {"title": "Needs Improvement", "payload": "/improvement"}
        ]
        
    elif "facebook" in message_lower or "face" in message_lower:
        buttons = [
            {"title": "Facebook", "payload": "/facebook"}
        ]
        
    elif "instagram" in message_lower or "insta" in message_lower:
        buttons = [
            {"title": "Instagram", "payload": "/instagram"}
        ]
    
    elif "linkedin" in message_lower or "linked" in message_lower:
        buttons = [
            {"title": "LinkedIn", "payload": "/linkedin"}
        ]

    return buttons
