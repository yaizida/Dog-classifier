from sqlalchemy import Column, String

from core.db import Base


class TraningResult(Base):
    image_path = ...
    breed = ...  # порода
    prediction_precent = ...
