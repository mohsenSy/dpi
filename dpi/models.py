from .app import db

class HTTPrequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    method = db.Column(db.String(10))
    url = db.Column(db.String(1000))
    version = db.Column(db.String(10))

    @classmethod
    def add(cls, method, url, version = "HTTP/1.1"):
        data = {
            "method": method,
            "url": url,
            "version": version
        }
        request = cls(**data)
        db.session.add(request)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
    @classmethod
    def get_requests(cls):
        return cls.query.all()
