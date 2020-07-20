"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price, qty=0):
        self.name = str(name)
        self.flavor = str(flavor)
        self.price = float(price)
        self.qty = int(qty)
        self.cache[name] = self
        

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def add_stock(self, amount):
        self.qty = self.qty + amount


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
