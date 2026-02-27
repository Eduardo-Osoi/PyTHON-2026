
def main():
    # Crear dos usuarios: Tory y Ramy
    tory = User("Tory")
    ramy = User("Ramy")
    
    # Tory envía un correo a Ramy
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    
    # Ramy envía un correo a Tory
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")
    
    # Ramy revisa su bandeja de entrada
    ramy.check_inbox()
    
    # Ramy lee el primer correo electrónico
    ramy.read_email(1)
    
    # Ramy elimina el primer correo electrónico
    ramy.delete_email(1)
    
    # Ramy revisa su bandeja de entrada nuevamente
    ramy.check_inbox()

# Llamar a la función main solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    main()