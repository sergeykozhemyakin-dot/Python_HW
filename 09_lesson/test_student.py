import pytest
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()


db_url = os.getenv("DATABASE_URL")


@pytest.fixture
def db():
    engine = create_engine(db_url)
    yield engine
    engine.dispose()


@pytest.fixture
def created_user(db):
    user_id = 123456
    with db.connect() as conn:
        conn.execute(
            text('INSERT INTO public.users (user_id, user_email, subject_id) VALUES (:id, :email, 1)'),
            {"id": user_id, "email": "test@pytest.ru"}
        )
        conn.commit()
        yield user_id
        conn.execute(text('DELETE FROM public.student WHERE user_id = :id'), {"id": user_id})
        conn.execute(text('DELETE FROM public.users WHERE user_id = :id'), {"id": user_id})
        conn.commit()


def test_add_student(db, created_user):
    with db.connect() as conn:
        conn.execute(
            text('INSERT INTO public.student (user_id, level, education_form) VALUES (:uid, :lvl, :form)'),
            {"uid": created_user, "lvl": "Beginner", "form": "personal"}
        )
        conn.commit()

        res = conn.execute(
            text('SELECT level FROM public.student WHERE user_id = :uid'),
            {"uid": created_user}
        ).scalar()
        assert res == 'Beginner'


def test_update_student(db, created_user):
    with db.connect() as conn:
        conn.execute(text('INSERT INTO public.student (user_id, level) VALUES (:uid, :lvl)'),
                     {"uid": created_user, "lvl": "Beginner"})
        conn.commit()

        conn.execute(text('UPDATE public.student SET level = :lvl WHERE user_id = :uid'),
                     {"lvl": "Advanced", "uid": created_user})
        conn.commit()

        res = conn.execute(text('SELECT level FROM public.student WHERE user_id = :uid'),
                           {"uid": created_user}).scalar()
        assert res == 'Advanced'


def test_delete_student(db, created_user):
    with db.connect() as conn:
        conn.execute(text('INSERT INTO public.student (user_id) VALUES (:uid)'), {"uid": created_user})
        conn.commit()
        conn.execute(text('DELETE FROM public.student WHERE user_id = :uid'), {"uid": created_user})
        conn.commit()
        count = conn.execute(text('SELECT count(*) FROM public.student WHERE user_id = :uid'),
                             {"uid": created_user}).scalar()
        assert count == 0
