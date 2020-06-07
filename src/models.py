from . import db


class Status(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'ORDER_STATUS'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(64), index=False, unique=False, nullable=False)

    def serialize(self):
        return {"id": self.id,
                "desc": self.desc
                }

    def __repr__(self):
        return '<Status {}>'.format(self.name)


class Product(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'PRODUCT_INFO'
    productId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productName = db.Column(db.String(64), index=False, nullable=False, primary_key=True, autoincrement=False)
    productBrand = db.Column(db.String(64), index=False, unique=True, nullable=False, primary_key=True,
                             autoincrement=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    amount = db.Column(db.BigInteger, index=False, unique=False, nullable=False)
    quantity = db.Column(db.BigInteger, index=False, unique=False, nullable=False)

    def serialize(self):
        return {"productId": self.productId,
                "productName": self.productName,
                "productBrand": self.productBrand,
                "created": self.created,
                "amount": self.amount,
                "quantity": self.quantity}

    def __repr__(self):
        return '<Product {}>'.format(self.name)


class Order(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'ORDER_INFO'
    orderId = db.Column(db.Integer, primary_key=True)
    accountId = db.Column(db.Integer, db.ForeignKey("ACCOUNT_INFO.accountId"), index=False, unique=False,nullable=False)
    productId = db.Column(db.Integer, index=False, nullable=False)
    productName = db.Column(db.String(64), index=False, nullable=False)
    productBrand = db.Column(db.String(64), index=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    amount = db.Column(db.Integer, index=False, unique=False, nullable=True)
    status = db.Column(db.BigInteger, db.ForeignKey("ORDER_STATUS.id"), index=False, unique=False, nullable=False)
    quantity = db.Column(db.BigInteger, index=False, unique=False, nullable=False)
    __table_args__ = (db.ForeignKeyConstraint([productId, productName, productBrand],[Product.productId, Product.productName, Product.productBrand]),)

    def serialize(self):
        return {"orderId": self.orderId,
                "accountId": self.accountId,
                "productId": self.productId,
                "created": self.created,
                "amount": self.amount,
                "status": self.status
                }

    def __repr__(self):
        return '<Order {}>'.format(self.name)


class Account(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'ACCOUNT_INFO'
    accountId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    address = db.Column(db.Text, index=False, unique=False, nullable=True)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)
    mobile = db.Column(db.BigInteger, index=False, unique=False, nullable=False)

    def serialize(self):
        return {"accountId": self.accountId,
                "name": self.name,
                "email": self.email,
                "created": self.created,
                "mobile": self.mobile,
                "address": self.address,
                "admin": self.admin}

    def __repr__(self):
        return '<Account {}>'.format(self.name)
