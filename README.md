# Credit Default ML Service

ML-сервис для прогнозирования дефолта по кредитным картам.


## Структура проекта

```text
├── app/
│   ├── __init__.py
│   └── model_handler.py
├── data/
│   └── UCI_Credit_Card.csv
├── models/
│   └── model.pkl
├── notebooks/
│   └── Untitled.ipynb
├── tests/
│   └── test_api.py
├── app.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## API
Сервис реализован на Flask.

## GET /health
Проверка работоспособности сервиса.

Пример запроса:
```commandline
curl.exe http://localhost:5000/health
```

Пример ответа:
```json
{
  "status": "ok"
}
```

## POST /predict
Принимает JSON с признаками клиента и возвращает предсказанный моделью класс и вероятность.

Пример запроса:
```commandline
curl.exe -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"LIMIT_BAL\":20000,\"SEX\":2,\"EDUCATION\":2,\"MARRIAGE\":1,\"AGE\":24,\"PAY_0\":2,\"PAY_2\":2,\"PAY_3\":-1,\"PAY_4\":-1,\"PAY_5\":-2,\"PAY_6\":-2,\"BILL_AMT1\":3913,\"BILL_AMT2\":3102,\"BILL_AMT3\":689,\"BILL_AMT4\":0,\"BILL_AMT5\":0,\"BILL_AMT6\":0,\"PAY_AMT1\":0,\"PAY_AMT2\":689,\"PAY_AMT3\":0,\"PAY_AMT4\":0,\"PAY_AMT5\":0,\"PAY_AMT6\":0}"
```

Пример ответа:

```json
{
  "prediction": 0,
  "probability": 0.23,
  "model_version": "v1"
}
```

## Запуск локально

```bash
pip install -r requirements.txt
python main.py
```

## Запуск через Docker
```bash
docker build -t credit-default-service .
docker run -p 5000:5000 credit-default-service
```


# Архитектура сервиса

В проекте используется монолитная архитектура