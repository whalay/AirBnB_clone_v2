#!/usr/bin/env bash
# This script sets up webservers for the deployment of the webstatic

# Update and install nginx if it doesnt exist
apt-get -y update
apt-get -y install nginx

# create these folders if they dont exist
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# create an html file with fake content to test configuration
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hello ALX</h1>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# remove the symbolic link if exist and recreate it
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership to the user and group ubuntu
chown -R ubuntu:ubuntu /data/

# update the nginx config the content of /data/web_static/current/ to hbnb_static
sed -i "s/^\s*location \/ {/\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n\n&/" /etc/nginx/sites-enabled/default

# restart the server
service nginx restart
