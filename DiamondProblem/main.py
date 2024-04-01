class A:
    """
    A class representing class A.

    Methods:
        introduce: Returns information about class A.
    """
    def introduce(self):
        """
        Returns a string introducing class A.

        Returns:
            str: A string introducing class A.
        """
        return "I am class A."


class B(A):
    """
    A class representing class B, which inherits from class A.

    Methods:
        introduce: Returns information about class B.
    """
    def introduce(self):
        """
        Returns a string introducing class B.

        Returns:
            str: A string introducing class B.
        """
        return "I am class B."


class C(A):
    """
    A class representing class C, which inherits from class A.

    Methods:
        introduce: Returns information about class C.
    """
    def introduce(self):
        """
        Returns a string introducing class C.

        Returns:
            str: A string introducing class C.
        """
        return "I am class C."


class D(B, C):
    """
    A class representing class D, which inherits from classes B and C.

    Methods:
        introduce: Returns information about class D.
    """
    def introduce(self):
        """
        Returns a string introducing class D.

        Returns:
            str: A string introducing class D.
        """
        return "I am class D."


instance_a = A()
instance_b = B()
instance_c = C()
instance_d = D()

print(instance_a.introduce())
print(instance_b.introduce())
print(instance_c.introduce())
print(instance_d.introduce())
