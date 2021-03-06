"""Classes for melon orders."""

class AbstractMelonOrder():


    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == 'christmas':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = 'domestic'
    tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    def get_total(self):
    #     """Calculate price, including tax."""
        if self.qty < 10:
            return super().get_total() + 3
        else:
            return super().get_total()
    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

        # return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovermentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed