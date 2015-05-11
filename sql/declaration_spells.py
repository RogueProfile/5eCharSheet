from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


#replace is_component with components enum list?
#enum for school
#is_blah sounds weird in some places
Base = declarative_base()
class Spell(Base):
	__tablename__ = 'spells'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	level = Column(Integer)
	school = Column(String)
	is_ritual = Column(Boolean)
	casting_time = Column(String)
	is_concentration = Column(Boolean)
	range = Column(Integer)
	is_verbal = Column(Boolean)
	is_stochastic = Column(Boolean)
	is_material = Column(Boolean)
	is_costly_material = Column(Boolean)
	materials = Column(String)
	duration = Column(String)
	description = Column(String)

