from sqlalchemy import Column, Unicode, ForeignKey, Integer
from restaurant.model.base import Base
from sqlalchemy.orm import relationship, Session
from restaurant.model.mixin import DateTimeMixin


class Address(DateTimeMixin, Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(Unicode(150), nullable=False)
    customer_id = Column(ForeignKey('customer.id'))

    orders = relationship('Order', cascade='all, delete')
    customer = relationship('Customer', back_populates='addresses')

    @classmethod
    def add(cls, session: Session, customer_id, address):
        address = cls(address=address, customer_id=customer_id)
        session.add(address)
        session.commit()
        session.refresh(address)

        return address

    @classmethod
    def show_all_for_admin(cls, session: Session, address_filter):
        sorted_addresses = address_filter.sort(address_filter.sort(session.query(cls))).all()

        return sorted_addresses

    @classmethod
    def show_all_for_customer(cls, session: Session, customer_id, address_filter):
        result = address_filter.sort(session.query(cls).filter(cls.customer_id == customer_id)).all()

        return result

    @classmethod
    def search_for_customer(cls, session: Session, address_id, customer_id):
        result = session.query(cls).filter(cls.id == address_id, cls.customer_id == customer_id).one_or_none()

        return result

    @classmethod
    def search_for_admin(cls, session: Session, address_id, address_filter):
        result = session.query(cls).filter(cls.id == address_id).one_or_none()

        return result
    
    @classmethod
    def delete(cls, session: Session, address_id, customer_id):
        address = cls.search_for_customer(session, address_id, customer_id)
        result = session.query(cls).filter(cls.id == address_id, cls.customer_id == customer_id).delete()

        session.commit()

        if result == 1:
            return address

        else:
            return None

