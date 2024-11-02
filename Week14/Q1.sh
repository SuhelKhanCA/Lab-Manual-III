#!/bin/bash

# Update package index
sudo apt update

# Install necessary packages
sudo apt install -y apache2 php libapache2-mod-php mysql-server php-mysql

# Start and enable Apache and MySQL services
sudo systemctl start apache2
sudo systemctl enable apache2
sudo systemctl start mysql
sudo systemctl enable mysql

# Create a sample PHP file
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

# Set permissions
sudo chown -R www-data:www-data /var/www/html

# Print success message
echo "Web server setup completed. Access the server at http://localhost/info.php"
