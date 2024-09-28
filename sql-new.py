from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Bett(base):
    __tablename__ = "Bet"
    id = Column(Integer, primary_key=True)
    bookmaker = Column(String)
    sport = Column(String)
    bet = Column(String)
    match = Column(String)
    description = Column(String)
    stake = Column(Integer)
    odds = Column(String)
    outcome = Column(String)
    returned = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Bet table
bet1 = Bett(
    bookmaker = "Bet365",
    sport = "Football",
    bet = "Brighton to win",
    match = "Brighton v Hull",
    description = "Single",
    stake = 20.75,
    odds = "8/15",
    outcome = "Win",
    returned = 28.05
)

session.add(bet1)

# commit our session to the database
session.commit()

all_bets = session.query(Bet)
for bet in all_bets:
    print(
        bet.id,
        bet.bet,
        bet.odds,
        bet.outcome,
        bet.returned,
        sep=" || "
    )
