from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from model import *

class DAO():
    def getEngine():
        engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/moviesDB")
        return engine

    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/moviesDB")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
       

class DAORelatorioMovies:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None:
            movies = session.query(t_relatorio_movies)
        elif conditionsFilters is None and conditionOrderBy is None:
            movies = session.query(*[t_relatorio_movies.c[field] for field in report_fields])
        elif conditionOrderBy is None:
            movies = session.query(*[t_relatorio_movies.c[field] for field in report_fields]).filter(text(conditionsFilters))
        elif conditionsFilters is None:
            movies = session.query(*[t_relatorio_movies.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        else:
            movies = session.query(*[t_relatorio_movies.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))
        
        return movies


class DAORelatorioMoviesGenres:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None:
            genres = session.query(t_relatorio_movies_genres)
        elif conditionsFilters is None and conditionOrderBy is None:
            genres = session.query(*[t_relatorio_movies_genres.c[field] for field in report_fields])
        elif conditionOrderBy is None:
            genres = session.query(*[t_relatorio_movies_genres.c[field] for field in report_fields]).filter(text(conditionsFilters))
        elif conditionsFilters is None:
            genres = session.query(*[t_relatorio_movies_genres.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        else:
            genres = session.query(*[t_relatorio_movies_genres.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))

        return genres


class DAORelatorioMoviesCompanies:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None and report_fields is None:
            companies = session.query(t_relatorio_movies_companies)
        elif conditionsFilters is None and conditionOrderBy is None:
            companies = session.query(*[t_relatorio_movies_companies.c[field] for field in report_fields])
        elif conditionsFilters is None:
            companies = session.query(*[t_relatorio_movies_companies.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        elif conditionOrderBy is None:
            companies = session.query(*[t_relatorio_movies_companies.c[field] for field in report_fields]).filter(text(conditionsFilters))
        else:
           companies = session.query(*[t_relatorio_movies_companies.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))

        return companies


class DAORelatorioMoviesTcast:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None and report_fields is None:
            tcast = session.query(t_relatorio_movies_tcast)
        elif conditionsFilters is None and conditionOrderBy is None:
            tcast = session.query(*[t_relatorio_movies_tcast.c[field] for field in report_fields])
        elif conditionsFilters is None:
            tcast = session.query(*[t_relatorio_movies_tcast.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        elif conditionOrderBy is None:
            tcast = session.query(*[t_relatorio_movies_tcast.c[field] for field in report_fields]).filter(text(conditionsFilters))
        else:
           tcast = session.query(*[t_relatorio_movies_tcast.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))

        return tcast


class DAORelatorioMoviesCrew:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None and report_fields is None:
            crew = session.query(t_relatorio_movies_crew)
        elif conditionsFilters is None and conditionOrderBy is None:
            crew = session.query(*[t_relatorio_movies_crew.c[field] for field in report_fields])
        elif conditionsFilters is None:
            crew = session.query(*[t_relatorio_movies_crew.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        elif conditionOrderBy is None:
            crew = session.query(*[t_relatorio_movies_crew.c[field] for field in report_fields]).filter(text(conditionsFilters))
        else:
            crew = session.query(*[t_relatorio_movies_crew.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))

        return crew

class DAORelatorioMoviesReviews:
    def select(session, conditionsFilters, conditionOrderBy, report_fields):
        if conditionsFilters is None and conditionOrderBy is None and report_fields is None:
            reviews = session.query(t_relatorio_movies_reviews)
        elif conditionsFilters is None and conditionOrderBy is None:
            reviews = session.query(*[t_relatorio_movies_reviews.c[field] for field in report_fields])
        elif conditionsFilters is None:
            reviews = session.query(*[t_relatorio_movies_reviews.c[field] for field in report_fields]).order_by(text(conditionOrderBy))
        elif conditionOrderBy is None:
            reviews = session.query(*[t_relatorio_movies_reviews.c[field] for field in report_fields]).filter(text(conditionsFilters))
        else:
            reviews = session.query(*[t_relatorio_movies_reviews.c[field] for field in report_fields]).filter(text(conditionsFilters)).order_by(text(conditionOrderBy))

        return reviews