from ..models.DBModel import Movie, Cast
from sqlalchemy import text
from ..config.Config import db
import csv

class MoiveService:
    @staticmethod
    def create_movie():
        # CSV 파일 경로 설정
        db.session.query(Movie).delete()

        db.session.execute(text('ALTER TABLE movie AUTO_INCREMENT = 1;'))
        csv_file_path = 'app/static/MovieDataList.csv'  # 여기에 실제 파일 경로를 넣어주세요

        # CSV 파일을 읽어와서 데이터베이스에 삽입
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # UTF-8 관련 예외 처리
                try:
                    summary=row['summary']
                except ValueError:
                    summary = '0'
                
                new_movie = Movie(
                    ott=row['ott'],
                    title=row['title'],
                    imagepath=row['imagepath'],
                    releasedate=row['releasedate'],
                    genre=row['genre'],
                    totalaudience=int(row['totalaudience']),
                    country=row['country'],
                    rating=row['rating'],
                    star=float(row['star']),
                    runningtime=int(row['runningtime']),
                    summary=row['summary']
                )
                db.session.add(new_movie)

        # 데이터베이스에 변경사항 반영
        db.session.commit()
        return True
    
    @staticmethod
    def create_cast():
        # CSV 파일 경로 설정
        csv_file_path = 'app/static/MovieCastData.csv'
        # db.session.query(Cast).delete()

        db.session.execute(text('ALTER TABLE cast AUTO_INCREMENT = 1;'))

        # CSV 파일을 읽어와서 데이터베이스에 삽입
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                new_cast = Cast(
                    movie_id = row['movie_id'],
                    imgpath=row['imgpath'],
                    name=row['name'],
                    role=row['role']
                )
                db.session.add(new_cast)

        # 데이터베이스에 변경사항 반영
        db.session.commit()
        return True
    
    @staticmethod
    def get_movie():
        movies = Movie.query.all()
        movie_list = []
        for movie in movies:
            movie_data = {
                'id': movie.id,
                'ott': movie.ott,
                'title': movie.title,
                'imagepath': movie.imagepath,
                'releasedate': movie.releasedate,
                'genre': movie.genre,
                'totalaudience': movie.totalaudience,
                'country': movie.country,
                'rating': movie.rating,
                'star': movie.star,
                'runningtime': movie.runningtime,
                'summary': movie.summary
            }
            movie_list.append(movie_data)
        db.session.commit()
        return movie_list
    
    @staticmethod
    def get_movie_one(movie_id):
        return Movie.query.filter_by(id=movie_id).first()

    
    @staticmethod
    def get_cast():
        casts = Cast.query.all()
        cast_list = []
        for cast in casts:
            cast_data = {
                'id': cast.id,
                'movie_id' : cast.movie_id,
                'imgpath' : cast.imgpath,
                'name' : cast.name,
                'role' : cast.role,
            }
            cast_list.append(cast_data)
        db.session.commit()
        return cast_list
    
    @staticmethod
    def get_cast_one(movie_id):
        return Cast.query.filter_by(movie_id=movie_id).all()