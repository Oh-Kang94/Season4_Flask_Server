from ..models.DBModel import Review
from ..config.Config import db
from datetime import datetime


class ReviewService:
    @staticmethod
    def create_review(user_email, movie_id, content, rating):
        existing_review = ReviewService.get_review(user_email, movie_id)
        if not existing_review:
            new_review = Review(
                user_email=user_email,
                movie_id=movie_id,
                content=content,
                rating=rating,
                insertdate=datetime.now().strftime("%Y.%m.%d")
            )
            db.session.add(new_review)
            db.session.commit()
            return new_review
        else:
            return None

    @staticmethod
    def get_review_all(movie_id):
        return Review.query.filter_by(movie_id=movie_id, deletedate=None).all()
    
    @staticmethod
    def get_review(user_email, movie_id):
        return Review.query.filter_by(user_email=user_email, movie_id=movie_id, deletedate=None).first()

    @staticmethod
    def update_review(user_email, movie_id, content, rating):
        review = ReviewService.get_review(user_email, movie_id)
        if review:
            review.content = content
            review.rating = rating
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete_review(user_email, movie_id):
        review = ReviewService.get_review(user_email, movie_id)
        if review:
            review.deletedate = datetime.now().strftime("%Y.%m.%d")
            db.session.commit()
            return True
        return False
