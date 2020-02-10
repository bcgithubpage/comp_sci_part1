class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = determine_card_type()
        self.valid = True

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        myCard = self.card_number
        if myCard[0] == '4':
            return 'VISA'
        elif myCard[0:2] =='34' or myCard[0:2]=='37':
            return 'AMEX'
        elif myCard[0:2] == '51' or myCard[0:2] =='52' or myCard[0:2] =='53' or myCard[0:2] == '54' or myCard[0:2] =='55':
            return 'MASTERCARD'
        elif myCard[0:4] == '6011':
            return 'DISCOVER'
        else:
            return 'INVALID CARD TYPE'

# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if len(str(self.card_number)) == 15 or len(str(self.card_number)) == 16:
            print('Valid')
        elif len(str(self.card_number)) < 15:
            print('The {} you entered is too short'.format(self.card_number))
        else:
            print('The {} you entered is too long'.format(self.card_number))

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        myCard = self.card_number
        new_card = []
        card_list = list(map(int,str(myCard)))
        #reverse the order  
        card_list.reverse()
        #if odd, double the number
        for i in range(len(card_list)):
            if i % 2 !=0:
                card_list[i] = card_list[i] * 2
        #if integer is greater than 9, then add the two digits
        for i in card_list:
            if i <= 9:
                new_card.append(i)
            else:
                i = sum(int(x) for x in str(i))
                new_card.append(i)
        #new_card.reverse()
        total = sum(new_card)
        #if the sum of the new number totals 80, then valid
        if total%10 != 0:
            return 'Invalid'
        else:
            return 'Valid'
        

# do not modify assert statements
cc = CreditCard('9999999999999999')
print(cc.determine_card_type())
print(cc.validate())

#assert cc.valid == False, "Credit Card number cannot start with 9"
#assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440000000000000000000000')
print(cc.check_length())

# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

# cc = CreditCard('5515460934365316')

# assert cc.valid == True, "Mastercard is Valid"
# assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')
#print(cc.determine_card_type())
#print(cc.validate())

#assert cc.valid == True, "Discover Card is Valid"
#assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"
