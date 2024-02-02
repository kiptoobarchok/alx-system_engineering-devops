#!/usr/bin/env bash

# Install the Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create the default Nginx site configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Template for the default Nginx configuration
file { 'nginx/default.conf.erb':
  ensure  => 'file',
  content => '
server {
  listen 80;
  server_name _;  # Listen for any hostname on port 80

  # Root directory for static files
  root /var/www/html;

  # Index page
  index index.html index.htm;

  location /redirect_me {
    return 301 http://example.com/new-page;  # Replace with your desired target URL
  }
}
',
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}
