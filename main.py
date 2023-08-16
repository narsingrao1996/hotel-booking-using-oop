import pandas as pd

df = pd.read_csv("hotels.csv")
df1=pd.read_csv("cards.csv").to_dict(orient="records")
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()


    def book_hotel(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv",index=False)


    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        if availability == "yes":
            return True

        else:
            return False



class Reservation:
    def __init__(self,customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_ticket(self):
        content = f"""
        THANK YOU FOR RESERVATION
        HERE IS THE YOU BOOKING DATA 
        NAME:{self.customer_name}
        HOTEL NAME:{self.hotel.name}
        """
        return content
class CreditCard:
    def __init__(self,number):
        self.number = number

    def validate(self,expiration,holder,cvc):
        card_data = {"number" : self.number, "expiration" : expiration,
                     "holder" : holder, "cvc": cvc}
        if card_data in df1:
            return True
        else:
            return False





print(df)

hotel_ID = int(input("enter a hotel id want to book:"))
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number="5678")
    if credit_card.validate(expiration="12/28",holder="JANE SMITH", cvc="456"):
        hotel.book_hotel()

    name = input("enter your name:")
    reservation_ticket = Reservation(customer_name=name,hotel_object=hotel)
    print(reservation_ticket.generate_ticket())
else:
    print("no room available")