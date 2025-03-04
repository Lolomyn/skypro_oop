from abc import ABC, abstractmethod


class BaseOrder(ABC):

    @abstractmethod
    def add_product(self, product):
        pass
