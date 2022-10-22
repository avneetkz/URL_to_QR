# install and import modules using: pip install qrcode 
# pip install image
import qrcode
import image

# define function to create QR codeg
def url_to_qr(data):
    # calling QRCode attribute from qrcode module 
    # defining the size of code in paramenters
    qr= qrcode.QRCode( version= 10,  
                       box_size= 50,
                       border= 30 )
    
    qr.add_data(data)
    # fit automatically detects the size if no size was given
    qr.make(fit= True)
    # converting qr to image
    img= qr.make_image( fill= 'white', back_colour= 'black')
    img.save('qr.png')

# driver code
if __name__ == "__main__":
    url= input("Enter the url : ")
    # function call 
    url_to_qr(url)

