from ..models.DBModel import Movie
from ..config.Config import db
import csv

class MoiveService:
    @staticmethod
    def create_movie():
        # CSV 파일 경로 설정
        csv_file_path = 'app/static/MovieDataList.csv'  # 여기에 실제 파일 경로를 넣어주세요

        # CSV 파일을 읽어와서 데이터베이스에 삽입
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
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
