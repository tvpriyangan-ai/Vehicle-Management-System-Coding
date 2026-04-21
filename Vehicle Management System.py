# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:35:33 2026

@author: Priyangan
"""
class Vehicle:
    def __init__(self, model,make):
        
        self.__model=model
        self.__make=make
        self.__state= "stopped"
        
    def move(self):
        self.__state="Moving"
    
    def stop(self):
        self.__state="Stopped"

    def get_model(self):
        return self.__model
    
    def get_make(self):
        return self.__make

    def get_state(self):
        return self.__state

    def set_state(self,state):
        self.__state=state
    
    def __str__(self):
        return f"{self.get_model()} {self.get_make()} is {self.get_state()}"




class Bus(Vehicle):
    def __init__ (self,model,make,decks,seats):
        Vehicle.__init__(self,make, model)
        self.no_decks= decks
        self.no_seats=seats
        self.set_state=("not in use")
        self.__stop_index=0
        self.__route=["New Street","Bullring","Moor Street","BCU"]
        
    def get_no_decks(self):
        return self.no_decks
    
    def get_no_of_seats(self):
        return self.no_seats
    
    def get_route(self):
        return "-".join(self.__route)
    def move(self):
        if self.__stop_index < len(self.__route)-1:
            
            previous_stop = self.__route[self.__stop_index]
            next_stop = self.__route[self.__stop_index+1]
            
            print(f"The bus was at {previous_stop} and is moving to {next_stop}")
            self.__stop_index+=1
        else:
            print("I am finished for today!")
            
    def stop(self):
        print("I am a non-stop bus")
        
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} ( No of decks- {self.get_no_decks()},No of seats-{self.get_no_of_seats()})  is {self.get_state()}"

class Car(Vehicle):
    def __init__(self,model,make, doors,seats):
        Vehicle.__init__(self,make, model)
        self.__doors_no=doors
        self.__seats_no=seats
        
    def set_doors_no(self, number):
        self.__doors_no = number
        
    def set_seats_no(self, number):
        self.__seats_no = number
        
    def get_doors_no(self):
        return self.__doors_no
    
    def __str__(self):
       return f"{self.get_model()} {self.get_make()} with {self.get_doors_no()} door is {self.get_state()}"
        
    
bus = Bus("super luxury", "flix", 2, 60)
print(bus)
bus.move()
bus.move()
bus.move()
bus.move()


