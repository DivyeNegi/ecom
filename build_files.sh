echo "BUILD START"

python3 -m pip install -r requirements.txt

echo "Installing tailwindcss and dependencies..."
python3 manage.py tailwind install

echo "Building tailwindcss..."
python3 manage.py tailwind build

echo "Migrating Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"