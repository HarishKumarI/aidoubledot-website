from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,UniqueConstraint
from webapp import app

db = SQLAlchemy(app)

class PreregisteredUser(db.Model):
    __tablename__ = "preregistered_users"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    phone = db.Column('phone', db.Unicode, unique=True, nullable=False)
    email = db.Column('email', db.Unicode, unique=True, nullable=False)
    batch = db.Column('batch', db.Unicode)
    address = db.Column('address', db.Unicode)
    message = db.Column('message', db.Unicode)
    toReference = db.Column('to_reference', db.Unicode)
    fromReference = db.Column('from_reference', db.Unicode)
    creationDate = db.Column('creation_date', db.Date, default=datetime.utcnow)
    # __table_args__ = (
    #     UniqueConstraint('phone', 'email', name='_customer_location_uc'),
    # )


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    identifier = db.Column('identifier', db.Unicode, unique=True, nullable=False)
    preregisterDiscount = db.Column('preregister_discount', db.Integer, default=0)
    mcqWeight = db.Column('mcq_weight', db.Integer, default=0)
    earlyBirdDiscount = db.Column('early_bird_discount', db.Integer)
    earlyBirdExpiry = db.Column('early_bird_expiry', db.Date)
    fee = db.Column('fee', db.Integer, default=0)
    courseExpiry = db.Column('course_expiry', db.Date)
    creationDate = db.Column('creation_date', db.Date, default=datetime.utcnow)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column('id', db.Integer, primary_key=True)
    orderId = db.Column('order_id', db.Unicode, unique=True)
    course = db.Column('course', db.Unicode, ForeignKey("courses.identifier"), nullable=False)
    amount = db.Column('amount', db.Float)
    paymentStatus = db.Column('payment_status', db.Unicode)
    batch = db.Column('batch', db.Unicode)
    address = db.Column('address', db.Unicode, nullable=False)
    pincode = db.Column('pincode', db.Unicode, nullable=False)
    message = db.Column('message', db.Unicode)
    toReference = db.Column('toReference', db.Unicode)
    fromReference = db.Column('fromReference', db.Unicode)
    creationDate = db.Column('creation_date', db.Date, default=datetime.utcnow)


class RegisteredUsers(db.Model):
    __tablename__ = "registered_users"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, nullable=False)
    phone = db.Column('phone', db.Unicode, nullable=False)
    email = db.Column('email', db.Unicode, nullable=False)
    preregistered_user = db.Column('preregistered_user', db.Integer, ForeignKey("preregistered_users.id"), nullable=True)
    orderId = db.Column('order_id', db.Unicode, ForeignKey("orders.order_id"), nullable=False)
    isGroup = db.Column('is_group', db.Boolean, default=False)
    amount = db.Column('amount', db.Float)
    discountNotes = db.Column('discount_notes', db.Unicode)
    course = db.Column('course', db.Unicode, ForeignKey("courses.identifier"), nullable=False)
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)
    __table_args__ = (
        UniqueConstraint('phone', 'email', 'course', name='_user_course_uc'),
    )