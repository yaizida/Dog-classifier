from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Классификация пород собоак'
    description: str = ('Проект для классификации пород собак через обучении' +
                        'модели на scikit-learn')

    class Config:
        env_file = '.env'


settings = Settings()
