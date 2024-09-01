<VirtualHost *:443>  
   ServerName example.com
   ExampleForm
   ServerAlias www.example.com  
   DocumentRoot /var/www/html  
  
   SSLEngine on  
   SSLCertificateFile /path/to/certificate.crt  
   SSLCertificateKeyFile /path/to/private/key.key  
</VirtualHost>
