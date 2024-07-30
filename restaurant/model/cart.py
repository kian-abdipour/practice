from sqlalchemy import Column, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Session, column_property


from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.cart_item import CartItem
from restaurant.database import get_session

for database_session in get_session():
    db_session = database_session


class Cart(DateTimeMixin, Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    total_quantity = column_property(db_session.query(func.count(CartItem.cart_id)).filter(id == CartItem.cart_id))
    total_amount = column_property(db_session.query(func.sum(CartItem.total_amount)).filter(id == CartItem.cart_id))
    customer_id = Column(ForeignKey('customer.id'))

    customer = relationship('Customer', back_populates='cart')
    items = relationship('CartItem', back_populates='cart')

    @classmethod
    def add(cls, session: Session, customer_id):
        cart = cls(customer_id=customer_id)
        session.add(cart)

        session.commit()
        session.refresh(cart)

        return cart

    @classmethod
    def search_cart_by_customer(cls, session: Session, customer_id):
        cart = session.query(cls).filter(cls.customer_id == customer_id).one()

        return cart

    @classmethod
    def search_cart_by_id(cls, session: Session, cart_id):
        cart = session.query(cls).filter(cls.id == cart_id).one_or_none()

        return cart

    @classmethod
    def show_item_identifiers_in_a_cart(cls, session: Session, customer_id):
        cart = session.query(cls).filter(cls.customer_id == customer_id).one_or_none()
        if cart is None:
            return None

        cart_items = session.query(CartItem).filter(cls.id == cart.id).all()

        return cart_items


