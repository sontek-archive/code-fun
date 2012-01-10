import hashlib
from collections import defaultdict

class Customer(object):
    def _get_email(self):
        return self._email

    def _set_email(self, email):
        primary, domain = email.lower().strip().split('@')
        primary = primary.split('+')[0]
        primary = primary.replace('.', '')
        self._email = ''.join([primary, '@', domain])

    def _get_street(self):
        return self._street

    def _set_street(self, street):
        st = street.lower().strip()
        st = st.replace('street', 'st.')
        st = st.replace('road', 'rd.')
        self._street = st

    def _get_state(self):
        return self._state

    def _set_state(self, state):
        st = state.upper().strip()

        if st == 'ILLINOIS':
            st = 'IL'
        elif st == 'NEW YORK':
            st = 'NY'
        elif st == 'CALIFORNIA':
            st = 'CA'

        self._state = st

    def _get_city(self):
        return self._city

    def _set_city(self, city):
        self._city = city.lower().strip()

    def _get_cc(self):
        return self._cc

    def _set_cc(self, cc):
        self._cc = hashlib.md5(cc).hexdigest()

    def _get_order_id(self):
        return self._order_id

    def _set_order_id(self, order_id):
        self._order_id = int(order_id)

    order_id = property(_get_order_id, _set_order_id)
    email = property(_get_email, _set_email)
    street = property(_get_street, _set_street)
    state = property(_get_state, _set_state)
    city = property(_get_city, _set_city)
    cc = property(_get_cc, _set_cc)

    @property
    def address(self):
        return ','.join([self.street, self.city, self.state, self.postal_code])

    def __init__(self, order, deal, email, street, city, state, postal, cc):
        self.order_id = order
        self.deal = deal
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal
        self.cc = cc

length = int(raw_input())

customers = defaultdict(set)

for index in range(1, length+1):
    test = raw_input()
    c = Customer(*test.split(','))
    customers[c.email + c.deal].add(c)
    customers[c.address + c.deal].add(c)

fraud_orders = set()

for key, orders in customers.items():
    if len(set(c.cc for c in orders)) > 1:
        for c in orders:
            fraud_orders.add(c.order_id)

print ','.join([str(i) for i in sorted(fraud_orders)])
