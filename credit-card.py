class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = None
        self.valid = False

# Create and add your method called `determine_card_type` to the CreditCard class:
    def determine_card_type(self):
        if self.card_number[0] == '4':
            self.card_type = 'VISA'
            return self.card_type
        elif self.card_number[0:2] == '51' or self.card_number[0:2] =='52' or self.card_number[0:2] == '53' or self.card_number[0:2] == '54' or self.card_number[0:2] =='55':
            self.card_type = 'MC'
            return self.card_type
        elif self.card_number[0:2] =='34' or self.card_number[0:2] == '37':
            self.card_type = 'AMEX'
            return self.card_type
        elif self.card_number[0:4] =='6011':
            self.card_type = 'Discover'
            return self.card_type
        else:
            return 'Error'

# Create and add your method called `check_length` to the CreditCard class:
    def check_length(self):
        if len(self.card_number) == 16 and self.card_type == 'MS':
            return self.card_type
        elif len(self.card_number) ==16 and self.card_type == 'Discover':
            return self.card_type
        elif len(self.card_number) == 16 and self.card_type == 'VISA':
            return self.card_type
        elif len(self.card_number) ==15 and self.card_type =='AMEX':
            return self.card_type
        else:
            return 'ERROR: Incorrect card length'

# # Create and add your method called 'validate' to the CreditCard class:
    def validate(self):
        valid_test = list(self.card_number)
        valid_test = valid_test[::-1]
        valid_test = list(map(int, valid_test))
        #print(valid_test)
        for i in range(0, len(valid_test)):
            if i%2 !=0:
                valid_test[i] = valid_test[i] * 2
                #print(valid_test[i])
                if valid_test[i] > 9:
                    valid_test[i] = str(valid_test[i])
                    valid_test[i] = valid_test[i][0:2]
                    valid_test[i] = list(map(int, valid_test[i]))
                    valid_test[i] = valid_test[i][0] + valid_test[i][1]
                #print(valid_test[i])
        valid_sum = sum(valid_test)
        #print(valid_sum)
        if valid_sum % 10 ==0:
            self.valid = True
            return self.valid
        else:
            return self.valid

      
#fake card numbers to try: 347650202246884 4485040993287616
card1 = '4485040993287616'
card2 = '347650202246884'
#my_cc = CreditCard(card1)
my_cc = CreditCard(card2)
(my_cc.validate())

if (my_cc.determine_card_type()) == (my_cc.check_length()) and my_cc.validate() == True:
    print(my_cc.determine_card_type(), ': Valid Card')
else:
    print('Invalid Card')


