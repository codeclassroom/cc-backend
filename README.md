# cc_backend

### Prerequisties
- Python 3.6.8+
- virtualenv

### Installation

1. Create Virtual Environment.
```bash
virtualenv -p python3 <name>
```
2. Clone repository.
```bash
git clone https://github.com/codeclassroom/cc_backend.git
```
3. Install Dependencies.
```bash
pip3 install requirements.txt
```
4. Migrate Changes.
```bash
python3 manage.py migrate
```
5. Run Server
```bash
python3 manage.py runserver
```
