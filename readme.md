## Практика python3 в автотестах
### 001 Виртуальное окружение (Virtual Environment)
```powershell
python -m venv venv # cоздание виртуального окружения

.\venv\Scripts\activate # активация виртуального окружения
```

### 002 unittest
```python
import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        sum_ = 2+2
        assert sum_ == 4

    def test2(self):
        sum_ = 2+2
        self.assertEqual (sum_,4)

# if __name__ == '__main__':
#     unittest.main()
```

```powershell
python -m unittest 001_test.py -v
python -m unittest 001_test.MyTest.test2 -v
```

