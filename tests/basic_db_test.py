from sqlalchemy import create_engine

# connect_string = 'sqlite:///:memory:'
connect_string = 'mysql+pymysql://root:@localhost/sample_db_local'

engine = create_engine(connect_string, echo=True)
print(engine)