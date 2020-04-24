from .app import db

class TCPPacket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    srcPort = db.Column(db.Integer)
    dstPort = db.Column(db.Integer)
    srcIP = db.Column(db.String(15))
    dstIP = db.Column(db.String(15))

    @classmethod
    def add(cls, srcPort, dstPort, srcIP, dstIP):
        data = {
            "srcPort": srcPort,
            "dstPort": dstPort,
            "srcIP": srcIP,
            "dstIP": dstIP
        }
        tcp = cls(**data)
        db.session.add(tcp)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    @classmethod
    def get_tcp(cls):
        return cls.query.all()

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
