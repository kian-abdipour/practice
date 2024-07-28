from sqlalchemy import Column, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Session, ColumnProperty


from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model.cart_item import CartItem
from restaurant.database import get_session


class Cart(DateTimeMixin, Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    total_quantity = ColumnProperty(get_session().query(func.count(CartItem.cart_id)).join(id == CartItem.cart_id))
    total_amount = ColumnProperty(get_session().query(func.sum(CartItem.total_amount)).join(id == CartItem.cart_id))

    customer = relationship('Customer', cascade='all, delete')
    items = relationship('CartItem', cascade='all, delete')

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

