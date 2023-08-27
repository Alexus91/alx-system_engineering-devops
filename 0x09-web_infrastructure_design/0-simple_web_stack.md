### 0. Simple web stack 
https://raw.githubusercontent.com/Alexus91/alx-system_engineering-devops/master/0x09-web_infrastructure_design/0.%20Simple%20web%20stack%20.png


## Server:
A server is a powerful computer system that hosts and serves resources to other computers over a network. In this case, our server will be responsible for hosting the website and its components.

## Domain Name:
A domain name is a human-readable address that is used to access websites instead of using numerical IP addresses. In our case, the domain name is foobar.com. The "www" prefix is a common subdomain used to specify the web server.

## DNS Record:
The www record in www.foobar.com is a CNAME (Canonical Name) DNS record that points to the server's IP address, which is 8.8.8.8. DNS (Domain Name System) translates human-readable domain names into IP addresses so that computers can communicate with each other.

## Web Server (Nginx):
The web server's role is to handle incoming HTTP requests from users' browsers and serve the appropriate web content. In this case, Nginx will receive the user's request for www.foobar.com and retrieve the relevant files from the application server.

## Application Server:
The application server hosts the application codebase. It processes dynamic content and generates responses based on user requests. When Nginx receives a request, it forwards the request to the application server, which then processes it and sends back the necessary data to be displayed on the user's browser.

## Application Files:
The application files contain the code that defines the website's functionality and dynamic content. These files are hosted on the application server and are responsible for generating the appropriate responses to user requests.

## Database (MySQL):
The database stores structured data that the application needs to function. This can include user information, content, settings, etc. MySQL is a popular relational database management system used to organize and manage this data.

## Communication with User's Computer:
When a user requests the website, their computer sends an HTTP request to the server. The request is then processed by Nginx, which forwards dynamic content requests to the application server and retrieves data from the database if needed. The server sends back an HTTP response containing the requested content, which is then displayed in the user's browser.
