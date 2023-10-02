from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class AddReview:
    restaurant_id: int
    rating: int
    comment: Optional[str]


@dataclass
class GetReviews:
    restaurant_id: int

@dataclass
class GetReviewsStats:
    restaurant_id: int


@dataclass
class DeleteReview:
    review_id: int


# @dataclass
# class UpdateProduct:
#     name: str
#     price: int
