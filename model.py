#sqlacodegen --schema public --outfile model.py postgresql+psycopg2://postgres:root@localhost:5432/moviesDB
# coding: utf-8
from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Date, ForeignKey, Integer, Numeric, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    homepage = Column(String(100))
    origin_country = Column(String(50))
    headquarters = Column(String(100))

    movies = relationship('Movie', secondary='public.movies_companies')


class Genre(Base):
    __tablename__ = 'genres'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    movies = relationship('Movie', secondary='public.movies_genres')


class Movie(Base):
    __tablename__ = 'movies'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    status = Column(String(50))
    runtime = Column(Integer)
    revenue = Column(BigInteger)
    release_date = Column(Date)
    popularity = Column(Numeric, index=True)
    overview = Column(Text)
    original_title = Column(String(100))
    original_language = Column(String(50))
    budget = Column(BigInteger)
    adult = Column(Boolean)
    vote_count = Column(Integer)
    vote_average = Column(Numeric)


class Person(Base):
    __tablename__ = 'people'
    __table_args__ = (
        CheckConstraint('(gender >= 0) AND (gender <= 3)'),
        {'schema': 'public'}
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True)
    gender = Column(Integer, server_default=text("0"))
    popularity = Column(Numeric, index=True)


t_relatorio_movies = Table(
    'relatorio_movies', metadata,
    Column('movie_id', Integer),
    Column('movie_title', String(100)),
    Column('movie_original_title', String(100)),
    Column('movie_original_language', String(50)),
    Column('movie_status', String(50)),
    Column('movie_runtime', Integer),
    Column('movie_budget', BigInteger),
    Column('movie_revenue', BigInteger),
    Column('movie_release_date', Date),
    Column('movie_popularity', Numeric),
    Column('movie_vote_count', Integer),
    Column('movie_vote_average', Numeric),
    Column('genre_id', Integer),
    Column('genre_name', String(50)),
    Column('company_id', Integer),
    Column('company_name', String(100)),
    Column('company_homepage', String(100)),
    Column('company_origin_country', String(50)),
    Column('company_headquarters', String(100)),
    Column('review_id', String(50)),
    Column('review_author', String(100)),
    Column('review_rating', Integer),
    schema='public'
)


t_relatorio_movies_companies = Table(
    'relatorio_movies_companies', metadata,
    Column('movie_id', Integer),
    Column('title', String(100)),
    Column('original_title', String(100)),
    Column('original_language', String(50)),
    Column('status', String(50)),
    Column('runtime', Integer),
    Column('budget', BigInteger),
    Column('revenue', BigInteger),
    Column('release_date', Date),
    Column('popularity', Numeric),
    Column('vote_count', Integer),
    Column('vote_average', Numeric),
    Column('companies_id', Integer),
    Column('companies_name', String(100)),
    Column('companies_homepage', String(100)),
    Column('companies_origin_country', String(50)),
    Column('companies_headquarters', String(100)),
    schema='public'
)


t_relatorio_movies_crew = Table(
    'relatorio_movies_crew', metadata,
    Column('movie_id', Integer),
    Column('title', String(100)),
    Column('original_title', String(100)),
    Column('original_language', String(50)),
    Column('status', String(50)),
    Column('runtime', Integer),
    Column('budget', BigInteger),
    Column('revenue', BigInteger),
    Column('release_date', Date),
    Column('popularity', Numeric),
    Column('vote_count', Integer),
    Column('vote_average', Numeric),
    Column('person_id', Integer),
    Column('gender', Integer),
    Column('person_popularity', Numeric),
    Column('job', String(100)),
    Column('department', String(100)),
    schema='public'
)


t_relatorio_movies_genres = Table(
    'relatorio_movies_genres', metadata,
    Column('movie_id', Integer),
    Column('title', String(100)),
    Column('original_title', String(100)),
    Column('original_language', String(50)),
    Column('status', String(50)),
    Column('runtime', Integer),
    Column('budget', BigInteger),
    Column('revenue', BigInteger),
    Column('release_date', Date),
    Column('popularity', Numeric),
    Column('vote_count', Integer),
    Column('vote_average', Numeric),
    Column('genre_id', Integer),
    Column('genre_name', String(50)),
    schema='public'
)


t_relatorio_movies_reviews = Table(
    'relatorio_movies_reviews', metadata,
    Column('movie_id', Integer),
    Column('title', String(100)),
    Column('original_title', String(100)),
    Column('original_language', String(50)),
    Column('status', String(50)),
    Column('runtime', Integer),
    Column('budget', BigInteger),
    Column('revenue', BigInteger),
    Column('release_date', Date),
    Column('popularity', Numeric),
    Column('vote_count', Integer),
    Column('vote_average', Numeric),
    Column('review_id', String(50)),
    Column('author', String(100)),
    Column('content', Text),
    Column('rating', Integer),
    schema='public'
)


t_relatorio_movies_tcast = Table(
    'relatorio_movies_tcast', metadata,
    Column('movie_id', Integer),
    Column('title', String(100)),
    Column('original_title', String(100)),
    Column('original_language', String(50)),
    Column('status', String(50)),
    Column('runtime', Integer),
    Column('budget', BigInteger),
    Column('revenue', BigInteger),
    Column('release_date', Date),
    Column('movie_popularity', Numeric),
    Column('vote_count', Integer),
    Column('vote_average', Numeric),
    Column('person_id', Integer),
    Column('name', String(100)),
    Column('gender', Integer),
    Column('person_popularity', Numeric),
    Column('character', String(100)),
    Column('department', String(100)),
    schema='public'
)


class Crew(Base):
    __tablename__ = 'crew'
    __table_args__ = {'schema': 'public'}

    id = Column(String(50), primary_key=True)
    job = Column(String(100))
    department = Column(String(100))
    personid = Column(ForeignKey('public.people.id', ondelete='CASCADE'), nullable=False, index=True)
    movieid = Column(ForeignKey('public.movies.id', ondelete='CASCADE'), nullable=False, index=True)

    movie = relationship('Movie')
    person = relationship('Person')


t_movies_companies = Table(
    'movies_companies', metadata,
    Column('movieid', ForeignKey('public.movies.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('companyid', ForeignKey('public.companies.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    schema='public'
)


t_movies_genres = Table(
    'movies_genres', metadata,
    Column('movieid', ForeignKey('public.movies.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    Column('genreid', ForeignKey('public.genres.id', ondelete='CASCADE'), primary_key=True, nullable=False),
    schema='public'
)


class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
        CheckConstraint('(rating >= 0) AND (rating <= 10)'),
        {'schema': 'public'}
    )

    id = Column(String(50), primary_key=True)
    author = Column(String(100))
    content = Column(Text)
    rating = Column(Integer)
    movieid = Column(ForeignKey('public.movies.id', ondelete='CASCADE'), nullable=False)

    movie = relationship('Movie')


class Tcast(Base):
    __tablename__ = 'tcast'
    __table_args__ = {'schema': 'public'}

    id = Column(String(50), primary_key=True)
    character = Column(String(100))
    department = Column(String(100))
    personid = Column(ForeignKey('public.people.id', ondelete='CASCADE'), nullable=False, index=True)
    movieid = Column(ForeignKey('public.movies.id', ondelete='CASCADE'), nullable=False, index=True)

    movie = relationship('Movie')
    person = relationship('Person')
