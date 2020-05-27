# zi_api_auth_client
To use this library you need to install the library *zi_api_auth_client* using pip.

This library supports 2 types of authentication methods. Both the methods return a JWT token which you can use to make
api calls for enterprise-api on production.

<ol>
<li>
<h4>Username and password authentication:</h4>
Usage:
<ol> 
<li>import zi_api_auth_client</li>
<li>jwt_token = zi_api_auth_client.user_name_pwd_authentication("your_user_name", "your_password") </li>
</ol>
<li>
<h4>PKI authentication:</h4> This type of authentication needs a private key and a client ID to generate the JWT token.
<br> Usage:
<ol> 
<li>
import zi_api_auth_client
</li>
<li>
Paste your private key.
<pre><code>
key = '''
-----BEGIN PRIVATE KEY-----
Your private key goes here
-----END PRIVATE KEY-----'''
</code></pre>
</li> 
<li>jwt_token = zi_api_auth_client.pki_authentication("your_user_name", "your_client_id", key) </li>
</ol>
</ol>

**Note: If you get the error "ValueError: Could not deserialize key data." when doing PKI authentication, make sure that
your private key has been properly formatted. Paste the private key as a multi-line string in python.**

*Correct way*: The following is the right way to paste your private key.
<pre><code>
'''
-----BEGIN PRIVATE KEY-----
Your private key goes here
-----END PRIVATE KEY-----'''
</code></pre>

*Wrong way*: Pasting the private key as follows would throw the error "ValueError: Could not deserialize key data." because
there are extra spaces on each line in the key.
<pre><code>
'''
                -----BEGIN PRIVATE KEY-----
                Your private key goes here
                -----END PRIVATE KEY-----'''
</code></pre>