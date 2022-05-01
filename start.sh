if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BXBotz2021/Spider-Bot.git /Spidey
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Spidey
fi
cd /Spidey
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
