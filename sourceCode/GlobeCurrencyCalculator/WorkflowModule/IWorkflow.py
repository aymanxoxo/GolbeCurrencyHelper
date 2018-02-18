from abc import ABC, abstractmethod

class IWorkflow(ABC):
    
    def __init__(self, input):
        self.InputEntity = input

    @abstractmethod
    def Handle(self):
        pass