class Memento:
    def __init__(self, value):
        self.state=value

    def set_state(self, value):
        self.state=value

    def get_state(self):
        return self.state


class Originator:
    def set_state(self, value):
        self.state=value

    def get_state(self):
        return self.state

    def createMemento(self):
        return (Memento(self.state))

    def setMemento(self, memento):
        print("going to previous state")
        self.state=memento.get_state()


class Caretaker:
    def __init__(self, originatorObj):
        self.memento = None
        self.origin=originatorObj

    def execute(self):
        self.memento=self.origin.createMemento()
        self.origin.set_state(0)

    def unexecute(self):
        self.origin.setMemento(self.memento)
        
        
originator =Originator()
originator.set_state(1)
print("the state value is: ", originator.get_state())

caretaker=Caretaker(originator)
caretaker.execute()
print("the state value is: ", originator.get_state())

caretaker.unexecute()
print("the state value is: ", originator.get_state())

