from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://user:password@localhost/burnin?charset=utf8',
    connect_args = {
        'port': 3306
    },
    echo='debug',
    echo_pool=True
)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)

Base = declarative_base()

def init_db():
    import burnin.models
    Base.metadata.create_all(engine)

    from burnin.models import User
    db_session.add_all([
        User(username='pinghero', password='fortinet'),
        User(username='test', password='fortinet')
    ])
    db_session.commit()

    print 'Initialized the database.'
