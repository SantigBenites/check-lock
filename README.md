# check-lock

Simple docker app to check if the desktop enviroment is locked


## INSTALL 

## Package

sudo dpkg -i check-lock-web-deb.deb
sudo systemctl start check-lock-web@$(logname)
sudo systemctl enable check-lock-web@$(logname)

## Docker

docker compose up -d

## UNINSTALL

## Package

sudo systemctl stop check-lock-web@$(logname)
sudo systemctl disable check-lock-web@$(logname)
sudo systemctl daemon-reload
sudo dpkg -r check-lock-web
sudo rm -rf /opt/check-lock-web

## Docker

docker compose down

## VERIFY CLEANUP

sudo systemctl list-unit-files | grep check-lock
dpkg -l | grep check-lock-web

