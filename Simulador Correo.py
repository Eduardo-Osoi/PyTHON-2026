
def main():
    
    tory = User("Tory")
    ramy = User("Ramy")
    
    
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    
    # Ramy envía un correo a Tory
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")
    
    
    ramy.check_inbox()
    
    
    ramy.read_email(1)
    
    
    ramy.delete_email(1)
    
    
    ramy.check_inbox()


if __name__ == '__main__':
    main()