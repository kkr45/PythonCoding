#This is an abstract Tree class

class Tree:
    """This is abstract position class"""
    class Position:

        def element(self):
            raise NotImplemented("This method needs to be implemented")

        def __eq__(self,other):
            raise NotImplemented("Equal to method needs to be implemented")

        def __ne__(self,other):
            return not (self == other)

    def root(self):
        raise NotImplemented("Root method needs to be implemented")

    def children(self,p):
        raise NotImplemented("Children method needs to be implemented")

    def parent(self,p):
        raise NotImplemented("Parent method needs to be implemented")

    def num_children(self,p):
        raise NotImplemented("num_children method needs to be implemented")

    def __len__(self):
        raise NotImplemented("length method needs to be implemented")

    def is_root(self,p):
        return  self.root() == p

    def is_leaf(self,p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0








