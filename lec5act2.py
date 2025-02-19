class Counter:
    number_of_counters = 0

    # Constructor
    def __init__(self, max_tickets=None):
        self.ticket_num = 0 
        self.max_tickets = max_tickets
        Counter.number_of_counters += 1
        

    def next_value(self):
        if self.max_tickets == self.ticket_num:
            self.ticket_num = None
        else:
            self.ticket_num += 1
        return self.ticket_num  
    
    def reload(self):
        self.ticket_num = 0 