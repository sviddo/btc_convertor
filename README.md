<h3>BTC to UAH convertor api service</h3>

**Functionaly provided:**
- subscribe (provide yout email)
- get actual BTC to UAH rate
- send emails to all users with actual rate

Service consists of 6 endpoints:
1. - (any api service such as [Postman](https://www.postman.com/), but a browser) **/api/subscribe_api** is endpoint making subscription stuff done. Send ***POST*** request to it providing email: [example](https://im.ge/i/FPOck6)
   - (browser only) **/api/subscribe** endpoint actually wrapping **/api/subscribe_api** one and supposed to use in browsers: [example](https://im.ge/i/FP1MU1)
2. - (any api service such as [Postman](https://www.postman.com/), but a browser) **/api/rate_api** is endpoint calculating BTC price in UAHs and returning result. Send ***GET*** request to it: [example](https://im.ge/i/FP1NyY)
   - (browser only) **/api/subscribe** endpoint actually wrapping **/api/rate** one and supposed to use in browsers: [example](https://im.ge/i/FP1VZc)
3. - (any api service such as [Postman](https://www.postman.com/), but a browser) **/api/send_emails_api** is endpoint sending actual BTC to UAH rate to all registered users. Send ***GET*** request to it: [example](https://im.ge/i/FP23V6)
   - (browser only) **/api/send_emails** endpoint actually wrapping **/api/send_emails** one and supposed to use in browsers: [example](https://im.ge/i/FP2prC)
   
   ***!!! All sent emails you can find in ["All mail"](https://im.ge/i/FPddUp) or ["Spam"](https://im.ge/i/FPq0SM) folder in gmail ([https://mail.google.com](https://mail.google.com)). They looks [such](https://im.ge/i/FPqdKz)***
   
Find more info [https://coxit.stoplight.io/docs/btc-to-uah-convertor/](https://coxit.stoplight.io/docs/btc-to-uah-convertor/)

**How to run the application? Follow next steps:**
```
git clone https://github.com/sviddo/btc_convertor.git
cd btc_convertor
docker build -t django-app . 
docker run -p 8000:80 django-app 
```
After that follow next links to see the functionality of service (for browsers):
1. [http://127.0.0.1:8000/api/subscribe](http://127.0.0.1:8000/api/subscribe)
2. [http://127.0.0.1:8000/api/rate](http://127.0.0.1:8000/api/rate)
3. [http://127.0.0.1:8000/api/send_emails](http://127.0.0.1:8000/api/send_emails)

or use any API service (e.g. Postman):

[Endpoint collection](https://www.postman.com/sviddo/workspace/btc-to-uah/collection/21140281-d01b3b2f-8601-4af6-8c22-a3200274e306?action=share&creator=21140281) **!!! Desktop version of Postman is must to make requests to localhost**


Trird-party libraries used in project:
1. Email delivery service [Mailjet](https://www.mailjet.com/
) in role of SMTP server. Their SDK for Python: [https://github.com/mailjet/mailjet-apiv3-python](https://github.com/mailjet/mailjet-apiv3-python)
2. Cryptoccurency platform [CoinGecko](https://www.coingecko.com/) to get actual BTC price. Their SDK for Python: [https://github.com/man-c/pycoingecko](https://github.com/man-c/pycoingecko)
